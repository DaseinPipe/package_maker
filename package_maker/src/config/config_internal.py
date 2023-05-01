
import os
__config_folder_path = os.path.dirname(os.path.realpath(__file__))

PACKAGE_FOR_LIST = [
    'Select',
    'Scan',
]


CLIENT_LIST = [
    'mpc',
    'filmgate'
]


def internal_config_data():
    return dict(
        job=dict(
            LABETE=dict(
                dir_path=f'/mnt/mpcparis/LABETE',
            ),
            PED=dict(
                dir_path=f'/mnt/pb6/Primary/PED',
            ),
            sitw = dict(
                dir_path=f'/mnt/sitw',
            )
        ),
    )



