import fileseq
import os
from package_maker.src.config.config_client import *


def get_frame_range(file):
    seq = fileseq.findSequenceOnDisk(file)
    try:
        seq = fileseq.findSequenceOnDisk(file)
    except:
        return []

    start, end = seq.frameRange().split('-')
    return int(start), int(end)


def check_seq_exists(dir_path):
    is_seqs = False
    for root, dirs, files in os.walk(dir_path):
        seqs = fileseq.findSequencesOnDisk(root)
        if seqs:
            is_seqs = True
    return is_seqs


def extend_files(dir_path, show_data=None):
    SHOW_DATA = show_data or get_show_data(os.environ.get(('show')))
    file_list = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.split('.')[-1] not in SHOW_DATA.get('seq_ext', global_seq_ext):
                file_list.append(os.path.join(root, file).replace('\\', '/'))
                continue
        seqs = fileseq.findSequencesOnDisk(root)
        if not seqs:
            continue
        for seq in seqs:
            if str(seq).split('.')[-1] in SHOW_DATA.get('seq_ext', global_seq_ext):
                file_list.append(str(seq).replace('\\', '/'))
    return (file_list)


if __name__ == '__main__':
    t = r'C:\mnt\mpcparis\A5\io\From_Pixstone\20220705D'

    r = fileseq.FileSequence(
        'C:\\mnt\\mpcparis\\A5\\io\\From_Pixstone\\20220705D\\080_bb_0375\\080_bb_0375_roto_v4@@@.nk')
    print(r.format())
    print(r.to_dict())

    print(extend_files(t))
