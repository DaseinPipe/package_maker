import os
from datetime import datetime
from package_maker.src.config.config_main import get_show_data, get_path
from package_maker.src.utils.general_utils import find_patten
from collections import defaultdict
import logging

__name = 'create vendor package'

logger = logging.getLogger('create_organization_package')
logger.info('------------------------------ make_link ---------------------------------------')

def run(**data):
    def get_shot_data(_discipline_folder_path, _discipline):
        shot_dict = {}
        if _discipline != 'Plates':
            for shot_folder in os.listdir(_discipline_folder_path):
                shot_folder_path = os.path.join(_discipline_folder_path, shot_folder)
                _shot = find_patten(shot_folder, [shot_name_regex])
                if not _shot:
                    logger.warning(f'cannot recognize {shot_folder_path} folder')
                    continue
                shot_dict[_shot] = shot_folder_path
        else:
            for episode_folder in os.listdir(_discipline_folder_path):
                episode_folder_path = os.path.join(_discipline_folder_path, episode_folder)
                for shot_folder in os.listdir(episode_folder_path):
                    shot_folder_path = os.path.join(episode_folder_path, shot_folder)
                    _shot = f'{episode_folder}_{shot_folder}'
                    shot_dict[_shot] = shot_folder_path
        return shot_dict

    source_dir_path = data['source_dir_path']
    destination_dir_path = data['destination_dir_path']
    job = data['job']
    date = datetime.today().strftime('%Y%m%d')
    show_data = get_show_data(job)
    disciplines = show_data.get('discipline')
    shot_name_regex = show_data.get('shot_name_regex')
    destination_path_data = {
        'pkg_dir': os.path.join(destination_dir_path, date)
    }
    for_dup_check = defaultdict(list)
    for discipline_folder in os.listdir(source_dir_path):
        discipline_folder_path = os.path.join(source_dir_path, discipline_folder)
        discipline = find_patten(
            text=discipline_folder.replace(' ', '_'),
            patterns=disciplines,
            get_matched_pattern=True
        )
        if not discipline:
            logger.warning(f'cannot recognize {discipline_folder_path}')
            continue
        destination_path_data['discipline'] = discipline
        shot_data = get_shot_data(discipline_folder_path, discipline)
        for shot, shot_path in shot_data.items():
            destination_path_data['shot'] = shot
            vendor_discipline_folder_template = get_path(job, 'vendor_discipline_folder_template')
            destination_path = vendor_discipline_folder_template.format(destination_path_data)
            if not os.path.exists(os.path.dirname(destination_path)):
                os.makedirs(os.path.dirname(destination_path))
            try:
                os.symlink(shot_path, destination_path, target_is_directory=True)
            except FileExistsError:
                logger.exception(f'having some error on {shot_path} symlink', exc_info=True)
            for_dup_check[destination_path].append(shot_path)

    for des_path, src_paths in for_dup_check.items():
        if len(src_paths) != 1:
            nl = '\n'
            logger.warning(f'{des_path} has duplicate src files :- \n{nl.join(src_paths)}')

    return 0, {
        'info': '',
        'return_data': {}
    }


if __name__ == '__main__':
    _data = dict(
        source_dir_path='/mnt/pb6/Filmgate/TRM/io/From_Client/Uel_2022-10-04/OFFICE SEQUENCES/',
        destination_dir_path='/mnt/pb6/Filmgate/TRM/io/To_Shakti/',
        job='trm',
    )
    run(**_data)
