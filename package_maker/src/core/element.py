import fileseq
import re
from package_maker.src.config.config_main import *
from package_maker.src.utils import general_utils


class Element:
    def __init__(self, base_data=None):
        self.base_data = base_data
        self.job = self.base_data.get('job', os.environ.get('job'))
        self._element_desc = UNKNOWN
        self._frame = UNKNOWN
        self._path_data = base_data or dict()

        self.source_path = self.base_data.get('source_path')
        self.ext = self.base_data.get('ext') or self.get_ext
        self.type = 'for_approval'

    @property
    def get_ext(self):
        _, ext = os.path.splitext(self.s)
        return ext.split('.')[-1]


    @property
    def element_desc_ext_name_patterns(self):
        default_mapping = {
            'UDP': 'UDP',
            'paint': 'prep',
            'prep': 'prep',
            'wire': 'wire',
            'cone': 'cones',
        }
        return dict(
            exr=default_mapping,
            jpg=default_mapping,
            jpeg=default_mapping,
            png=default_mapping,
            tiff=default_mapping,
        )

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
    def element_desc(self):
        if self._element_desc == UNKNOWN:
            if not self.source_path:
                return UNKNOWN
            mapping_data = self.element_desc_ext_name_patterns.get(self.ext, {})
            patterns = mapping_data.keys()
            result = general_utils.find_patten(self.source_path, patterns)
            return mapping_data.get(result, UNKNOWN)
        return self._element_desc

    @element_desc.setter
    def element_desc(self, element_desc_name=None):
        self._element_desc = element_desc_name

    @property
    def path_data(self):
        if not self._path_data.get('frame'):
            self._path_data['frame'] = self.frame
        if not self._path_data.get('element_desc'):
            self._path_data['element_desc'] = self.element_desc
        return self._path_data

    @path_data.setter
    def path_data(self, data=None):
        self._path_data = data

    @property
    def template(self):
        return get_path(self.job, 'for_approval_filepath_template')

    @property
    def destination_path(self):
        return self.template.format(self.path_data)


if __name__ == '__main__':

    base_data = {'pkg_dir':'temp_dir', 'source_path': 'C:/mnt/mpcparis/A5/io/From_Pixstone/20220705D/exr_seq/test.0-99@.exr', 'ext':'exr', 'pkg_dir_type': 'for_approval', 'custom_name': '', 'shot': '080_bb_0375', 'discipline': 'roto', 'plate_version_num': '01', 'shot_version_num': '001', 'plate_version_prefix': 'master', 'shot_version_prefix': 'v', 'files': [{'source_path': 'C:/mnt/mpcparis/A5/io/From_Pixstone/20220705B/082_em_0325/082_em_0325_roto_v005.nk', 'ext': 'nk', 'pkg_dir_type': 'workfile', 'custom_name': '', 'shot': '080_bb_0375', 'discipline': 'roto', 'plate_version_num': '01', 'shot_version_num': '001', 'plate_version_prefix': 'master', 'shot_version_prefix': 'v', 'date': '20221002', 'vendor': 'dasein', 'show': 'asterix', 'pkg_version_prefix': 'v', 'pkg_version_num': '0005', 'pkg_type': 'shot', 'pkg_dir': 'temp_dir', 'app': 'test', 'frame': '1001', 'ext': 'exr', 'destination_path': 'temp_dir/20221002-dasein-asterix-v0005-package/20221002-dasein-asterix-v0005/shot-080_bb_0375-roto-master01-dasein-v001/for_approval/080_bb_0375-roto-master01-aces_test_v001/080_bb_0375-roto-master01-aces_test_1001_v001.exr'}, {'source_path': 'C:/mnt/mpcparis/A5/io/From_Pixstone/20220705B/082_em_0325/082_em_0325_roto_v005.sfx', 'pkg_dir_type': 'workfile', 'custom_name': '', 'shot': '080_bb_0375', 'discipline': 'roto', 'plate_version_num': '01', 'shot_version_num': '001', 'plate_version_prefix': 'master', 'shot_version_prefix': 'v', 'date': '20221002', 'vendor': 'dasein', 'show': 'asterix', 'pkg_version_prefix': 'v', 'pkg_version_num': '0005', 'pkg_type': 'shot', 'pkg_dir': 'temp_dir', 'app': 'test', 'frame': '1001', 'ext': 'exr', 'destination_path': 'temp_dir/20221002-dasein-asterix-v0005-package/20221002-dasein-asterix-v0005/shot-080_bb_0375-roto-master01-dasein-v001/for_approval/080_bb_0375-roto-master01-aces_test_v001/080_bb_0375-roto-master01-aces_test_1001_v001.exr'}, {'source_path': 'C:/mnt/mpcparis/A5/io/From_Pixstone/20220705B/082_em_0325/082_em_0325_roto_a_mb_v005/082_em_0325_roto_a_mb_v005.993#.exr', 'pkg_dir_type': 'for_approval', 'custom_name': '', 'shot': '080_bb_0375', 'discipline': 'roto', 'plate_version_num': '01', 'shot_version_num': '001', 'plate_version_prefix': 'master', 'shot_version_prefix': 'v', 'date': '20221002', 'vendor': 'dasein', 'show': 'asterix', 'pkg_version_prefix': 'v', 'pkg_version_num': '0005', 'pkg_type': 'shot', 'pkg_dir': 'temp_dir', 'app': 'test', 'frame': '1001', 'ext': 'exr', 'destination_path': 'temp_dir/20221002-dasein-asterix-v0005-package/20221002-dasein-asterix-v0005/shot-080_bb_0375-roto-master01-dasein-v001/for_approval/080_bb_0375-roto-master01-aces_test_v001/080_bb_0375-roto-master01-aces_test_1001_v001.exr'}, {'source_path': 'C:/mnt/mpcparis/A5/io/From_Pixstone/20220705B/082_em_0325/082_em_0325_roto_a_nmb_v005/082_em_0325_roto_a_nmb_v005.993#.exr', 'pkg_dir_type': 'for_approval', 'custom_name': '', 'shot': '080_bb_0375', 'discipline': 'roto', 'plate_version_num': '01', 'shot_version_num': '001', 'plate_version_prefix': 'master', 'shot_version_prefix': 'v', 'date': '20221002', 'vendor': 'dasein', 'show': 'asterix', 'pkg_version_prefix': 'v', 'pkg_version_num': '0005', 'pkg_type': 'shot', 'pkg_dir': 'temp_dir', 'app': 'test', 'frame': '1001', 'ext': 'exr', 'destination_path': 'temp_dir/20221002-dasein-asterix-v0005-package/20221002-dasein-asterix-v0005/shot-080_bb_0375-roto-master01-dasein-v001/for_approval/080_bb_0375-roto-master01-aces_test_v001/080_bb_0375-roto-master01-aces_test_1001_v001.exr'}, {'source_path': 'C:/mnt/mpcparis/A5/io/From_Pixstone/20220705B/082_em_0325/082_em_0325_roto_b_mb_v005/082_em_0325_roto_b_mb_v005.993#.exr', 'pkg_dir_type': 'for_approval', 'custom_name': '', 'shot': '080_bb_0375', 'discipline': 'roto', 'plate_version_num': '01', 'shot_version_num': '001', 'plate_version_prefix': 'master', 'shot_version_prefix': 'v', 'date': '20221002', 'vendor': 'dasein', 'show': 'asterix', 'pkg_version_prefix': 'v', 'pkg_version_num': '0005', 'pkg_type': 'shot', 'pkg_dir': 'temp_dir', 'app': 'test', 'frame': '1001', 'ext': 'exr', 'destination_path': 'temp_dir/20221002-dasein-asterix-v0005-package/20221002-dasein-asterix-v0005/shot-080_bb_0375-roto-master01-dasein-v001/for_approval/080_bb_0375-roto-master01-aces_test_v001/080_bb_0375-roto-master01-aces_test_1001_v001.exr'}, {'source_path': 'C:/mnt/mpcparis/A5/io/From_Pixstone/20220705B/082_em_0325/082_em_0325_roto_b_nmb_v005/082_em_0325_roto_b_nmb_v005.993#.exr', 'pkg_dir_type': 'for_approval', 'custom_name': '', 'shot': '080_bb_0375', 'discipline': 'roto', 'plate_version_num': '01', 'shot_version_num': '001', 'plate_version_prefix': 'master', 'shot_version_prefix': 'v', 'date': '20221002', 'vendor': 'dasein', 'show': 'asterix', 'pkg_version_prefix': 'v', 'pkg_version_num': '0005', 'pkg_type': 'shot', 'pkg_dir': 'temp_dir', 'app': 'test', 'frame': '1001', 'ext': 'exr', 'destination_path': 'temp_dir/20221002-dasein-asterix-v0005-package/20221002-dasein-asterix-v0005/shot-080_bb_0375-roto-master01-dasein-v001/for_approval/080_bb_0375-roto-master01-aces_test_v001/080_bb_0375-roto-master01-aces_test_1001_v001.exr'}, {'source_path': 'C:/mnt/mpcparis/A5/io/From_Pixstone/20220705B/082_em_0325/082_em_0325_roto_b_nmb_v006/foo.nk', 'pkg_dir_type': 'workfile', 'custom_name': '', 'shot': '080_bb_0375', 'discipline': 'roto', 'plate_version_num': '01', 'shot_version_num': '001', 'plate_version_prefix': 'master', 'shot_version_prefix': 'v', 'date': '20221002', 'vendor': 'dasein', 'show': 'asterix', 'pkg_version_prefix': 'v', 'pkg_version_num': '0005', 'pkg_type': 'shot', 'pkg_dir': 'temp_dir', 'app': 'test', 'frame': '1001', 'ext': 'exr', 'destination_path': 'temp_dir/20221002-dasein-asterix-v0005-package/20221002-dasein-asterix-v0005/shot-080_bb_0375-roto-master01-dasein-v001/for_approval/080_bb_0375-roto-master01-aces_test_v001/080_bb_0375-roto-master01-aces_test_1001_v001.exr'}, {'source_path': 'C:/mnt/mpcparis/A5/io/From_Pixstone/20220705B/foo/foo.nk', 'pkg_dir_type': 'workfile', 'custom_name': '', 'shot': '080_bb_0375', 'discipline': 'roto', 'plate_version_num': '01', 'shot_version_num': '001', 'plate_version_prefix': 'master', 'shot_version_prefix': 'v', 'date': '20221002', 'vendor': 'dasein', 'show': 'asterix', 'pkg_version_prefix': 'v', 'pkg_version_num': '0005', 'pkg_type': 'shot', 'pkg_dir': 'temp_dir', 'app': 'test', 'frame': '1001', 'ext': 'exr', 'destination_path': 'temp_dir/20221002-dasein-asterix-v0005-package/20221002-dasein-asterix-v0005/shot-080_bb_0375-roto-master01-dasein-v001/for_approval/080_bb_0375-roto-master01-aces_test_v001/080_bb_0375-roto-master01-aces_test_1001_v001.exr'}, {'source_path': 'C:/mnt/mpcparis/A5/io/From_Pixstone/20220705B/foo/082_em_0325_roto_a_mb_v006.993#.exr', 'pkg_dir_type': 'for_approval', 'custom_name': '', 'shot': '080_bb_0375', 'discipline': 'roto', 'plate_version_num': '01', 'shot_version_num': '001', 'plate_version_prefix': 'master', 'shot_version_prefix': 'v', 'date': '20221002', 'vendor': 'dasein', 'show': 'asterix', 'pkg_version_prefix': 'v', 'pkg_version_num': '0005', 'pkg_type': 'shot', 'pkg_dir': 'temp_dir', 'app': 'test', 'frame': '1001', 'ext': 'exr', 'destination_path': 'temp_dir/20221002-dasein-asterix-v0005-package/20221002-dasein-asterix-v0005/shot-080_bb_0375-roto-master01-dasein-v001/for_approval/080_bb_0375-roto-master01-aces_test_v001/080_bb_0375-roto-master01-aces_test_1001_v001.exr'}, {'source_path': 'C:/mnt/mpcparis/A5/io/From_Pixstone/20220705C/082_em_0320-src-master02/082_em_0320-src-master02_roto_v008.nk', 'pkg_dir_type': 'workfile', 'custom_name': '', 'shot': '080_bb_0375', 'discipline': 'roto', 'plate_version_num': '01', 'shot_version_num': '001', 'plate_version_prefix': 'master', 'shot_version_prefix': 'v', 'date': '20221002', 'vendor': 'dasein', 'show': 'asterix', 'pkg_version_prefix': 'v', 'pkg_version_num': '0005', 'pkg_type': 'shot', 'pkg_dir': 'temp_dir', 'app': 'test', 'frame': '1001', 'ext': 'exr', 'destination_path': 'temp_dir/20221002-dasein-asterix-v0005-package/20221002-dasein-asterix-v0005/shot-080_bb_0375-roto-master01-dasein-v001/for_approval/080_bb_0375-roto-master01-aces_test_v001/080_bb_0375-roto-master01-aces_test_1001_v001.exr'}, {'source_path': 'C:/mnt/mpcparis/A5/io/From_Pixstone/20220705C/082_em_0320-src-master02/082_em_0320-src-master02_roto_v008.sfx', 'pkg_dir_type': 'workfile', 'custom_name': '', 'shot': '080_bb_0375', 'discipline': 'roto', 'plate_version_num': '01', 'shot_version_num': '001', 'plate_version_prefix': 'master', 'shot_version_prefix': 'v', 'date': '20221002', 'vendor': 'dasein', 'show': 'asterix', 'pkg_version_prefix': 'v', 'pkg_version_num': '0005', 'pkg_type': 'shot', 'pkg_dir': 'temp_dir', 'app': 'test', 'frame': '1001', 'ext': 'exr', 'destination_path': 'temp_dir/20221002-dasein-asterix-v0005-package/20221002-dasein-asterix-v0005/shot-080_bb_0375-roto-master01-dasein-v001/for_approval/080_bb_0375-roto-master01-aces_test_v001/080_bb_0375-roto-master01-aces_test_1001_v001.exr'}, {'source_path': 'C:/mnt/mpcparis/A5/io/From_Pixstone/20220705C/082_em_0320-src-master02/082_em_0320-src-master02_roto_mb_v008/082_em_0320-src-master02_roto_mb_v008.993#.exr', 'pkg_dir_type': 'for_approval', 'custom_name': '', 'shot': '080_bb_0375', 'discipline': 'roto', 'plate_version_num': '01', 'shot_version_num': '001', 'plate_version_prefix': 'master', 'shot_version_prefix': 'v', 'date': '20221002', 'vendor': 'dasein', 'show': 'asterix', 'pkg_version_prefix': 'v', 'pkg_version_num': '0005', 'pkg_type': 'shot', 'pkg_dir': 'temp_dir', 'app': 'test', 'frame': '1001', 'ext': 'exr', 'destination_path': 'temp_dir/20221002-dasein-asterix-v0005-package/20221002-dasein-asterix-v0005/shot-080_bb_0375-roto-master01-dasein-v001/for_approval/080_bb_0375-roto-master01-aces_test_v001/080_bb_0375-roto-master01-aces_test_1001_v001.exr'}, {'source_path': 'C:/mnt/mpcparis/A5/io/From_Pixstone/20220705C/082_em_0320-src-master02/082_em_0320-src-master02_roto_nmb_v008/082_em_0320-src-master02_roto_nmb_v008.993#.exr', 'pkg_dir_type': 'for_approval', 'custom_name': '', 'shot': '080_bb_0375', 'discipline': 'roto', 'plate_version_num': '01', 'shot_version_num': '001', 'plate_version_prefix': 'master', 'shot_version_prefix': 'v', 'date': '20221002', 'vendor': 'dasein', 'show': 'asterix', 'pkg_version_prefix': 'v', 'pkg_version_num': '0005', 'pkg_type': 'shot', 'pkg_dir': 'temp_dir', 'app': 'test', 'frame': '1001', 'ext': 'exr', 'destination_path': 'temp_dir/20221002-dasein-asterix-v0005-package/20221002-dasein-asterix-v0005/shot-080_bb_0375-roto-master01-dasein-v001/for_approval/080_bb_0375-roto-master01-aces_test_v001/080_bb_0375-roto-master01-aces_test_1001_v001.exr'}, {'source_path': 'C:/mnt/mpcparis/A5/io/From_Pixstone/20220705D/080_bb_0375/080_bb_0375_roto_v004.nk', 'pkg_dir_type': 'workfile', 'custom_name': '', 'shot': '080_bb_0375', 'discipline': 'roto', 'plate_version_num': '01', 'shot_version_num': '001', 'plate_version_prefix': 'master', 'shot_version_prefix': 'v', 'date': '20221002', 'vendor': 'dasein', 'show': 'asterix', 'pkg_version_prefix': 'v', 'pkg_version_num': '0005', 'pkg_type': 'shot', 'pkg_dir': 'temp_dir', 'app': 'test', 'frame': '1001', 'ext': 'exr', 'destination_path': 'temp_dir/20221002-dasein-asterix-v0005-package/20221002-dasein-asterix-v0005/shot-080_bb_0375-roto-master01-dasein-v001/for_approval/080_bb_0375-roto-master01-aces_test_v001/080_bb_0375-roto-master01-aces_test_1001_v001.exr'}, {'source_path': 'C:/mnt/mpcparis/A5/io/From_Pixstone/20220705D/080_bb_0375/080_bb_0375_roto_v004.sfx', 'pkg_dir_type': 'workfile', 'custom_name': '', 'shot': '080_bb_0375', 'discipline': 'roto', 'plate_version_num': '01', 'shot_version_num': '001', 'plate_version_prefix': 'master', 'shot_version_prefix': 'v', 'date': '20221002', 'vendor': 'dasein', 'show': 'asterix', 'pkg_version_prefix': 'v', 'pkg_version_num': '0005', 'pkg_type': 'shot', 'pkg_dir': 'temp_dir', 'app': 'test', 'frame': '1001', 'ext': 'exr', 'destination_path': 'temp_dir/20221002-dasein-asterix-v0005-package/20221002-dasein-asterix-v0005/shot-080_bb_0375-roto-master01-dasein-v001/for_approval/080_bb_0375-roto-master01-aces_test_v001/080_bb_0375-roto-master01-aces_test_1001_v001.exr'}, {'source_path': 'C:/mnt/mpcparis/A5/io/From_Pixstone/20220705D/080_bb_0375/080_bb_0375_roto_v004/080_bb_0375_roto_v004.1000', 'pkg_dir_type': 'custom', 'custom_name': '', 'shot': '080_bb_0375', 'discipline': 'roto', 'plate_version_num': '01', 'shot_version_num': '001', 'plate_version_prefix': 'master', 'shot_version_prefix': 'v', 'date': '20221002', 'vendor': 'dasein', 'show': 'asterix', 'pkg_version_prefix': 'v', 'pkg_version_num': '0005', 'pkg_type': 'shot', 'pkg_dir': 'temp_dir', 'app': 'test', 'frame': '1001', 'ext': 'exr', 'destination_path': 'temp_dir/20221002-dasein-asterix-v0005-package/20221002-dasein-asterix-v0005/shot-080_bb_0375-roto-master01-dasein-v001/for_approval/080_bb_0375-roto-master01-aces_test_v001/080_bb_0375-roto-master01-aces_test_1001_v001.exr'}, {...}, {'source_path': 'C:/mnt/project/080/bb/0375/roto/for_approval/.nk/080_bb_0375_roto_v004.nk', 'pkg_dir_type': 'workfile', 'custom_name': ''}, {'source_path': 'C:/mnt/project/080/bb/0375/roto/for_approval/.sfx/080_bb_0375_roto_v004.sfx', 'pkg_dir_type': 'workfile', 'custom_name': ''}, {'source_path': 'C:/mnt/project/082/em/0320/roto/for_approval/.exr/082_em_0320_roto_v008.0993..exr', 'pkg_dir_type': 'for_approval', 'custom_name': ''}, {'source_path': 'C:/mnt/project/082/em/0320/roto/workfile/.nk/082_em_0320_roto_v008.nk', 'pkg_dir_type': 'workfile', 'custom_name': ''}, {'source_path': 'C:/mnt/project/082/em/0320/roto/workfile/.sfx/082_em_0320_roto_v008.sfx', 'pkg_dir_type': 'workfile', 'custom_name': ''}, {'source_path': 'C:/mnt/project/082/em/0325/roto/for_approval/.exr/082_em_0325_roto_v005.0993..exr', 'pkg_dir_type': 'for_approval', 'custom_name': ''}, {'source_path': 'C:/mnt/project/082/em/0325/roto/for_approval/.nk/082_em_0325_roto_v006.nk', 'pkg_dir_type': 'workfile', 'custom_name': ''}, {'source_path': 'C:/mnt/project/082/em/0325/roto/geometry/.exr/082_em_0325_roto_v006.0993..exr', 'pkg_dir_type': 'for_approval', 'custom_name': ''}, {'source_path': 'C:/mnt/project/082/em/0325/roto/workfile/.nk/082_em_0325_roto_v005.nk', 'pkg_dir_type': 'workfile', 'custom_name': ''}, {'source_path': 'C:/mnt/project/082/em/0325/roto/workfile/.sfx/082_em_0325_roto_v005.sfx', 'pkg_dir_type': 'workfile', 'custom_name': ''}], 'date': '20221002', 'vendor': 'dasein', 'show': 'asterix', 'pkg_version_prefix': 'v', 'pkg_version_num': '0005', 'pkg_type': 'shot'}

    t= Element(base_data=base_data)
    r = 'temp_dir/20221002-dasein-asterix-v0005-package/20221002-dasein-asterix-v0005/shot-080_bb_0375-roto-master01-dasein-v001/for_approval/080_bb_0375-roto-master01-aces_UNKNOWN_v001/080_bb_0375-roto-master01-aces_UNKNOWN_v001.0-99.exr'
    r = t.destination_path
    print(r)

    # print(t.template.parse(r))

