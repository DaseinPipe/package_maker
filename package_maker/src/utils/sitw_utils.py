import re, csv, shutil
from datetime import datetime, timedelta
from pathlib import Path, PurePath
from tempfile import NamedTemporaryFile
from package_maker.src.config.config_client import *
from package_maker.src.config.config_vendor import *
from package_maker.src.utils.general_utils import fix_nulls


def global_pkg_data(job, destination, pkg_dir, pkg_for, vendor_name):
    if pkg_for == 'client':
        GLOBAL_DATA = get_global_data()
    elif pkg_for == 'vendor':
        GLOBAL_DATA = vendor_config_data(vendor='dasein')
    else:
        return {
            'show': job,
            'pkg_dir': pkg_dir,
        }

    return dict(
        date=datetime.today().strftime('%Y_%m_%d'),
        vendor=GLOBAL_DATA['destination'][destination]['vendor'],
        root_dir=GLOBAL_DATA['destination'][destination]['job'][job]['root_path'],
        show=job,
        pkg_version_prefix=GLOBAL_DATA['destination'][destination]['pkg_version_prefix'],
        pkg_version_num=get_latest_pkg_version(pkg_dir),
        pkg_dir=pkg_dir,
        pkg_for=pkg_for,
        vendor_name=vendor_name
    )


def get_latest_pkg_version(pkg_dir):
    def get_existing_versions():
        first_version = '{version_prefix}{version_num}'.format(
            version_prefix=version_prefix,
            version_num='0'.zfill(version_num)
        )
        date_fld = os.path.join(pkg_dir, datetime.today().strftime('%Y_%m_%d'))
        if not os.path.exists(date_fld):
            os.makedirs(date_fld)
        pkg_names = sorted(os.listdir(date_fld))
        # print(pkg_names)
        if not pkg_names:
            return [first_version]
        version_list = []
        for pkg_name in pkg_names:
            version_expression = f'{version_prefix}\d' + '{' + str(version_num) + '}'
            # print(version_expression)
            pkg_version = next(iter(re.findall(version_expression, pkg_name)), None)
            if pkg_version:
                version_list.append(pkg_version)
        return sorted(version_list) or [first_version]

    GLOBAl_DATA = get_global_data()
    version_prefix = GLOBAl_DATA['destination'].get(os.environ.get('destination'), {}).get(
        'pkg_version_prefix', '-')
    version_num = GLOBAl_DATA['destination'].get(os.environ.get('destination'), {}).get(
        'pkg_version_padding', 2)
    latest_version = get_existing_versions()[-1]
    # print(latest_version)
    up_version = re.sub(r'[0-9]+$',
                        lambda x: str(int(x.group()) + 1).zfill(len(x.group())),
                        latest_version)
    return re.split(version_prefix, up_version)[-1]


def update_shot_version(item_data):
    dept = item_data['discipline']
    pkg_dir = Path(item_data['files'][0]['pkg_dir'])
    job_dir = pkg_dir.parents[1]
    shots = list(set([file_data['shot'] for file_data in item_data['files']]))
    csv_path = PurePath(job_dir, ".package", 'to_client.csv')
    default_client_version = 1
    fields = ['shot', 'client_version']
    csv_file = Path(csv_path)
    csv_file.touch(exist_ok=True)

    tempfile = NamedTemporaryFile(mode='w', delete=False)

    with open(csv_file, 'r') as csvfile, tempfile:
        reader = csv.DictReader(csvfile, fieldnames=fields)
        writer = csv.DictWriter(tempfile, fieldnames=fields)
        writer.writeheader()
        for shot in shots:
            row_update = False
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
    default_client_version = 1
    source_path = item_data.get('source_path', 'temp')
    match_obj = re.search(r'(?i)v\d+', source_path, re.IGNORECASE)
    if not match_obj:
        return default_client_version
    version_text = match_obj.group()
    return int(version_text[1:])


def check_shot_version(item_data):
    csv_shot_version = get_latest_shot_version_from_csv(item_data)
    filename_shot_version = get_latest_shot_version(item_data)
    if csv_shot_version > filename_shot_version:
        return False
    return True


def get_latest_shot_version_from_csv(item_data):
    print(item_data)
    pkg_dir = Path(item_data['pkg_dir'])
    dept = item_data['discipline']
    job_dir = pkg_dir.parents[1]
    csv_path = PurePath(job_dir, ".package", 'to_client.csv')
    shot = item_data['shot']

    default_client_version = 0
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


t = {'pkg_dir': '/mnt/sitw/io/to-sitw/', 'shot': '044sin_0010', 'discipline': 'paint',
     'source_path': '/mnt/sitw/movs/shots/scansORIG/044SIN_0010_BG01_V01.mov'}

p = '/mnt/sitw/io/to-sitw'

print(check_shot_version(t))
