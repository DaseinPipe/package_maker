import fileseq
import re
from package_maker.src.config.config_main import *
from package_maker.src.utils import general_utils


class Workfile:
    def __init__(self, base_data=None):
        self.base_data = base_data
        self._element_desc = UNKNOWN
        self._path_data = base_data or dict()
        self.ext = self.base_data.get('ext') or self.get_ext
        self.source_path = self.base_data.get('source_path')
        self.type = 'workfile'


    @property
    def get_ext(self):
        _, ext = os.path.splitext(self.s)
        return ext.split('.')[-1]


    @property
    def element_desc_ext_assignment(self):
        return {
            'nk': 'nuke',
            'ma': 'maya',
            'sfx': 'sfx',
            '3de': '3de',
        }

    @property
    def element_desc_ext_name_patterns(self):
        return dict(
            nk=["nukeLD"],
        )

    @property
    def element_desc(self):
        if self._element_desc == UNKNOWN:
            if not self.ext:
                return UNKNOWN
            patterns = self.element_desc_ext_name_patterns.get(self.ext, [])
            element_desc_result = general_utils.find_patten(self.source_path, patterns) or None
            if element_desc_result:
                return element_desc_result
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
    base_data1 = {'source_path': 'C:/mnt/mpcparis/NOTRE_DAME/IO/From_Rotomaker/20220530_MM/A/3035_0140-src-tracking-master01_v1001/3035_0140-src-master01-aces_nukeLD_v1001.nk', 'pkg_dir_type': 'workfile', 'custom_name': '', 'ext': 'nk', 'shot': '080_bb_0375', 'discipline': 'matchmove', 'plate_version_num': '01', 'shot_version_num': '001', 'plate_version_prefix': 'master', 'shot_version_prefix': 'v', 'date': '20221005', 'vendor': 'dasein', 'show': 'asterix', 'pkg_version_prefix': 'v', 'pkg_version_num': '0001', 'pkg_dir': '/mnt/mpcparis/A5/io/To_Client/packages', 'pkg_type': 'shot'}
    t = Workfile(base_data=base_data1)
    r = t.destination_path
    print(r)

    # print(t.template.parse(r))

