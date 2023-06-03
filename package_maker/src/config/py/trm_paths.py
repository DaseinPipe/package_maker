import lucidity
from package_maker.src.config.py.trm_nomenclature import *

resolver = {}

main_pkg_dir = lucidity.Template(
    'main_pkg_dir',
    '{pkg_dir}/PKG-{@global_pkg_name}-package',
    anchor=lucidity.Template.ANCHOR_END,
    template_resolver=resolver
)

global_pkg_dir = lucidity.Template(
    'global_pkg_dir',
    '{@main_pkg_dir}/{@global_pkg_name}',
    anchor=lucidity.Template.ANCHOR_END,
    template_resolver=resolver
)



shot_pkg_dir = lucidity.Template(
    'shot_pkg_dir',
    '{@global_pkg_dir}/{@shot_pkg_name}',
    anchor=lucidity.Template.ANCHOR_END,
    template_resolver=resolver
)

for_approval_dir = lucidity.Template(
    'for_approval_dir',
    '{@shot_pkg_dir}/sequence',
    anchor=lucidity.Template.ANCHOR_END,
    template_resolver=resolver
)


workfile_filepath_template = lucidity.Template(
    'workfile',
    '{@shot_pkg_dir}/nuke_script/{@workfile_name}',
    anchor=lucidity.Template.ANCHOR_END,
    template_resolver=resolver
)


for_approval_filepath_template = lucidity.Template(
    'for_approval_filepath',
    '{@for_approval_dir}/{@seq_file_name}',
    anchor=lucidity.Template.ANCHOR_END,
    template_resolver=resolver
)

vendor_discipline_folder_template = lucidity.Template(
    'vendor_discipline_folder',
    '{pkg_dir}/{@vendor_shot_pkg_name}/{discipline}',
    anchor=lucidity.Template.ANCHOR_END,
    template_resolver=resolver
)

resolver_target_list = [
    GLOBAL_PKG_NAME, LOCAL_PKG_NAME, SHOT_PKG_NAME, SEQ_FILE_NAME,
    WORKFILE_NAME,VENDOR_SHOT_PKG_NAME, main_pkg_dir, global_pkg_dir, 
    shot_pkg_dir, for_approval_dir, vendor_discipline_folder_template
]

for each_target in resolver_target_list:
    resolver[each_target.name] = each_target
