import lucidity

LOCAL_PKG_NAME = lucidity.Template('local_pkg_name',
                                  '{pkg_type}-{shot}-{discipline}-{plate_version_prefix}{plate_version_num}'
                                  '-{vendor}-{shot_version_prefix}{shot_version_num}')

GLOBAL_PKG_NAME = lucidity.Template('global_pkg_name',
                                    '{date}-{vendor}-{show}-{pkg_version_prefix}{pkg_version_num}')

WORKFILE_NAME = lucidity.Template('workfile_name',
                                  '{shot}-{discipline}-{plate_version_prefix}{plate_version_num}-aces'
                                  '_{element_desc}_{shot_version_prefix}{shot_version_num}')

SEQ_FILE_NAME = lucidity.Template('seq_file_name',
                                  '{shot}-{discipline}-{plate_version_prefix}{plate_version_num}-aces'
                                  '_{element_desc}_{shot_version_prefix}{shot_version_num}.{frame}')



