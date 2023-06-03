
import os
__config_folder_path = os.path.dirname(os.path.realpath(__file__))

VENDOR_LIST = [
    'Select',
    'Rotomaker',
    'Shakti',
    'Amolesh'
]

CLIENT_LIST = [
    'mpc',
]

def vendor_config_data(vendor):
    vendor = vendor.lower()
    vendor_global_config = dict(
        destination=dict(
            MPC_Paris=dict(
                job=dict(
                    asterix=dict(
                        dir_path=f'/mnt/mpcparis/A5/io/to_{vendor}/packages',
                        title='DASEIN PACKAGE FOR A5.',
                    ),
                    NOTRE_DAME=dict(
                        dir_path=f'/mnt/mpcparis/NOTRE_DAME/io/to_{vendor}/packages',
                        title='DASEIN PACKAGE FOR NOTRE_DAME.',
                    ),
                    Greek_Salad=dict(
                        dir_path=f'/mnt/mpcparis/Greek_Salad/io/to_{vendor}/packages',
                        title='DASEIN PACKAGE FOR Greek_Salad.',
                    ),
                    DOGMAN=dict(
                        dir_path=f'/mnt/mpcparis/DOGMAN/io/to_{vendor}/packages',
                        title='DASEIN PACKAGE FOR DOGMAN.',
                    ),
                    WONDERMAN=dict(
                        dir_path=f'/mnt/mpcparis/WONDERMAN/io/to_{vendor}/packages',
                        title='DASEIN PACKAGE FOR WONDERMAN.',
                    ),
                    MARINET=dict(
                        dir_path=f'/mnt/mpcparis/MARINET/io/to_{vendor}/packages',
                        title='DASEIN PACKAGE FOR MARINET.',
                    ),
                    ECODLAIR=dict(
                        dir_path=f'/mnt/mpcparis/ECODLAIR/IO/to_{vendor}/packages',
                        title='DASEIN PACKAGE FOR ECODLAIR.',
                    ),
                    LATRESSE=dict(
                        dir_path=f'/mnt/mpcparis/LATRESSE/IO/to_{vendor}/packages',
                        title='DASEIN PACKAGE FOR LATRESSE.',
                    ),
                    LABETE=dict(
                        dir_path=f'/mnt/mpcparis/LABETE/IO/to_{vendor}/packages',
                        title='DASEIN PACKAGE FOR LABETE.',
                    ),
                    LGO=dict(
                        dir_path=f'/mnt/mpcparis/LGO/io/to_{vendor}/packages',
                        title='DASEIN PACKAGE FOR LGO.',
                    ),
                    PED=dict(
                        dir_path=f'/mnt/pb6/Primary/PED/io/to_{vendor}/packages',
                        title='DASEIN PACKAGE FOR LGO.',
                    ),
                    test=dict(
                        dir_path=f'/mnt/mpcparis/tesr/io/to_{vendor}/packages',
                        title='DASEIN PACKAGE FOR NOTRE_DAME.',
                    ),
                ),
                vendor='dasein',
                pkg_version_padding=4,
                pkg_version_prefix='v',
            ),
            filmgate=dict(
                job=dict(
                    TRM=dict(
                        dir_path=f'/mnt/pb6/Filmgate/TRM/io/to_{vendor}/Package',
                        title='DASEIN PACKAGE FOR TRM.',
                    ),
                    KILL=dict(
                        dir_path=f'/mnt/pb6/Filmgate/KILL/io/to_{vendor}/Package',
                        title='DASEIN PACKAGE FOR KILL.',
                    ),
                    Boderland=dict(
                        dir_path=f'/mnt/pb6/Filmgate/Boderland/io/to_{vendor}/Package',
                        title='DASEIN PACKAGE FOR Boderland.',
                    ),
                ),
                vendor='DASEIN',
                pkg_version_padding=4,
                pkg_version_prefix='v',
            )
        )
    )
    return vendor_global_config


