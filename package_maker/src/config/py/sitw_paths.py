import lucidity
from package_maker.src.config.py.sitw_nomenclature import *

resolver = {}

main_pkg_dir = lucidity.Template(
    'main_pkg_dir',
    '{pkg_dir}/{date}',
    anchor=lucidity.Template.ANCHOR_END,
    template_resolver=resolver
)

global_pkg_dir = lucidity.Template(
    'global_pkg_dir',
    '{@main_pkg_dir}/{@global_pkg_name}',
    anchor=lucidity.Template.ANCHOR_END,
    template_resolver=resolver
)

local_pkg_dir = lucidity.Template(
    'local_pkg_dir',
    '{pkg_dir}/{discipline}/shot',
    anchor=lucidity.Template.ANCHOR_END,
    template_resolver=resolver
)

shot_pkg_dir = lucidity.Template(
    'shot_pkg_dir',
    '{@global_pkg_dir}',
    anchor=lucidity.Template.ANCHOR_END,
    template_resolver=resolver
)


seq_filepath = lucidity.Template(
    'seq_filepath',
    '{@shot_pkg_dir}/{@seq_filename}/4448 x 3096/{@seq_filename}.{ext}',
    anchor=lucidity.Template.ANCHOR_END,
    template_resolver=resolver
)


final_mov_filepath = lucidity.Template(
    'final_mov_filepath',
    '{@shot_pkg_dir}/{@final_mov_filename}',
    anchor=lucidity.Template.ANCHOR_END,
    template_resolver=resolver
)

mov_filepath = lucidity.Template(
    'mov_filepath',
    '{@shot_pkg_dir}/{@mov_filename}',
    anchor=lucidity.Template.ANCHOR_END,
    template_resolver=resolver
)



resolver_target_list = [GLOBAL_PKG_NAME, LOCAL_PKG_NAME, SEQ_FILE_NAME, MOV_FILENAME, FINAL_MOV_FILENAME,
                        main_pkg_dir, global_pkg_dir, shot_pkg_dir, seq_filepath, final_mov_filepath,
                        mov_filepath, local_pkg_dir

]


for each_target in resolver_target_list:
    resolver[each_target.name] = each_target
