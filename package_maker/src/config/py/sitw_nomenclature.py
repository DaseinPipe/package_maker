import lucidity

LOCAL_PKG_NAME = lucidity.Template('local_pkg_name',
                                  '{discipline}-package')

GLOBAL_PKG_NAME = lucidity.Template('global_pkg_name',
                                    'SITW_{vendor}_{date}_{pkg_version_prefix}{pkg_version_num}')





SEQ_FILE_NAME = lucidity.Template('seq_filename',
                                  '{shot}_{shot_version_prefix}{shot_version_num}.{frame}')

FINAL_MOV_FILENAME = lucidity.Template('final_mov_filename',
                                       '{shot}_{shot_version_prefix}{shot_version_num}.mov')

MOV_FILENAME = lucidity.Template( 'mov_filename',
                                  '{shot}_{discipline}_{shot_version_prefix}{shot_version_num}.mov')






