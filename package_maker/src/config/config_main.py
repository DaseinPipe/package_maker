import yaml
import os
from package_maker.src.config.py.asterix_paths import *
from package_maker.src import stylesheets

__config_folder_path = os.path.dirname(os.path.realpath(__file__))

_stylesheets_folder_path = os.path.dirname(os.path.abspath(stylesheets.__file__))

global stylesheet_path
stylesheet_path = os.path.join(_stylesheets_folder_path,'EasyCode.qss')

global global_discipline
global_discipline = [
    'roto',
    'prep',
    'comp',
    'matchmove'
]

global global_seq_ext
global_seq_ext = [
    'exr',
    'jpg',
    'jpeg',
    'png',
    'tiff'
]
global global_work_app_config
global_work_app_config = {
    'nk': 'nuke',
    'ma': 'maya',
    'sfx': 'sfx',
    '3de': '3de',
    'abc': 'maya',
    'fbx': 'maya'
}
global global_pkg_version_padding
global_pkg_version_padding = 4

global global_pkg_version_prefix
global_pkg_version_prefix = 'ver'

global global_shot_version_padding
global_shot_version_padding = 3

global global_shot_version_prefix
global_shot_version_prefix = 'v'

global global_plate_version_padding
global_plate_version_padding = 2

global global_plate_version_prefix
global_plate_version_prefix = 'master'


global global_pkg_dir_types
global_pkg_dir_types = dict(
    camera=dict(
        match_list=['cam', 'camera', 'len'],
        ext_list=['.fbx', '.abc'],
        discipline=['matchmove'],
        ext_type='app'
    ),
    element=dict(
        match_list=['element', 'STmaps', 'map', 'plate', 'undistort', 'matte'],
        ext_list=['.exr', '.png', '.jpeg', '.tiff'],
        discipline=['prep', 'roto'],
        ext_type='image',
    ),
    for_approval=dict(
        match_list=[],
        ext_list=['.exr', '.jpg', '.jpeg', '.png', '.tiff'],
        discipline=['matchmove', 'roto', 'comp'],
        ext_type='image',
    ),
    geometry=dict(
        match_list=[],
        ext_list=['.fbx', '.abc'],
        discipline=['matchmove'],
        ext_type='app',
    ),
    workfile=dict(
        match_list=[],
        ext_list=['.nk', '.3de', '.hip', '.sfx', '.ma'],
        discipline=['roto', 'prep', 'comp', 'matchmove'],
        app_config=global_work_app_config,
        ext_type='app',
    ),
    custom={},
    select={})

global global_discipline_pkg_type_assignment
global_discipline_pkg_type_assignment=dict(
    roto=dict(
        image=dict(
            pkg_types=['element', 'for_approval'],
            ext_list=['.exr', '.jpg', '.jpeg', '.png', '.tiff'],
            default='select'
        ),
        app=dict(
            pkg_types=['workfile'],
            ext_list=['.sfx', '.nk'],
            default='workfile'
        ),
    ),
    prep=dict(
        image=dict(
            pkg_types=['element'],
            ext_list=['.exr', '.jpg', '.jpeg', '.png', '.tiff'],
            default='element'
        ),
        app=dict(
            pkg_types=['workfile'],
            ext_list=['.nk'],
            default='workfile'
        ),
    ),
    matchmove=dict(
        image=dict(
            pkg_types=['for_approval'],
            ext_list=['.exr', '.jpg', '.jpeg', '.png', '.tiff'],
            default='for_approval'
        ),
        app=dict(
            pkg_types=['camera', 'geometry'],
            ext_list=['.abc', '.fbx', '.ma', '.nk', '.3de'],
            default=['geometry', 'workfile']
        ),
    ),
    comp=dict(
        image=dict(
            pkg_types=['for_approval'],
            ext_list=['.exr', '.jpg', '.jpeg', '.png', '.tiff'],
            default='for_approval'
        ),
        app=dict(
            pkg_types=['workfile'],
            ext_list=['.nk'],
            default='workfile'
        ),
    ),
)

def asterix_config_setup():
    asterix_config = dict(
        shot=[
            "080_bb_0375",
            "082_em_0325",
            "082_em_0320",
        ],
        discipline=global_discipline,
        seq_ext=global_seq_ext,
        pkg_dir_types=global_pkg_dir_types,
        shot_version_padding=3,
        shot_version_prefix='v',
        plate_version_padding=2,
        plate_version_prefix='master'
    )
    return asterix_config


def test_config_setup():
    test_config = dict(
        shot=[
            "080_bb_0375_test",
            "082_em_0325_test",
            "082_em_0320_test",
        ],
        discipline=global_discipline,
        seq_ext=global_seq_ext,
        pkg_dir_type=global_pkg_dir_types,
        shot_version_padding=3,
        shot_version_prefix='v',
        plate_version_padding=2,
        plate_version_prefix='master'
    )
    return test_config


def global_config_setup():
    global_config = dict(
        destination=dict(
            MPC_Paris=dict(
                job=dict(
                    asterix=dict(
                        dir_path='C:/mnt/mpcparis/A5/io/To_Client/packages',
                        title='MPC PARIS PACKAGE FOR A5.',
                    ),
                    NOTRE_DAME=dict(
                        dir_path='C:/mnt/mpcparis/NOTRE_DAME/io/To_Client/packages',
                        title='MPC PARIS PACKAGE FOR NOTRE_DAME.',
                    ),
                ),
                vendor='dasein',
                pkg_version_padding=4,
                pkg_version_prefix='v',
            ),
            filmgate=dict(
                job=dict(
                    TRM=dict(
                        dir_path='/mnt/pb6/Filmgate/TRM/io/To_Client/Package',
                        title='FILMGATE PACKAGE FOR TRM.',
                    ),
                ),
                vendor='dasein',
                pkg_version_padding=4,
                pkg_version_prefix='v',
            )
        )
    )
    return global_config


def get_show_config(show):
    return dict(
        asterix=asterix_config_setup(),
        test=test_config_setup()
    ).get(show)


def global_config_exec():
    global_config_filepath = os.path.join(__config_folder_path, "yaml/global_config.yaml")
    global_config_data = global_config_setup()
    with open(global_config_filepath, 'w') as yamlfile:
        data = yaml.dump(global_config_data, yamlfile)
        print("Write successful")


def show_config_exec(show=None):
    show_config_filepath = os.path.join(__config_folder_path, f'yaml/{show}_config.yaml')
    show_config_data = get_show_config(show)
    assert show_config_data, f"can't find config function for {show}"
    with open(show_config_filepath, 'w') as yamlfile:
        data = yaml.dump(show_config_data, yamlfile)
        print("Write successful")


def get_global_data():
    global_config_filepath = os.path.join(__config_folder_path, "yaml/global_config.yaml")
    with open(global_config_filepath, "r") as yamlfile:
        return yaml.load(yamlfile, Loader=yaml.FullLoader)


def get_show_data(show: object) -> object:
    if not show:
        return {}
    show_config_filepath = os.path.join(__config_folder_path, f'yaml/{show}_config.yaml')
    with open(show_config_filepath, "r") as yamlfile:
        return yaml.load(yamlfile, Loader=yaml.FullLoader)


if __name__ == '__main__':
    show_list = ['asterix', 'test']
    global_config_exec()
    for show in show_list:  show_config_exec(show)
