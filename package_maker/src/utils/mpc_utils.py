import re
from datetime import datetime, timedelta

from package_maker.src.config.config_main import *
from package_maker.src.config.config_vendor import  *



def global_pkg_data(job, destination, pkg_dir, pkg_for, vendor_name):

    if pkg_for == 'client':
        GLOBAL_DATA = get_global_data()
    elif pkg_for == 'vendor':
        GLOBAL_DATA = vendor_config_data(vendor='dasein')
    else:
        return {}

    return dict(
        date=datetime.today().strftime('%Y%m%d'),
        vendor=GLOBAL_DATA['destination'][destination]['vendor'],
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
    version_prefix = GLOBAl_DATA['destination'].get(os.environ.get('destination'), {}).get(
        'pkg_version_prefix', global_pkg_version_prefix)
    version_num = GLOBAl_DATA['destination'].get(os.environ.get('destination'), {}).get(
        'pkg_version_padding', global_pkg_version_padding)
    latest_version = get_existing_versions()[-1]
    up_version = re.sub(r'[0-9]+$',
                  lambda x: str(int(x.group()) + 1).zfill(len(x.group())),
                  latest_version)
    return re.split(version_prefix, up_version)[-1]
