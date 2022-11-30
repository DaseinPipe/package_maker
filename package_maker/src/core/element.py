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
        self.type = 'element'

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
            result = general_utils.find_patten(self.source_path.lower(), patterns)
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
        return get_path(self.job, 'element_filepath_template')

    @property
    def destination_path(self):
        return self.template.format(self.path_data)


if __name__ == '__main__':

    base_data = {'source_path': '/mnt/mpcparis/DOGMAN/io/from_shakti/20221128_prep/Dogman_025_010-prep-master01-mpc_Paint_v001/Dogman_025_010-prep-master01-mpc_Paint_v001/025_010-prep-master01-mpc_Paint_v001.993-1100#.exr', 'pkg_dir_type': 'element', 'custom_name': '', 'ext': 'exr', 'pkg_type': 'shot', 'job': 'dogman', 'shot': '080_020', 'discipline': 'prep', 'plate_version_num': '01', 'shot_version_num': '0002', 'plate_version_prefix': 'master', 'shot_version_prefix': 'v', 'date': '20221130', 'vendor': 'dasein', 'show': 'dogman', 'pkg_version_prefix': 'v', 'pkg_version_num': '0013', 'pkg_dir': '/mnt/mpcparis/DOGMAN/io/to_client/packages', 'destination_path': '/mnt/mpcparis/DOGMAN/io/to_client/packages/PKG-20221130-dasein-dogman-v0013-package/20221130-dasein-dogman-v0013/shot-080_020-prep-master01-dasein-v0002/element/080_020-prep-master01-aces_UNKNOWN_v0002/080_020-prep-master01-aces_UNKNOWN_v0002.993-1100@.exr'}
    t= Element(base_data=base_data)
    r = t.destination_path
    print(r)

    # print(t.template.parse(r))

