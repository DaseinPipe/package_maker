import fileseq
import re
from package_maker.src.config.config_main import *
from package_maker.src.utils import general_utils


class Geomerty:
    def __init__(self, base_data=None):
        self.base_data = base_data
        self._element_desc = UNKNOWN
        self._path_data = base_data or dict()
        self.ext = self.base_data.get('ext') or self.get_ext
        self.source_path = self.base_data.get('source_path')
        self.type = 'geomerty'

    @property
    def element_desc_ext_assignment(self):
        return {
            'abc': 'geoABC',
            'fbx': 'geoFBX'
        }

    @property
    def get_ext(self):
        _, ext = os.path.splitext(self.s)
        return ext.split('.')[-1]

    @property
    def element_desc(self):
        if self._element_desc == UNKNOWN:
            if not self.ext:
                return UNKNOWN
            return self.element_desc_ext_assignment.get(self.ext, UNKNOWN)
        return self._element_desc

    @element_desc.setter
    def element_desc(self, element_desc_name=None):
        self._element_desc = element_desc_name

    @property
    def path_data(self):
        if not self._path_data.get('element_desc'):
            self._path_data['element_desc'] = self.element_desc
        return self._path_data

    @path_data.setter
    def path_data(self, data=None):
        self._path_data = data

    @property
    def template(self):
        return workfile_filepath_template

    @property
    def destination_path(self):
        return self.template.format(self.path_data)


if __name__ == '__main__':

    base_data = {'source_path': 'C:/mnt/mpcparis/A5/io/From_Pixstone/20220705B/082_em_0325/082_em_0325_roto_v005.nk', 'pkg_dir_type': 'workfile', 'custom_name': '', 'ext': 'nk', 'shot': '080_bb_0375', 'discipline': 'roto', 'plate_version_num': '01', 'shot_version_num': '001', 'plate_version_prefix': 'master', 'shot_version_prefix': 'v', 'date': '20221005', 'vendor': 'dasein', 'show': 'asterix', 'pkg_version_prefix': 'v', 'pkg_version_num': '0001', 'pkg_dir': '/mnt/mpcparis/A5/io/To_Client/packages', 'pkg_type': 'shot'}
    base_data1 = {'source_path': 'C:/mnt/mpcparis/A5/io/From_Pixstone/20220705B/082_em_0325/082_em_0325_roto_v005.sfx', 'pkg_dir_type': 'workfile', 'custom_name': '', 'ext': 'sfx', 'shot': '080_bb_0375', 'discipline': 'roto', 'plate_version_num': '01', 'shot_version_num': '001', 'plate_version_prefix': 'master', 'shot_version_prefix': 'v', 'date': '20221005', 'vendor': 'dasein', 'show': 'asterix', 'pkg_version_prefix': 'v', 'pkg_version_num': '0001', 'pkg_dir': '/mnt/mpcparis/A5/io/To_Client/packages', 'pkg_type': 'shot'}
    t = Geomerty(base_data=base_data1)
    r = t.destination_path
    print(r)

    # print(t.template.parse(r))

