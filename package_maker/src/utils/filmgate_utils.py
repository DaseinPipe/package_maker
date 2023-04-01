import re
from datetime import datetime, timedelta

from package_maker.src.config.config_main import *
from package_maker.src.config.config_vendor import *



def global_pkg_data(job, destination, pkg_dir, pkg_for, vendor_name):

    if pkg_for == 'client':
        GLOBAL_DATA = get_global_data()
    elif pkg_for == 'vendor':
        GLOBAL_DATA = vendor_config_data(vendor='dasein')
    else:
        return {}

    return dict(
        date=datetime.today().strftime('%Y%m%d')[2:],
        vendor= GLOBAL_DATA['destination'][destination]['vendor'],
        show=job,
        pkg_version=get_latest_pkg_version(pkg_dir),
        pkg_dir=pkg_dir,
        pkg_for=pkg_for,
        vendor_name=vendor_name,
    )


def get_latest_pkg_version(pkg_dir):

    def get_existing_versions():

        if not os.path.exists(pkg_dir):
            os.makedirs(pkg_dir)
        pkg_names = sorted(os.listdir(pkg_dir))
        if not pkg_names:
            return first_version
        today = datetime.today().strftime('%Y%m%d')[2:]
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


if __name__ == '__main__':
    pkg_dir = r'/mnt/pb6/Filmgate/TRM/io/To_Client/Package'
    print(get_latest_pkg_version(pkg_dir))