from package_maker.src.utils.general_utils import make_relative_file
from package_maker.src.config.config_client import *
import pathlib, os
__name = 'make seq symbolic link'

def run(**data):
    # print(data)
    source_dir_path = pathlib.Path(data['files'][0]['source_path']).parents[2]
    for file_data in data['files']:
        source_path = pathlib.Path(file_data['source_path'])
        destination_path = file_data['destination_path']
        shot = '_'.join(source_path.name.split('_')[:2])
        destination_path = destination_path.replace('shot', shot)
        if not os.path.exists(os.path.dirname(destination_path)):
            os.makedirs(os.path.dirname(destination_path))
        make_relative_file(str(source_path), destination_path)
        cc_source_path = get_cc_path(source_dir_path, shot)
        if cc_source_path:
            destination_dir_path = pathlib.Path(destination_path).parent
            cc_destination_path = pathlib.Path(destination_dir_path, cc_source_path.name)
            if not os.path.exists(str(cc_destination_path)):
                make_relative_file(str(cc_source_path), str(cc_destination_path))


    return 0, {
        'info': '', 
        'return_data': {}
    }


def get_cc_path(root_path, shot):
    for root, dirs, files in os.walk(root_path):
        for file in files:
            if file.endswith('.cc'):
                if shot in file:
                    return pathlib.Path(root, file)




if __name__ == '__main__':
    data = {'shot': '', 'files': [{'source_path': '/mnt/sitw/io/from_client/20230420/20230418_sitw_vfx_pull_TO_009_01/01_plates/001AIR_0030_BG01_V01', 'destination_path': '/mnt/sitw/scans/shot/001AIR_0030_BG01_V01'}], 'discipline': 'scans', 'show': 'sitw', 'pkg_dir': '/mnt/sitw'}
    run(**data)




