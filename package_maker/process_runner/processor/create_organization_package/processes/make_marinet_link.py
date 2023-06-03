import os
from ctypes import Union
from datetime import datetime
from package_maker.src.config.config_client import get_show_data, get_path
from package_maker.src.utils.general_utils import find_patten as _find_patten
import re
import logging

__name = 'create vendor package'

# logger = logging.getLogger('create_organization_package')
# logger.info('------------------------------ make_link ---------------------------------------')
#

from pathlib import Path

import os
import fileseq





source_dir = '/mnt/mpcparis/MARINET/io/from_client/PKG - 20221118-mpc-marinet-v0062/20221118-mpc-marinet-v0062/'
# source_file_data = {
#     "189_040": "shot-189_040-roto-master01-mpc-v001/element/189_040-src-master01-v001-aces/189_040-src-master01-v001-aces.1001-1043#.exr",
#     "189_020": "shot-189_020-roto-master01-mpc-v001/element/189_020-src-master01-v001-aces/189_020-src-master01-v001-aces.1001-1068#.exr",
#     "247_020": "shot-247_020-roto-master01-mpc-v001/element/247_020-src-master01-v001-aces/247_020-src-master01-v001-aces.1001-1090#.exr",
#     "196_010": "shot-196_010-roto-master01-mpc-v001/element/196_010-src-master01-v001-aces/196_010-src-master01-v001-aces.1001-1174#.exr",
#     "247_010": "shot-247_010-roto-master01-mpc-v001/element/247_010-src-master01-v001-aces/247_010-src-master01-v001-aces.1001-1116#.exr",
#     "247_050": "shot-247_050-roto-master01-mpc-v001/element/247_050-src-master01-v001-aces/247_050-src-master01-v001-aces.1001-1165#.exr",
#     "247_080": "shot-247_080-roto-master01-mpc-v001/element/247_080-src-master01-v001-aces/247_080-src-master01-v001-aces.1001-1122#.exr",
#     "247_070": "shot-247_070-roto-master01-mpc-v001/element/247_070-src-master01-v001-aces/247_070-src-master01-v001-aces.1001-1128#.exr",
#     "249_046": "shot-249_046-roto-master01-mpc-v001/element/249_046-src-master01-v001-aces/249_046-src-master01-v001-aces.1001-1070#.exr",
#     "249_044": "shot-249_044-roto-master01-mpc-v001/element/249_044-src-master01-v001-aces/249_044-src-master01-v001-aces.1001-1093#.exr",
#     "249_010": "shot-249_010-roto-master01-mpc-v001/element/249_010-src-master01-v001-aces/249_010-src-master01-v001-aces.1001-1421#.exr",
#     "249_040": "shot-249_040-roto-master01-mpc-v001/element/249_040-src-master01-v001-aces/249_040-src-master01-v001-aces.1081-2245#.exr",
# }

source_file_data = {
    "189_020" : "shot-189_020-roto-master01-mpc-v001/element/189_020-roto-base-nk-MASTER_REF_ROTO-v002-aces/189_020-roto-base-nk-MASTER_REF_ROTO-v002-aces.1001-1068#.exr",
    "189_040" : "shot-189_040-roto-master01-mpc-v001/element/189_040-roto-base-nk-MASTER_REF_ROTO-v003-aces/189_040-roto-base-nk-MASTER_REF_ROTO-v003-aces.1001-1043#.exr",
    "247_020" : "shot-247_020-roto-master01-mpc-v001/element/247_020-roto-base-nk-MASTER_REF_ROTO-v002-aces/247_020-roto-base-nk-MASTER_REF_ROTO-v002-aces.1001-1090#.exr",
    "247_010" : "shot-247_010-roto-master01-mpc-v001/element/247_010-roto-base-nk-MASTER_REF_ROTO-v005-aces/247_010-roto-base-nk-MASTER_REF_ROTO-v005-aces.1001-1116#.exr",
    "196_010" : "shot-196_010-roto-master01-mpc-v001/element/196_010-roto-base-nk-MASTER_REF_ROTO-v002-aces/196_010-roto-base-nk-MASTER_REF_ROTO-v002-aces.1001-1174#.exr",
    "247_070" : "shot-247_070-roto-master01-mpc-v001/element/247_070-roto-base-nk-MASTER_REF_ROTO-v002-aces/247_070-roto-base-nk-MASTER_REF_ROTO-v002-aces.1001-1128#.exr",
    "247_050" : "shot-247_050-roto-master01-mpc-v001/element/247_050-roto-base-nk-MASTER_REF_ROTO-v004-aces/247_050-roto-base-nk-MASTER_REF_ROTO-v004-aces.1001-1165#.exr",
    "247_080" : "shot-247_080-roto-master01-mpc-v001/element/247_080-roto-base-nk-MASTER_REF_ROTO-v002-aces/247_080-roto-base-nk-MASTER_REF_ROTO-v002-aces.1001-1122#.exr",
    "249_044" : "shot-249_044-roto-master01-mpc-v001/element/249_044-roto-base-nk-MASTER_REF_ROTO-v002-aces/249_044-roto-base-nk-MASTER_REF_ROTO-v002-aces.1001-1093#.exr",
    "249_046" : "shot-249_046-roto-master01-mpc-v001/element/249_046-roto-base-nk-MASTER_REF_ROTO-v007-aces/249_046-roto-base-nk-MASTER_REF_ROTO-v007-aces.1001-1070#.exr",
}



fromfolder = '/mnt/mpcparis/MARINET/'
tofolder = '/mnt/mpcparis/MARINET/reference/'


for shot_name, source_path in source_file_data.items():
    source_seq_file = source_path.split('/')[-1]
    source_seq = fileseq.FileSequence(source_path)
    destination_path = os.path.join(tofolder, f'{shot_name}/{source_seq_file}')
    destination_seq = fileseq.FileSequence(destination_path)
    for frame in range(source_seq.start(), source_seq.end()+1):
        source_framepath = os.path.join(source_dir, source_seq.frame(frame))
        destination_framepath = os.path.join(tofolder, destination_seq.frame(frame))
        relativepath = os.path.relpath(source_framepath, fromfolder)
        target = Path(source_framepath)
        destination = Path(destination_framepath)
        target_dir = destination.parent
        target_dir.mkdir(exist_ok=True, parents=True)
        relative_source = os.path.relpath(target, target_dir)
        dir_fd = os.open(str(target_dir.absolute()), os.O_RDONLY)
        try:
            os.symlink(relative_source, destination.name, dir_fd=dir_fd)
        finally:
            os.close(dir_fd)




if __name__ == '__main__':
    # source_dir_path = '/mnt/pb6/Filmgate/TRM/io/From_Client/Uel_2022-10-04/OFFICE-SEQUENCES/Lighting/trm_ep01-rl01_00760_lighting_v0005/',
    _data = dict(
        source_dir_path='/mnt/pb6/Filmgate/TRM/io/From_Client/Uel_2022-10-04/OFFICE-SEQUENCES/',
        destination_dir_path='/home/rithik/rithik/test/To_Shakti/',
        job='trm',
        source_dir_type='shot'
    )
    # run(**_data)
