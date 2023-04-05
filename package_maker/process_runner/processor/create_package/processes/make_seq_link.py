import os
import fileseq
from package_maker.src.config.config_client import *
from package_maker.src.utils.general_utils import make_relative_file
__name = 'make seq symbolic link'

def run(**data):
    for file_data in data['files']:
        source_path = file_data['source_path']
        ext = os.path.splitext(source_path)[-1][1:]
        if ext not in global_seq_ext:
            continue

        destination_path = file_data['destination_path']
        source_seq = fileseq.FileSequence(source_path)
        destination_seq = fileseq.FileSequence(destination_path)
        destination_seq.setPadding(source_seq.padding())
        for frame in range(source_seq.start(), source_seq.end()+1):
            source_framepath = source_seq.frame(frame)
            destination_framepath = destination_seq.frame(frame)
            if not os.path.exists(os.path.dirname(destination_framepath)):
                os.makedirs(os.path.dirname(destination_framepath))
            make_relative_file(source_framepath, destination_framepath)


    return 0, {
        'info': '', 
        'return_data': {}
    }


if __name__ == '__main__':
    data = {'shot': '080_020', 'discipline': 'prep', 'plate_version_num': '01', 'shot_version_num': '0002', 'plate_version_prefix': 'master', 'shot_version_prefix': 'v', 'files': [{'source_path': '/mnt/mpcparis/DOGMAN/io/from_rotomaker/20221117/080_220-src-master01-v001-linear_paint_v001/080_220-src-master01-v001-linear.993-1043#.exr', 'pkg_dir_type': 'element', 'custom_name': '', 'ext': 'exr', 'pkg_type': 'shot', 'job': 'dogman', 'shot': '080_020', 'discipline': 'prep', 'plate_version_num': '01', 'shot_version_num': '0002', 'plate_version_prefix': 'master', 'shot_version_prefix': 'v', 'date': '20221121', 'vendor': 'dasein', 'show': 'dogman', 'pkg_version_prefix': 'v', 'pkg_version_num': '0004', 'pkg_dir': '/mnt/mpcparis/DOGMAN/io/to_client/packages/', 'destination_path': '/mnt/mpcparis/DOGMAN/io/to_client/packages//PKG-20221121-dasein-dogman-v0004-package/20221121-dasein-dogman-v0004/shot-080_020-prep-master01-dasein-v0002/element/080_020-prep-master01-aces_prep_v0002/080_020-prep-master01-aces_prep_v0002.993-1043@.exr'}], 'date': '20221121', 'vendor': 'dasein', 'show': 'dogman', 'pkg_version_prefix': 'v', 'pkg_version_num': '0004', 'pkg_dir': '/mnt/mpcparis/DOGMAN/io/to_client/packages/', 'pkg_type': 'shot'}

    run(**data)


