import yaml
import os

from package_maker.src import stylesheets

__config_folder_path = os.path.dirname(os.path.realpath(__file__))
import importlib
_stylesheets_folder_path = os.path.dirname(os.path.abspath(stylesheets.__file__))


stylesheet_path = os.path.join(_stylesheets_folder_path,'EasyCode.qss')

UNKNOWN = 'UNKNOWN'

global_discipline = [
    'roto',
    'prep',
    'comp',
    'matchmove'
]


global_seq_ext = [
    'exr',
    'jpg',
    'jpeg',
    'png',
    'tiff'
]

global_work_app_config = {
    'nk': 'nuke',
    'ma': 'maya',
    'sfx': 'sfx',
    '3de': '3de',
    'abc': 'maya',
    'fbx': 'maya'
}


global_pkg_version_padding = 4


global_pkg_version_prefix = 'v'


global_shot_version_padding = 3


global_shot_version_prefix = 'v'


global_plate_version_padding = 2


global_plate_version_prefix = 'master'



global_pkg_dir_types = dict(
    camera=dict(
        match_list=['cam', 'camera', 'len'],
        ext_list=['.fbx', '.abc'],
        discipline=['matchmove'],
        ext_type='app'
    ),
    element=dict(
        match_list=[
            'element', 'STmaps', 'map', 'plate',
            'undistort', 'matte']
        ,
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
    return dict(
        discipline=global_discipline,
        seq_ext=global_seq_ext,
        pkg_dir_types=global_pkg_dir_types,
        shot_version_padding=3,
        shot_version_prefix='v',
        plate_version_padding=2,
        plate_version_prefix='master'
    )

def greek_salad_config_setup():
    return dict(
        discipline=global_discipline,
        seq_ext=global_seq_ext,
        pkg_dir_types=global_pkg_dir_types,
        shot_version_padding=4,
        shot_version_prefix='v',
        plate_version_padding=2,
        plate_version_prefix='master'
    )


def trm_config_setup():
    return dict(
        discipline=[
            'Animation', 'BG_plates', 'Cleanup', 'Lighting', 'comp',
            'Matchmoving', 'Matte_painting', 'Plates', 'Rotoscoping'
        ],
        seq_ext=global_seq_ext,
        shot_version_padding=4,
        shot_version_prefix='v',
        plate_version_padding=2,
        plate_version_prefix='master',
        episode_name_regex=r'ep\d{2}-rl\d{2}',
        shot_no_regex=r'\d{5}',
        shot_name_regex=r'ep\d{2}-rl\d{2}_\d{5}'
    )

def notre_dame_config_setup():
    return dict(
        discipline=global_discipline,
        seq_ext=global_seq_ext,
        pkg_dir_types=global_pkg_dir_types,
        shot_version_padding=3,
        shot_version_prefix='v',
        plate_version_padding=2,
        plate_version_prefix='master'
    )


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
                        dir_path='/mnt/mpcparis/A5/io/To_Client/packages',
                        title='MPC PARIS PACKAGE FOR A5.',
                    ),
                    NOTRE_DAME=dict(
                        dir_path='/mnt/mpcparis/NOTRE_DAME/io/To_Client/packages',
                        title='MPC PARIS PACKAGE FOR NOTRE_DAME.',
                    ),
                    Greek_Salad=dict(
                        dir_path='/mnt/mpcparis/Greek_Salad/io/to_client/packages',
                        title='MPC PARIS PACKAGE FOR Greek_Salad.',
                    ),
                    test=dict(
                        dir_path='/mnt/mpcparis/tesr/io/To_Client/packages',
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
        test=test_config_setup(),
        trm=trm_config_setup(),
        notre_dame=notre_dame_config_setup(),
        Greek_Salad=greek_salad_config_setup(),
    ).get(show)


def global_config_exec():
    global_config_filepath = os.path.join(__config_folder_path, "yaml/global_config.yaml")
    global_config_data = global_config_setup()
    with open(global_config_filepath, 'w') as yamlfile:
        data = yaml.dump(global_config_data, yamlfile)
        print("Write successful")


def show_config_exec(show):
    show_config_filepath = os.path.join(__config_folder_path, f'yaml/{show.lower()}_config.yaml')
    show_config_data = get_show_config(show)
    with open(show_config_filepath, 'w') as yamlfile:
        data = yaml.dump(show_config_data, yamlfile)
        print("Write successful")


def get_global_data():
    global_config_filepath = os.path.join(__config_folder_path, "yaml/global_config.yaml")
    with open(global_config_filepath, "r") as yamlfile:
        return yaml.load(yamlfile, Loader=yaml.FullLoader)


def get_show_data(show):
    if not show:
        return {}
    show = show.lower()
    show_config_filepath = os.path.join(__config_folder_path, f'yaml/{show}_config.yaml')
    with open(show_config_filepath, "r") as yamlfile:
        return yaml.load(yamlfile, Loader=yaml.FullLoader)

def get_path(job, attr):
    job = job.lower()
    show_config = f'package_maker.src.config.py.{job}_paths'
    path_config = importlib.import_module(show_config)
    return path_config.__getattribute__(attr)

def get_nomenclature(job, attr):
    show_config = f'package_maker.src.config.py.{job}_nomenclature'
    nomenclature_config = importlib.import_module(show_config)
    return nomenclature_config.__getattribute__(attr)


if __name__ == '__main__':

    show_list = ['asterix', 'test', 'trm', 'notre_dame', 'Greek_Salad']
    global_config_exec()
    for show in show_list:  show_config_exec(show)
