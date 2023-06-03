import os
from datetime import datetime
from package_maker.src.config.config_client import get_show_data, get_path
from package_maker.src.utils.general_utils import find_patten as _find_patten
import re
import logging

__name = 'create vendor package'

logger = logging.getLogger('create_organization_package')
logger.info('------------------------------ make_link ---------------------------------------')


def run(**data):
    destination_dir_path = data.get('destination_dir_path')
    date = datetime.today().strftime('%Y%m%d')
    pkg_version = get_latest_pkg_version(destination_dir_path)

    data['destination_dir_path'] = os.path.join(data.get('destination_dir_path'), f'{date}_{pkg_version}')

    MakeLinkForRoot(**data)
    return 0, {
        'info': '',
        'return_data': {}
    }


def find_pattern(folder_path, patterns, what, get_matched_pattern=False, write_log=True):
    if not isinstance(patterns, list):
        patterns = [patterns]
    patterns = _find_patten(
        text=folder_path.replace(' ', '_'),
        patterns=patterns,
        get_matched_pattern=get_matched_pattern,
    )
    if write_log:
        if not patterns:
            logger.warning(f'{what}: UNKNOWN, cannot recognize {folder_path}')
    return patterns


def link(source_path, destination_path):
    if not os.path.exists(os.path.dirname(destination_path)):
        os.makedirs(os.path.dirname(destination_path))
    try:
        os.symlink(source_path, destination_path, target_is_directory=True)
    except FileExistsError:
        logger.exception(f'having some error on {source_path} symlink', exc_info=True)


def get_latest_pkg_version(pkg_dir):
    def get_existing_versions():

        if not os.path.exists(pkg_dir):
            os.makedirs(pkg_dir)
        pkg_names = sorted(os.listdir(pkg_dir))
        if not pkg_names:
            return first_version
        today = datetime.today().strftime('%Y%m%d')
        today_pkg_versions = []
        for pkg_name in pkg_names:
            pkg_version = next(iter(re.findall(today, pkg_name)), None)
            if pkg_version:
                today_pkg_versions.append(pkg_name[-1])

        if not today_pkg_versions:
            return first_version
        return sorted(today_pkg_versions)[-1]

    first_version = None
    lastest_version = get_existing_versions()
    if not lastest_version:
        return 'A'

    return chr(ord(lastest_version)+1)



class MakeLink:
    def __init__(self, **data):
        self.data = data
        self.source_dir_path = self.data['source_dir_path']
        self.destination_dir_path = data['destination_dir_path']
        self.job = data['job']
        self.show_data = get_show_data(self.job)
        self.disciplines = self.show_data.get('discipline')
        self.shot_name_regex = self.show_data.get('shot_name_regex')
        self.episode_name_regex = self.show_data.get('episode_name_regex')
        self.shot_no_regex = self.show_data.get('shot_no_regex')
        self.destination_path_data = {
            'pkg_dir': self.destination_dir_path,
            'job': self.job
        }

    def get_destination_path(self):
        vendor_discipline_folder_template = get_path(self.job, 'vendor_discipline_folder_template')
        return vendor_discipline_folder_template.format(self.destination_path_data)

    def check_folder_type(self, discipline=None):
        folders = self.source_dir_path.replace('\\', '/').split('/')
        if folders[-1]:
            latest_folder = folders[-1].replace(' ', '_')
        else:
            latest_folder = folders[-2].replace(' ', '_')

        if not discipline:
            return 'root'

        if discipline == 'Plates':
            folder_type_list = dict(
                episode=self.episode_name_regex,
                shot_no=self.shot_no_regex,
                discipline=self.disciplines,
            )
        else:
            folder_type_list = dict(
                shot_name=self.shot_name_regex,
                discipline=self.disciplines,

            )

        for folder_type, pattern in folder_type_list.items():
            result = find_pattern(
                folder_path=latest_folder,
                patterns=pattern,
                what=folder_type,
                write_log=False
            )
            if result:
                return folder_type
        return 'root'


class MakeLinkForRoot(MakeLink):
    def __init__(self, **data):
        super(MakeLinkForRoot, self).__init__(**data)
        discipline = find_pattern(
            folder_path=self.source_dir_path,
            patterns=self.disciplines,
            what='discipline',
            get_matched_pattern=True,
            write_log=False

        )
        folder_type = self.check_folder_type(discipline)
        if folder_type != 'root':
            MakeLinkForDiscipline(**data)
        else:
            for discipline_folder in os.listdir(self.source_dir_path):
                discipline_folder_path = os.path.join(self.source_dir_path, discipline_folder)
                discipline = find_pattern(
                    folder_path=discipline_folder_path,
                    patterns=self.disciplines,
                    what='discipline',
                    get_matched_pattern=True
                )
                if not discipline:
                    continue
                data[discipline] = discipline
                data['source_dir_path'] = discipline_folder_path
                MakeLinkForDiscipline(**data)


class MakeLinkForDiscipline(MakeLink):
    def __init__(self, **data):
        self.data = data.copy()
        super(MakeLinkForDiscipline, self).__init__(**self.data)
        if not self.data.get('discipline'):
            self.data['discipline'] = find_pattern(
                folder_path=self.source_dir_path,
                patterns=self.disciplines,
                what='discipline',
                get_matched_pattern=True
            )

        self.discipline = self.data['discipline']

        for shot_folder_path in self.get_shot_folder_path_list():
            self.data['source_dir_path'] = shot_folder_path
            MakeLinkForShot(**self.data.copy())

    def get_shot_folder_path_list(self):

        def get_plate_shots():
            shot_list = []
            if folder_type == 'discipline':
                for episode_folder in os.listdir(self.source_dir_path):
                    episode_folder_path = os.path.join(self.source_dir_path, episode_folder)
                    for shot_folder in os.listdir(episode_folder_path):
                        shot_folder_path = os.path.join(episode_folder_path, shot_folder)
                        shot_list.append(shot_folder_path)
            if folder_type == 'episode':
                for shot_folder in os.listdir(self.source_dir_path):
                    shot_folder_path = os.path.join(self.source_dir_path, shot_folder)
                    shot_list.append(shot_folder_path)
            if folder_type == 'shot_no':
                shot_list.append(self.source_dir_path)
            return shot_list

        def get_shots():
            shot_list = []
            if folder_type == 'discipline':
                for shot_folder in os.listdir(self.source_dir_path):
                    shot_folder_path = os.path.join(self.source_dir_path, shot_folder)
                    shot_list.append(shot_folder_path)
            if folder_type == 'shot_name':
                shot_list.append(self.source_dir_path)
            return shot_list

        folder_type = self.check_folder_type(self.discipline)
        if self.discipline == 'Plates':
            _shot_list = get_plate_shots()
        else:
            _shot_list = get_shots()
        return _shot_list


class MakeLinkForShot(MakeLink):
    def __init__(self, **data):
        super(MakeLinkForShot, self).__init__(**data)
        self.data = data
        self.discipline = self.data.get('discipline', None) or find_pattern(
            folder_path=self.source_dir_path,
            patterns=self.disciplines,
            what='discipline',
            get_matched_pattern=True
        )
        if not self.discipline:
            return
        if not os.path.isdir(self.source_dir_path):
            return
        self.destination_path_data['discipline'] = self.discipline

        self.shot = self.data.get('shot', None) or self.get_shot()
        if not self.shot:
            return
        self.destination_path_data['shot'] = self.shot

        self.destination_path = self.get_destination_path()

        link(self.source_dir_path, self.destination_path)

    def get_shot(self):
        if self.discipline == 'Plates':
            episode = find_pattern(
                folder_path=self.source_dir_path,
                patterns=self.episode_name_regex,
                what='episode_name'
            )
            shot_no = find_pattern(
                folder_path=self.source_dir_path,
                patterns=self.shot_no_regex,
                what='episode_name'
            )
            if not episode or not shot_no:
                return
            return f'{episode}_{shot_no}'
        else:
            shot = find_pattern(
                folder_path=self.source_dir_path,
                patterns=self.shot_name_regex,
                what='full_shot_name'
            )
            return shot


if __name__ == '__main__':
    # source_dir_path = '/mnt/pb6/Filmgate/TRM/io/From_Client/Uel_2022-10-04/OFFICE-SEQUENCES/Lighting/trm_ep01-rl01_00760_lighting_v0005/',
    _data = dict(
        source_dir_path='/mnt/pb6/Filmgate/TRM/io/From_Client/Uel_2022-10-04/OFFICE-SEQUENCES/',
        destination_dir_path='/home/rithik/rithik/test/To_Shakti/',
        job='trm',
        source_dir_type='shot'
    )
    run(**_data)
