import fileseq
import re
from package_maker.src.config.config_client import *
from package_maker.src.utils import general_utils


class Seq:
    def __init__(self, base_data=None):
        self.base_data = base_data
        self.job = self.base_data.get('job', os.environ.get('show'))
        self._path_data = base_data or dict()

        self.source_path = self.base_data.get('source_path')
        self.ext = self.base_data.get('ext') or self.get_ext
        self.type = 'for_approval'



    @property
    def frame(self):
        if not self.source_path:
            return UNKNOWN
        filepath = self.source_path
        seq = fileseq.findSequenceOnDisk(filepath)
        if seq:
            if seq.frameSet():
                return f'{seq.frameSet()}@'
        frame_expression = r'(?<!\/)(?=.*\W)\b\d+(?=.*\W)'
        frame_result = re.search(frame_expression, filepath)
        if frame_result:
            return frame_result.group(0)
        return UNKNOWN

    @frame.setter
    def frame(self, frame_name):
        self._frame = frame_name

    @property
    def path_data(self):
        if not self._path_data.get('frame'):
            self._path_data['frame'] = self.frame
        return self._path_data

    @path_data.setter
    def path_data(self, data=None):
        self._path_data = data

    @property
    def template(self):
        return get_path(self.job, 'seq_filepath')

    @property
    def destination_path(self):
        return self.template.format(self.path_data)


if __name__ == '__main__':

    base_data = {'source_path': '/mnt/pb6/Filmgate/TRM/io/From_Amolesh/20221014/0530_issue/Output/trm_ep01-rl02_00530_compositing_v0001/trm_ep01-rl02_00530_compositing_v0001.1009-1026#.exr', 'pkg_version': 'A', 'ext': 'exr', 'shot_version_num': '001', 'shot_version_prefix': 'v', 'shot': 'TRM_ep01-rl02_00530', 'pkg_dir_type': 'for_approval', 'pkg_type': 'shot', 'job': 'trm', 'discipline': 'comp', 'date': '20221008', 'vendor': 'dasein', 'show': 'trm', 'pkg_version_prefix': 'v', 'pkg_version_num': '0021', 'pkg_dir': '/mnt/pb6/Filmgate/TRM/io/To_Client/Package', 'frame': '1009-1026@', 'element_desc': 'comp'}

    t= ForApproval(base_data=base_data)
    r = 'temp_dir/20221002-dasein-asterix-v0005-package/20221002-dasein-asterix-v0005/shot-080_bb_0375-roto-master01-dasein-v001/for_approval/080_bb_0375-roto-master01-aces_UNKNOWN_v001/080_bb_0375-roto-master01-aces_UNKNOWN_v001.0-99.exr'
    r = t.destination_path
    print(r)

    # print(t.template.parse(r))



