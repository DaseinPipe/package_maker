import lucidity
from package_maker import src

LOCAL_PKG_NAME = lucidity.Template('local_pkg_name',
                                  'TRM-{discipline}-{vendor}-package')

GLOBAL_PKG_NAME = lucidity.Template('global_pkg_name',
                                    'PKG-TRM-{date}_{pkg_version}')


SHOT_PKG_NAME = lucidity.Template('shot_pkg_name',
                                    '{shot}_compositing_{shot_version_prefix}{shot_version_num}')


SEQ_FILE_NAME = lucidity.Template('seq_file_name',
                                  '{filename}')




