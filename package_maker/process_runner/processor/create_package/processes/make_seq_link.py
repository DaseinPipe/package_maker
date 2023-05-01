import os
import fileseq
from package_maker.src.config.config_client import *
from package_maker.src.utils.general_utils import make_relative_file
__name = 'make seq symbolic link'

def run(**data):
    print(data)
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
            print(source_framepath, destination_framepath)
            make_relative_file(source_framepath, destination_framepath)


    return 0, {
        'info': '', 
        'return_data': {}
    }


if __name__ == '__main__':
    data = {'source_path': '/mnt/pb6/Primary/PED/io/from_client/20230407/EXRs/05_0340_V01/05_0340_V01.394007-394060##.exr', 'pkg_dir_type': 'element', 'custom_name': '', 'ext': 'exr', 'filename': '05_0340_V01.394007-394060##.exr', 'pkg_type': 'shot', 'job': 'ped', 'shot': 'test', 'discipline': 'prep', 'plate_version_num': '01', 'shot_version_num': '0001', 'plate_version_prefix': 'master', 'shot_version_prefix': 'v', 'date': '20230407', 'vendor': 'dasein', 'show': 'ped', 'pkg_version_prefix': 'v', 'pkg_version_num': '0001', 'pkg_dir': '/mnt/pb6/Primary/PED/io/to_client/packages', 'pkg_for': 'client', 'vendor_name': 'UNKNOWN', 'destination_path': '/mnt/pb6/Primary/PED/io/to_client/packages/PKG-20230407-dasein-ped-v0001-package/20230407-dasein-ped-v0001/shot-test-prep-master01-dasein-v0001/element/test-prep-master01-aces_UNKNOWN_v0001/test-src-master01-aces_UNKNOWN_v0001.394007-394060@.exr'}
    run(**data)


