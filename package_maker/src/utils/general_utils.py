from package_maker.src.core.for_approval import *
from package_maker.src.utils import dbHelper

def is_name_matched(text, patterns):
    for pattern in patterns:
        result = re.search(pattern, text)
        if result:
            return True
    return False


def is_ext_matched(filepath, ext_list):
    _ext = os.path.splitext(filepath)[-1]
    if _ext in ext_list:
        return True
    return False


def find_patten(text, patterns):
    result_list = []
    for pattern in patterns:
        result = re.search(pattern, text)
        if result:
            return result.group(0)
    return None

def list_duplicates(seq):
    seen = set()
    seen_add = seen.add
    seen_twice = set( x for x in seq if x in seen or seen_add(x) )
    return list( seen_twice )


def transferFile(scrFile, destFile, moveFlag=False):
    if not os.path.exists(os.path.dirname(destFile)):
        os.makedirs(os.path.dirname(destFile))

    if moveFlag:
        shutil.move(scrFile, destFile)
        return
    shutil.copyfile(scrFile, destFile)

    print('Transfer complete...')


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
        if not pkg_dir_type_data: # to ignore custom and select
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


def get_latest_pkg_version(pkg_dir):


    def get_existing_versions():
        first_version = '{version_prefix}{version_num}'.format(
            version_prefix=version_prefix,
            version_num='0'.zfill(version_num)
        )
        if not os.path.exists(pkg_dir):
            os.makedirs(pkg_dir)
        pkg_names = sorted(os.listdir(pkg_dir))
        if not pkg_names:
            return [first_version]
        version_list = []
        for pkg_name in pkg_names:
            version_expression = f'{version_prefix}\d' + '{' + str(version_num) + '}'
            pkg_version = next(iter(re.findall(version_expression, pkg_name)), None)
            if pkg_version:
                version_list.append(pkg_version)
        return sorted(version_list) or [first_version]

    GLOBAl_DATA = get_global_data()
    version_prefix = GLOBAl_DATA['job'].get(os.environ.get('show'), {}).get(
        'pkg_version_prefix', global_pkg_version_prefix)
    version_num = GLOBAl_DATA['job'].get(os.environ.get('show'), {}).get(
        'pkg_version_padding', global_pkg_version_padding)

    latest_version = get_existing_versions()[-1]
    up_version =re.sub(r'[0-9]+$',
                  lambda x: str(int(x.group()) + 1).zfill(len(x.group())),
                  latest_version)
    return re.split(version_prefix, up_version)[-1]

def update_shot_version(item_data):
    pkg_dir = item_data['pkg_dir']
    dept = item_data['discipline']
    shot = item_data['shot']
    db_path = os.path.join(pkg_dir, ".package/asterix.db").replace('\\', '/')
    with dbHelper.ConnectDB(db_path) as con:
        con.execute(f"SELECT client_version FROM {dept} WHERE shot = '{shot}'")
        current_version = con.fetchone()
    default_version = 1
    if current_version:
        latest_version = current_version[0] + 1
    else:
        latest_version = default_version + 1

    with dbHelper.ConnectDB(db_path) as con:
        con.execute(f"SELECT client_version FROM {dept} where shot = '{shot}'")
        if con.fetchone():
            msg = f"UPDATE {dept} set client_version = '{latest_version}' where shot = '{shot}'"
        else:
            msg = f"INSERT INTO {dept} (shot, client_version) VALUES ('{shot}', '{latest_version}')"
        con.execute(msg)

def get_latest_shot_version(item_data):
    pkg_dir = item_data['pkg_dir']
    dept = item_data['discipline']
    shot = item_data['shot']
    db_path = os.path.join(pkg_dir, ".package/asterix.db").replace('\\', '/')

    with dbHelper.ConnectDB(db_path) as con:
        msg = f'CREATE TABLE IF NOT EXISTS "{dept}" ("shot" TEXT UNIQUE, "client_version" INTEGER)'
        con.execute(msg)

    with dbHelper.ConnectDB(db_path) as con:
        con.execute(f"SELECT client_version FROM {dept} WHERE shot = '{shot}'")
        current_version = con.fetchone()
    if current_version:
        return current_version[0]
    else:
        return 1

def get_custom_element_descs(item_data):
    pkg_dir = item_data['pkg_dir']
    dept = item_data['discipline']
    shot = item_data['shot']
    db_path = os.path.join(pkg_dir, ".package/asterix.db").replace('\\', '/')
    with dbHelper.ConnectDB(db_path) as con:
        con.execute(f"SELECT {dept}_element_descs FROM main_db WHERE shot = '{shot}'")
        custom_element_descs = con.fetchone()
    if custom_element_descs:
        if not custom_element_descs[0]:
            return
        return [each.strip() for each in custom_element_descs[0].split(',')]
    return []

def get_shots(item_data):
    pkg_dir = item_data['pkg_dir']
    db_path = os.path.join(pkg_dir, ".package/asterix.db").replace('\\', '/')

    with dbHelper.ConnectDB(db_path) as con:
        msg = 'CREATE TABLE IF NOT EXISTS "main_db" ("id" INTEGER, "shot" TEXT UNIQUE, "roto_element_descs" TEXT, ' \
              '"prep_element_descs" TEXT, "comp_element_descs"	TEXT, "matchmove_element_descs" TEXT, ' \
              'PRIMARY KEY("id" AUTOINCREMENT))'
        con.execute(msg)


    with dbHelper.ConnectDB(db_path) as con:
        con.execute("SELECT shot FROM main_db")
        shot_list = con.fetchall()
    return [each[0] for each in shot_list]

def db_check(db_path):
    if not os.path.exists(db_path):
        pass



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
    #     print(assumed_pkg_type(dept, source_filepath))
    
    # item_data = {'date': '20221008', 'discipline': 'roto', 'files': [], 'pkg_dir': 'C:/mnt/mpcparis/A5/io/To_Client/packages', 'pkg_type': 'shot', 'pkg_version_num': '0046', 'pkg_version_prefix': 'v', 'plate_version_num': '01', 'plate_version_prefix': 'master', 'shot': '080_bb_0375', 'shot_version_num': '001', 'shot_version_prefix': 'v', 'show': 'asterix', 'vendor': 'dasein'}
    # print(get_shots(item_data))

    import random


    print(random.choice(range(256)))


