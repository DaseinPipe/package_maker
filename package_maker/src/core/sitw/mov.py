import fileseq
import re
from package_maker.src.config.config_client import *
from package_maker.src.utils import general_utils


class Mov:
    def __init__(self, base_data=None):
        self.base_data = base_data
        self.job = self.base_data.get('job', os.environ.get('job'))
        self._path_data = base_data or dict()
        self.source_path = self.base_data.get('source_path')
        self.type = 'mov'

    @property
    def path_data(self):
        return self._path_data

    @path_data.setter
    def path_data(self, data=None):
        self._path_data = data

    @property
    def template(self):
        return get_path(self.job, 'mov_filepath')
    @property
    def destination_path(self):
        return self.template.format(self.path_data)


if __name__ == '__main__':

    base_data = {'source_path': 'C:/mnt/mpcparis/A5/io/From_Pixstone/20220705B/082_em_0325/082_em_0325_roto_v005.nk', 'pkg_dir_type': 'workfile', 'custom_name': '', 'ext': 'nk', 'shot': '080_bb_0375', 'discipline': 'roto', 'plate_version_num': '01', 'shot_version_num': '001', 'plate_version_prefix': 'master', 'shot_version_prefix': 'v', 'date': '20221005', 'vendor': 'dasein', 'show': 'asterix', 'pkg_version_prefix': 'v', 'pkg_version_num': '0001', 'pkg_dir': '/mnt/mpcparis/A5/io/To_Client/packages', 'pkg_type': 'shot'}
    base_data1 = {'source_path': 'C:/mnt/mpcparis/NOTRE_DAME/IO/From_Rotomaker/20220530_MM/A/3035_0140-src-tracking-master01_v1001/3035_0140-src-master01-aces_nukeLD_v1001.nk', 'pkg_dir_type': 'workfile', 'custom_name': '', 'ext': 'nk', 'shot': '080_bb_0375', 'discipline': 'matchmove', 'plate_version_num': '01', 'shot_version_num': '001', 'plate_version_prefix': 'master', 'shot_version_prefix': 'v', 'date': '20221005', 'vendor': 'dasein', 'show': 'asterix', 'pkg_version_prefix': 'v', 'pkg_version_num': '0001', 'pkg_dir': '/mnt/mpcparis/A5/io/To_Client/packages', 'pkg_type': 'shot'}
    t = FinalMov(base_data=base_data1)
    r = t.path_data
    # print(r)

    # # print(t.template.parse(r))

