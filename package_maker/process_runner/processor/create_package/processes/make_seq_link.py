import os
import fileseq
from package_maker.src.config.config_main import *
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
        for frame in range(source_seq.start(), source_seq.end()+1):
            source_framepath = source_seq.frame(frame)
            destination_framepath = destination_seq.frame(frame)
            if not os.path.exists(os.path.dirname(destination_framepath)):
                os.makedirs(os.path.dirname(destination_framepath))
            os.symlink(source_framepath, destination_framepath)

    return 0, {
        'info': '', 
        'return_data': {}
    }


if __name__ == '__main__':
    data = {'date': '221015', 'discipline': 'comp', 'files': [{'date': '221015', 'destination_path': '/mnt/pb6/Filmgate/TRM/io/To_Client/Package/PKG-TRM-221015_B/trm_TRM_ep01-rl02_00530_compositing_v001/sequence/trm_ep01-rl02_00530_compositing_v0001.1009-1026#.exr', 'discipline': 'comp', 'ext': 'exr', 'filename': 'trm_ep01-rl02_00530_compositing_v0001.1009-1026#.exr', 'job': 'trm', 'pkg_dir': '/mnt/pb6/Filmgate/TRM/io/To_Client/Package', 'pkg_dir_type': 'for_approval', 'pkg_type': 'shot', 'pkg_version': 'B', 'shot': 'TRM_ep01-rl02_00530', 'shot_version_num': '001', 'shot_version_prefix': 'v', 'show': 'trm', 'source_path': '/mnt/pb6/Filmgate/TRM/io/From_Amolesh/20221014/0530_issue/Output/trm_ep01-rl02_00530_compositing_v0001/trm_ep01-rl02_00530_compositing_v0001.1009-1026#.exr', 'vendor': 'dasein'}, {'date': '221015', 'destination_path': '/mnt/pb6/Filmgate/TRM/io/To_Client/Package/PKG-TRM-221015_B/trm_TRM_ep01-rl03_00131_compositing_v001/sequence/trm_ep01-rl03_00131_compositing_v0001_1009-1073#.exr', 'discipline': 'comp', 'ext': 'exr', 'filename': 'trm_ep01-rl03_00131_compositing_v0001_1009-1073#.exr', 'job': 'trm', 'pkg_dir': '/mnt/pb6/Filmgate/TRM/io/To_Client/Package', 'pkg_dir_type': 'for_approval', 'pkg_type': 'shot', 'pkg_version': 'B', 'shot': 'TRM_ep01-rl03_00131', 'shot_version_num': '001', 'shot_version_prefix': 'v', 'show': 'trm', 'source_path': '/mnt/pb6/Filmgate/TRM/io/From_Amolesh/20221011/11shots/131/OUTPUT/trm_ep01-rl03_00131_compositing_v0001/trm_ep01-rl03_00131_compositing_v0001_1009-1073#.exr', 'vendor': 'dasein'}, {'date': '221015', 'destination_path': '/mnt/pb6/Filmgate/TRM/io/To_Client/Package/PKG-TRM-221015_B/trm_TRM_ep01-rl03_00140_compositing_v001/sequence/trm_ep01-rl03_00140_compositing_v0001_1009-1129#.exr', 'discipline': 'comp', 'ext': 'exr', 'filename': 'trm_ep01-rl03_00140_compositing_v0001_1009-1129#.exr', 'job': 'trm', 'pkg_dir': '/mnt/pb6/Filmgate/TRM/io/To_Client/Package', 'pkg_dir_type': 'for_approval', 'pkg_type': 'shot', 'pkg_version': 'B', 'shot': 'TRM_ep01-rl03_00140', 'shot_version_num': '001', 'shot_version_prefix': 'v', 'show': 'trm', 'source_path': '/mnt/pb6/Filmgate/TRM/io/From_Amolesh/20221011/11shots/140/Output/trm_ep01-rl03_00140_compositing_v0001/trm_ep01-rl03_00140_compositing_v0001_1009-1129#.exr', 'vendor': 'dasein'}, {'date': '221015', 'destination_path': '/mnt/pb6/Filmgate/TRM/io/To_Client/Package/PKG-TRM-221015_B/trm_TRM_ep01-rl03_00120_compositing_v001/sequence/trm_ep01-rl03_00120_compositing_v0001.1009-1037#.exr', 'discipline': 'comp', 'ext': 'exr', 'filename': 'trm_ep01-rl03_00120_compositing_v0001.1009-1037#.exr', 'job': 'trm', 'pkg_dir': '/mnt/pb6/Filmgate/TRM/io/To_Client/Package', 'pkg_dir_type': 'for_approval', 'pkg_type': 'shot', 'pkg_version': 'B', 'shot': 'TRM_ep01-rl03_00120', 'shot_version_num': '001', 'shot_version_prefix': 'v', 'show': 'trm', 'source_path': '/mnt/pb6/Filmgate/TRM/io/From_Amolesh/20221011/11shots/120/Output/trm_ep01-rl03_00120_compositing_v0001/trm_ep01-rl03_00120_compositing_v0001.1009-1037#.exr', 'vendor': 'dasein'}, {'date': '221015', 'destination_path': '/mnt/pb6/Filmgate/TRM/io/To_Client/Package/PKG-TRM-221015_B/trm_TRM_ep01-rl03_00130_compositing_v001/sequence/trm_ep01-rl03_00130_compositing_v0001.1009-1165#.exr', 'discipline': 'comp', 'ext': 'exr', 'filename': 'trm_ep01-rl03_00130_compositing_v0001.1009-1165#.exr', 'job': 'trm', 'pkg_dir': '/mnt/pb6/Filmgate/TRM/io/To_Client/Package', 'pkg_dir_type': 'for_approval', 'pkg_type': 'shot', 'pkg_version': 'B', 'shot': 'TRM_ep01-rl03_00130', 'shot_version_num': '001', 'shot_version_prefix': 'v', 'show': 'trm', 'source_path': '/mnt/pb6/Filmgate/TRM/io/From_Amolesh/20221011/11shots/130/OUTPUT/trm_ep01-rl03_00130_compositing_v0001/trm_ep01-rl03_00130_compositing_v0001.1009-1165#.exr', 'vendor': 'dasein'}, {'date': '221015', 'destination_path': '/mnt/pb6/Filmgate/TRM/io/To_Client/Package/PKG-TRM-221015_B/trm_TRM_ep01-rl03_00132_compositing_v001/sequence/trm_ep01-rl03_00132_compositing_v0001.1009-1150#.exr', 'discipline': 'comp', 'ext': 'exr', 'filename': 'trm_ep01-rl03_00132_compositing_v0001.1009-1150#.exr', 'job': 'trm', 'pkg_dir': '/mnt/pb6/Filmgate/TRM/io/To_Client/Package', 'pkg_dir_type': 'for_approval', 'pkg_type': 'shot', 'pkg_version': 'B', 'shot': 'TRM_ep01-rl03_00132', 'shot_version_num': '001', 'shot_version_prefix': 'v', 'show': 'trm', 'source_path': '/mnt/pb6/Filmgate/TRM/io/From_Amolesh/20221011/11shots/132/Output/trm_ep01-rl03_00132_compositing_v0001/trm_ep01-rl03_00132_compositing_v0001.1009-1150#.exr', 'vendor': 'dasein'}, {'date': '221015', 'destination_path': '/mnt/pb6/Filmgate/TRM/io/To_Client/Package/PKG-TRM-221015_B/trm_TRM_ep01-rl01_00980_compositing_v001/sequence/trm_ep01-rl01_00980_mattepainting_v0003.1001#.exr', 'discipline': 'comp', 'ext': 'exr', 'filename': 'trm_ep01-rl01_00980_mattepainting_v0003.1001#.exr', 'job': 'trm', 'pkg_dir': '/mnt/pb6/Filmgate/TRM/io/To_Client/Package', 'pkg_dir_type': 'for_approval', 'pkg_type': 'shot', 'pkg_version': 'B', 'shot': 'TRM_ep01-rl01_00980', 'shot_version_num': '001', 'shot_version_prefix': 'v', 'show': 'trm', 'source_path': '/mnt/pb6/Filmgate/TRM/io/From_Amolesh/20221013/0090/DMP_precomp/trm_ep01-rl01_00980_mattepainting_v0003.1001#.exr', 'vendor': 'dasein'}, {'date': '221015', 'destination_path': '/mnt/pb6/Filmgate/TRM/io/To_Client/Package/PKG-TRM-221015_B/trm_TRM_ep01-rl01_00980_compositing_v001/sequence/trm_ep01-rl01_00980_mattepainting_v0003.1001#.exr', 'discipline': 'comp', 'ext': 'exr', 'filename': 'trm_ep01-rl01_00980_mattepainting_v0003.1001#.exr', 'job': 'trm', 'pkg_dir': '/mnt/pb6/Filmgate/TRM/io/To_Client/Package', 'pkg_dir_type': 'for_approval', 'pkg_type': 'shot', 'pkg_version': 'B', 'shot': 'TRM_ep01-rl01_00980', 'shot_version_num': '001', 'shot_version_prefix': 'v', 'show': 'trm', 'source_path': '/mnt/pb6/Filmgate/TRM/io/From_Amolesh/20221012/1030/DMP_precomp/trm_ep01-rl01_00980_mattepainting_v0003.1001#.exr', 'vendor': 'dasein'}], 'pkg_dir': '/mnt/pb6/Filmgate/TRM/io/To_Client/Package', 'pkg_type': 'shot', 'pkg_version': 'B', 'show': 'trm', 'vendor': 'dasein'}
    run(**data)


