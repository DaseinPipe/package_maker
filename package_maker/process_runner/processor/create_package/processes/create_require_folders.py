from package_maker.src.config.config_client import get_path
import os
__name = 'create require folders'

def run(**data):
    job = data.get('show')
    required_folders = ['camera', 'element', 'for_approval', 'geometry', 'note', 'workfile']
    shot_pkg_dir = get_path(job, 'shot_pkg_dir').format(data)

    for require_folder in required_folders:
        require_folder_path = os.path.join(shot_pkg_dir, require_folder)
        if os.path.exists(require_folder_path):
            continue
        os.makedirs(require_folder_path)

    return 0, {
        'info': '', 
        'return_data': {}
    }
if __name__ == '__main__':
    data = {'shot': '080_020', 'discipline': 'prep', 'plate_version_num': '01', 'shot_version_num': '0002', 'plate_version_prefix': 'master', 'shot_version_prefix': 'v', 'files': [{'source_path': '/mnt/mpcparis/DOGMAN/io/from_rotomaker/20221117/080_220-src-master01-v001-linear_paint_v001/080_220-src-master01-v001-linear.993-1043#.exr', 'pkg_dir_type': 'element', 'custom_name': '', 'ext': 'exr', 'pkg_type': 'shot', 'job': 'dogman', 'shot': '080_020', 'discipline': 'prep', 'plate_version_num': '01', 'shot_version_num': '0002', 'plate_version_prefix': 'master', 'shot_version_prefix': 'v', 'date': '20221121', 'vendor': 'dasein', 'show': 'dogman', 'pkg_version_prefix': 'v', 'pkg_version_num': '0004', 'pkg_dir': '/mnt/mpcparis/DOGMAN/io/to_client/packages/', 'destination_path': '/mnt/mpcparis/DOGMAN/io/to_client/packages//PKG-20221121-dasein-dogman-v0004-package/20221121-dasein-dogman-v0004/shot-080_020-prep-master01-dasein-v0002/element/080_020-prep-master01-aces_prep_v0002/080_020-prep-master01-aces_prep_v0002.993-1043@.exr'}], 'date': '20221121', 'vendor': 'dasein', 'show': 'dogman', 'pkg_version_prefix': 'v', 'pkg_version_num': '0004', 'pkg_dir': '/mnt/mpcparis/DOGMAN/io/to_client/packages/', 'pkg_type': 'shot'}
    run(**data)




