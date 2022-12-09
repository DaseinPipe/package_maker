import lucidity
from package_maker import src

LOCAL_PKG_NAME = lucidity.Template('local_pkg_name',
                                  'Boderland-{discipline}-{vendor}-package')

GLOBAL_PKG_NAME = lucidity.Template('global_pkg_name',
                                    'PKG-Boderland-{date}_{pkg_version}')


SHOT_PKG_NAME = lucidity.Template('shot_pkg_name',
                                    'Boderland_{shot}_compositing_{shot_version_prefix}{shot_version_num}')


SEQ_FILE_NAME = lucidity.Template('seq_file_name',
                                  '{filename}')


VENDOR_SHOT_PKG_NAME = lucidity.Template('vendor_shot_pkg_name',
                                    'boderland_{shot}')




