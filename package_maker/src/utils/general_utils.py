import csv
import os.path
from pathlib import Path, PurePath
from tempfile import NamedTemporaryFile
import shutil

from package_maker.src.core.for_approval import *
from package_maker.src.utils import mpc_utils, filmgate_utils


def is_name_matched(text, patterns):
    for pattern in patterns:
        result = re.search(pattern, text, re.IGNORECASE)
        if result:
            return True
    return False


def is_ext_matched(filepath, ext_list):
    _ext = os.path.splitext(filepath)[-1]
    if _ext in ext_list:
        return True
    return False


def find_patten(text, patterns, get_matched_pattern=False):
    result_list = []
    for pattern in patterns:
        result = re.search(pattern, text, re.IGNORECASE)
        if result:
            if get_matched_pattern:
                return pattern
            else:
                return result.group(0)
    return None


def list_duplicates(seq):
    seen = set()
    seen_add = seen.add
    seen_twice = set(x for x in seq if x in seen or seen_add(x))
    return list(seen_twice)


def fix_nulls(s):
    for line in s:
        yield line.replace('\0', ' ')


def transferFile(scrFile, destFile, moveFlag=False):
    if not os.path.exists(os.path.dirname(destFile)):
        os.makedirs(os.path.dirname(destFile))

    if moveFlag:
        shutil.move(scrFile, destFile)
        return
    shutil.copyfile(scrFile, destFile)

    # print('Transfer complete...')


def assumed_pkg_type(dept, source_filepath):
    def get_ext_type(source_ext):
        img_ext_types = global_seq_ext
        app_ext_types = list(global_work_app_config.keys())
        if source_ext.split('.')[-1] in img_ext_types:
            return 'image'
        elif source_ext.split('.')[-1] in app_ext_types:
            return 'app'

    def get_matched_ext():
        matched_ext_list = []
        for pkg_dir_type in default_pkg_dir_type:
            pkg_dir_type_data = pkg_dir_type_dict[pkg_dir_type]
            matched_ext = is_ext_matched(source_filepath, pkg_dir_type_data.get('ext_list', []))
            if matched_ext:
                matched_ext_list.append(pkg_dir_type)
        if len(matched_ext_list) != 1:
            return 'select'
        else:
            return matched_ext_list[0]

    _, source_ext = os.path.splitext(source_filepath)
    SHOW_DATA = get_show_data(os.environ.get('show'))
    if os.environ.get('show') == 'TRM':
        return 'select'
    pkg_dir_type_dict = SHOW_DATA.get('pkg_dir_types', global_pkg_dir_types)
    ext_type = get_ext_type(source_ext)

    # first line of assuming
    if not ext_type:
        return 'select'

    # second line of assuming
    if source_ext not in global_discipline_pkg_type_assignment[dept][ext_type]['ext_list']:
        return 'select'
    # third line of assuming
    for pkg_dir_type, pkg_dir_type_data in pkg_dir_type_dict.items():
        if not pkg_dir_type_data:  # to ignore custom and select
            continue
        matched_name = is_name_matched(source_filepath, pkg_dir_type_data.get('match_list', []))
        matched_ext = is_ext_matched(source_filepath, pkg_dir_type_data.get('ext_list', []))
        if matched_name and matched_ext:
            return pkg_dir_type
    default_pkg_dir_type = global_discipline_pkg_type_assignment[dept][ext_type]['default']

    # forth line of assuming
    if isinstance(default_pkg_dir_type, list):
        return get_matched_ext()
    # fifth line of assuming
    return global_discipline_pkg_type_assignment[dept][ext_type]['default']


def update_shot_version(item_data):
    pkg_dir = Path(item_data['pkg_dir'])
    job_dir = pkg_dir.parents[2]
    dept = item_data['discipline']
    shot = item_data['shot']
    csv_path = PurePath(job_dir, ".package", 'to_client', f"{dept}.csv")
    default_client_version = 1
    fields = ['shot', 'client_version']

    csv_file = Path(csv_path)
    csv_file.touch(exist_ok=True)

    tempfile = NamedTemporaryFile(mode='w', delete=False)

    with open(csv_file, 'r') as csvfile, tempfile:
        reader = csv.DictReader(csvfile, fieldnames=fields)
        writer = csv.DictWriter(tempfile, fieldnames=fields)
        row_update = False
        writer.writeheader()

        for row in reader:

            if row['shot'] == 'shot' and row['client_version'] == 'client_version':
                continue

            if row['shot'] == shot:
                row_update = True
                row['shot'], row['client_version'], = row['shot'], str(int(row['client_version']) + 1)
            row = {'shot': row['shot'], 'client_version': row['client_version']}
            writer.writerow(row)
        if not row_update:
            row = {'shot': shot, 'client_version': str(default_client_version + 1)}
            writer.writerow(row)

    shutil.move(tempfile.name, csv_file)


def get_latest_shot_version(item_data):
    # print(item_data)
    pkg_dir = Path(item_data['pkg_dir'])
    dept = item_data['discipline']
    if 'sitw' in str(pkg_dir):
        job_dir = pkg_dir.parents[1]
    else:
        job_dir = pkg_dir.parents[2]
    csv_path = PurePath(job_dir, ".package", 'to_client', f"{dept}.csv")
    shot = item_data['shot']

    default_client_version = 1
    fields = ['shot', 'client_version']

    csv_file = Path(csv_path)
    csv_file.parents[0].parents[0].mkdir(parents=True, exist_ok=True)
    csv_file.touch(exist_ok=True)
    with open(csv_file, 'r') as csvfile:
        reader = csv.DictReader(fix_nulls(csvfile), fieldnames=fields)
        for row in reader:
            if row['shot'] == shot:
                return int(row['client_version'])
    return default_client_version


def get_custom_element_descs(item_data):
    pkg_dir = Path(item_data['pkg_dir'])
    if 'sitw' in str(pkg_dir):
        job_dir = pkg_dir.parents[1]
    else:
        job_dir = pkg_dir.parents[2]
    csv_path = PurePath(job_dir, ".package", "shot_list.csv")
    dept = item_data['discipline']
    shot = item_data['shot']
    fields = ['Shot', 'roto_custom_name', 'prep_custom_name', 'comp_custom_name', 'matchmove_custom_name']
    custom_name = ''
    with open(csv_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=fields)
        for row in reader:
            if row['Shot'] == shot:
                try:
                    custom_name = row[f'{dept}_custom_name']
                except:
                    pass
    if not custom_name:
        return []
    return custom_name.split(',')


def get_shots(item_data):
    pkg_dir = Path(item_data['pkg_dir'])
    if 'sitw' in str(pkg_dir):
        job_dir = pkg_dir.parents[1]
    else:
        job_dir = pkg_dir.parents[2]
    csv_path = PurePath(job_dir, ".package", "shot_list.csv")
    if not os.path.exists(os.path.dirname(csv_path)):
        os.makedirs(os.path.dirname(csv_path))
    fields = ['Shot Code']
    csv_file = Path(csv_path)
    # print(csv_file)
    csv_file.touch(exist_ok=True)
    with open(csv_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=fields)
        shot_list = []
        for row in reader:
            # print(row)
            if row['Shot Code'] and row['Shot Code'] != 'Shot Code':
                shot_list.append(row['Shot Code'])

    return shot_list






def assume_shot(item_data):
    source_file = item_data['source_file']
    shots = get_shots(item_data)
    return find_patten(source_file, shots)


def assume_custom_name(item_data):
    source_file = item_data['source_file']
    custom_name = [item_data['custom_name']]
    return find_patten(source_file, custom_name)


def process_executor(project, processor, process, data, ignore_processes=None, app=None):
    from package_maker.process_runner.core import process_runner
    p = process_runner.ProcessRunner(project=project, processor=processor, app=app, process=process, kwargs=data,
                                     ignore_processes=ignore_processes)
    p.runProcesses()
    return True


def make_relative_file(source_path, destination_path):
    target = Path(source_path)
    destination = Path(destination_path)
    target_dir = destination.parent
    target_dir.mkdir(exist_ok=True, parents=True)
    relative_source = os.path.relpath(target, target_dir)
    dir_fd = os.open(str(target_dir.absolute()), os.O_RDONLY)
    try:
        os.symlink(relative_source, destination.name, dir_fd=dir_fd)
    finally:
        os.close(dir_fd)


if __name__ == '__main__':
    source_filepath = r'C:/From_Pixstone/20220705B/082_em_0325/082_em_0325_roto_a_mb_v005/082_em_0325_matte_v005.993#.exr'
    source_filepath_list = ['C:/From_Pixstone/20220705B/082_em_0325/082_em_0325_roto_v005.nk',
                            'C:/From_Pixstone/20220705B/082_em_0325/082_em_0325_roto_v005.sfx',
                            'C:/From_Pixstone/20220705B/082_em_0325/082_em_0325_roto_a_mb_v005/082_em_0325_roto_a_mb_v005.993#.exr',
                            'C:/From_Pixstone/20220705B/082_em_0325/082_em_0325_roto_a_nmb_v005/082_em_0325_roto_a_nmb_v005.993#.exr',
                            'C:/From_Pixstone/20220705B/082_em_0325/082_em_0325_roto_b_mb_v005/082_em_0325_roto_b_mb_v005.993#.exr',
                            'C:/From_Pixstone/20220705B/082_em_0325/082_em_0325_roto_b_nmb_v005/082_em_0325_roto_b_nmb_v005.993#.exr',
                            'C:/From_Pixstone/20220705B/082_em_0325/082_em_0325_roto_b_nmb_v006/foo_cam.fbx',
                            'C:/From_Pixstone/20220705B/foo/foo.mb', 'C:/From_Pixstone/20220705B/foo/foo.nk',
                            'C:/From_Pixstone/20220705B/foo/082_em_0325_roto_a_mb_v006.993#.exr',
                            'C:/From_Pixstone/20220705C/082_em_0320-src-master02/082_em_0320-src-master02_roto_v008.abc',
                            'C:/From_Pixstone/20220705C/082_em_0320-src-master02/082_em_0320-src-master02_roto_v008.sfx',
                            'C:/From_Pixstone/20220705C/082_em_0320-src-master02/082_em_0320-src-master02_roto_mb_v008/082_em_0320-src-master02_roto_mb_v008.993#.exr',
                            'C:/From_Pixstone/20220705C/082_em_0320-src-master02/082_em_0320-src-master02_roto_nmb_v008/082_em_0320-src-master02_roto_nmb_v008.993#.exr',
                            'C:/From_Pixstone/20220705D/080_bb_0375/080_bb_0375_roto_v004.nk',
                            'C:/From_Pixstone/20220705D/080_bb_0375/080_bb_0375_roto_v004.sfx',
                            'C:/From_Pixstone/20220705D/080_bb_0375/080_bb_0375_roto_v004/080_bb_0375_roto_v004.1000#.exr',
                            'C:/From_Pixstone/20220705D/exr_seq/test.0-99@.exr']

    # source_filepath_list = [r'C:/mnt/mpcparis/NOTRE_DAME/IO/From_Rotomaker/20220701_MM/4023_0015-src_master01-aces_v103/4023_0015-src-master01-aces_UDP_v003/4023_0015-src-master01-aces_UDP_v003.991#.jpeg']
    # os.environ['show'] = 'asterix'
    # dept = 'matchmove'
    # for source_filepath in source_filepath_list:
    #     # print(assumed_pkg_type(dept, source_filepath))

    # pkg_dir = r'/mnt/pb6/Filmgate/TRM/io/To_Client/Package'

    # filepaths = [
    #     "trm_ep01-rl03_00131_compositing_v0001_1009-1073#.exr",
    #     "trm_ep01-rl03_00140_compositing_v0001_1009-1129#.exr",
    #     "trm_ep01-rl03_00120_compositing_v0001.1009-1037#.exr",
    #     "trm_ep01-rl03_00130_compositing_v0001.1009-1165#.exr",
    #     "trm_ep01-rl03_00132_compositing_v0001.1009-1150#.exr",
    #     "trm_ep01-rl01_00980_mattepainting_v0003.1001#.exr",
    #     "trm_ep01-rl01_00980_mattepainting_v0003.1001#.exr",
    # ]
    # for file in filepaths:
    #     # print(11111111)
    #     item_data = item_data.copy()
    #     item_data['source_file'] = file
    #     # print(assume_shot(item_data))

    # item_data = {'date': '221015', 'discipline': 'comp', 'files': [{'date': '221015', 'destination_path': '/mnt/pb6/Filmgate/TRM/io/To_Client/Package/PKG-TRM-221015_E/TRM-comp-dasein-package/sequence/trm_ep01-rl02_00530_compositing_v0001.1009-1026#.exr', 'discipline': 'comp', 'ext': 'exr', 'filename': 'trm_ep01-rl02_00530_compositing_v0001.1009-1026#.exr', 'job': 'trm', 'pkg_dir': '/mnt/pb6/Filmgate/TRM/io/To_Client/Package', 'pkg_dir_type': 'for_approval', 'pkg_type': 'shot', 'pkg_version': 'E', 'shot': 'TRM_ep01-rl02_00530', 'shot_version_num': '001', 'shot_version_prefix': 'v', 'show': 'trm', 'source_path': '/mnt/pb6/Filmgate/TRM/io/From_Amolesh/20221014/0530_issue/Output/trm_ep01-rl02_00530_compositing_v0001/trm_ep01-rl02_00530_compositing_v0001.1009-1026#.exr', 'vendor': 'dasein'}, {'date': '221015', 'destination_path': '/mnt/pb6/Filmgate/TRM/io/To_Client/Package/PKG-TRM-221015_E/TRM-comp-dasein-package/sequence/trm_ep01-rl03_00131_compositing_v0001_1009-1073#.exr', 'discipline': 'comp', 'ext': 'exr', 'filename': 'trm_ep01-rl03_00131_compositing_v0001_1009-1073#.exr', 'job': 'trm', 'pkg_dir': '/mnt/pb6/Filmgate/TRM/io/To_Client/Package', 'pkg_dir_type': 'for_approval', 'pkg_type': 'shot', 'pkg_version': 'E', 'shot': 'TRM_ep01-rl03_00131', 'shot_version_num': '001', 'shot_version_prefix': 'v', 'show': 'trm', 'source_path': '/mnt/pb6/Filmgate/TRM/io/From_Amolesh/20221011/11shots/131/OUTPUT/trm_ep01-rl03_00131_compositing_v0001/trm_ep01-rl03_00131_compositing_v0001_1009-1073#.exr', 'vendor': 'dasein'}, {'date': '221015', 'destination_path': '/mnt/pb6/Filmgate/TRM/io/To_Client/Package/PKG-TRM-221015_E/TRM-comp-dasein-package/sequence/trm_ep01-rl03_00140_compositing_v0001_1009-1129#.exr', 'discipline': 'comp', 'ext': 'exr', 'filename': 'trm_ep01-rl03_00140_compositing_v0001_1009-1129#.exr', 'job': 'trm', 'pkg_dir': '/mnt/pb6/Filmgate/TRM/io/To_Client/Package', 'pkg_dir_type': 'for_approval', 'pkg_type': 'shot', 'pkg_version': 'E', 'shot': 'TRM_ep01-rl03_00140', 'shot_version_num': '001', 'shot_version_prefix': 'v', 'show': 'trm', 'source_path': '/mnt/pb6/Filmgate/TRM/io/From_Amolesh/20221011/11shots/140/Output/trm_ep01-rl03_00140_compositing_v0001/trm_ep01-rl03_00140_compositing_v0001_1009-1129#.exr', 'vendor': 'dasein'}, {'date': '221015', 'destination_path': '/mnt/pb6/Filmgate/TRM/io/To_Client/Package/PKG-TRM-221015_E/TRM-comp-dasein-package/sequence/trm_ep01-rl03_00120_compositing_v0001.1009-1037#.exr', 'discipline': 'comp', 'ext': 'exr', 'filename': 'trm_ep01-rl03_00120_compositing_v0001.1009-1037#.exr', 'job': 'trm', 'pkg_dir': '/mnt/pb6/Filmgate/TRM/io/To_Client/Package', 'pkg_dir_type': 'for_approval', 'pkg_type': 'shot', 'pkg_version': 'E', 'shot': 'TRM_ep01-rl03_00120', 'shot_version_num': '001', 'shot_version_prefix': 'v', 'show': 'trm', 'source_path': '/mnt/pb6/Filmgate/TRM/io/From_Amolesh/20221011/11shots/120/Output/trm_ep01-rl03_00120_compositing_v0001/trm_ep01-rl03_00120_compositing_v0001.1009-1037#.exr', 'vendor': 'dasein'}, {'date': '221015', 'destination_path': '/mnt/pb6/Filmgate/TRM/io/To_Client/Package/PKG-TRM-221015_E/TRM-comp-dasein-package/sequence/trm_ep01-rl03_00130_compositing_v0001.1009-1165#.exr', 'discipline': 'comp', 'ext': 'exr', 'filename': 'trm_ep01-rl03_00130_compositing_v0001.1009-1165#.exr', 'job': 'trm', 'pkg_dir': '/mnt/pb6/Filmgate/TRM/io/To_Client/Package', 'pkg_dir_type': 'for_approval', 'pkg_type': 'shot', 'pkg_version': 'E', 'shot': 'TRM_ep01-rl03_00130', 'shot_version_num': '001', 'shot_version_prefix': 'v', 'show': 'trm', 'source_path': '/mnt/pb6/Filmgate/TRM/io/From_Amolesh/20221011/11shots/130/OUTPUT/trm_ep01-rl03_00130_compositing_v0001/trm_ep01-rl03_00130_compositing_v0001.1009-1165#.exr', 'vendor': 'dasein'}, {'date': '221015', 'destination_path': '/mnt/pb6/Filmgate/TRM/io/To_Client/Package/PKG-TRM-221015_E/TRM-comp-dasein-package/sequence/trm_ep01-rl03_00132_compositing_v0001.1009-1150#.exr', 'discipline': 'comp', 'ext': 'exr', 'filename': 'trm_ep01-rl03_00132_compositing_v0001.1009-1150#.exr', 'job': 'trm', 'pkg_dir': '/mnt/pb6/Filmgate/TRM/io/To_Client/Package', 'pkg_dir_type': 'for_approval', 'pkg_type': 'shot', 'pkg_version': 'E', 'shot': 'TRM_ep01-rl03_00132', 'shot_version_num': '001', 'shot_version_prefix': 'v', 'show': 'trm', 'source_path': '/mnt/pb6/Filmgate/TRM/io/From_Amolesh/20221011/11shots/132/Output/trm_ep01-rl03_00132_compositing_v0001/trm_ep01-rl03_00132_compositing_v0001.1009-1150#.exr', 'vendor': 'dasein'}, {'date': '221015', 'destination_path': '/mnt/pb6/Filmgate/TRM/io/To_Client/Package/PKG-TRM-221015_E/TRM-comp-dasein-package/sequence/trm_ep01-rl01_00980_mattepainting_v0003.1001#.exr', 'discipline': 'comp', 'ext': 'exr', 'filename': 'trm_ep01-rl01_00980_mattepainting_v0003.1001#.exr', 'job': 'trm', 'pkg_dir': '/mnt/pb6/Filmgate/TRM/io/To_Client/Package', 'pkg_dir_type': 'for_approval', 'pkg_type': 'shot', 'pkg_version': 'E', 'shot': 'TRM_ep01-rl01_00980', 'shot_version_num': '001', 'shot_version_prefix': 'v', 'show': 'trm', 'source_path': '/mnt/pb6/Filmgate/TRM/io/From_Amolesh/20221013/0090/DMP_precomp/trm_ep01-rl01_00980_mattepainting_v0003.1001#.exr', 'vendor': 'dasein'}, {'date': '221015', 'destination_path': '/mnt/pb6/Filmgate/TRM/io/To_Client/Package/PKG-TRM-221015_E/TRM-comp-dasein-package/sequence/trm_ep01-rl01_00980_mattepainting_v0003.1001#.exr', 'discipline': 'comp', 'ext': 'exr', 'filename': 'trm_ep01-rl01_00980_mattepainting_v0003.1001#.exr', 'job': 'trm', 'pkg_dir': '/mnt/pb6/Filmgate/TRM/io/To_Client/Package', 'pkg_dir_type': 'for_approval', 'pkg_type': 'shot', 'pkg_version': 'E', 'shot': 'TRM_ep01-rl01_00980', 'shot_version_num': '001', 'shot_version_prefix': 'v', 'show': 'trm', 'source_path': '/mnt/pb6/Filmgate/TRM/io/From_Amolesh/20221012/1030/DMP_precomp/trm_ep01-rl01_00980_mattepainting_v0003.1001#.exr', 'vendor': 'dasein'}], 'pkg_dir': '/mnt/pb6/Filmgate/TRM/io/To_Client/Package', 'pkg_type': 'shot', 'pkg_version': 'E', 'show': 'trm', 'vendor': 'dasein'}
    #
    # for file_data in item_data['files']:
    #     update_shot_version(file_data)

    # item_data = {'pkg_dir': '/mnt/mpcparis/NOTRE_DAME/io/To_Client/packages', 'shot': '1039b_0010', 'discipline': 'prep'}

    # item_data = {'pkg_dir': '/mnt/mpcparis/DOGMAN/io/to_client/packages', 'shot': '025_010', 'discipline': 'prep'}
    # # print(get_shots(item_data))
    #
    # import sys
    # sys.path.append(r'/mnt/mpcparis/IO_Stuff/PKG_TOOL/package_maker_testing/shotgun/shotgun-python-api/')
    import shotgun_api3

    # #shotgun_api3.Shotgun.NO_SSL_VALIDATION = True
    # sg = shotgun_api3.Shotgun("https://dasein.shotgunstudio.com",
    #                           login="data@daseinvfx.com",
    #                           password="whenDolphin@9752")
    #
    # projList = sg.find('Project', [], ['name'])
    #
    # for i in projList:
    #     # print('id:' + str(i['id']) + ' ' + i['name'])

    data = {'pkg_dir': '/mnt/sitw/io/to-sitw', 'shot': '', 'discipline': ''}
    get_shots(data)