import lucidity
from package_maker.src.config.py.ecodlair_nomenclature import *

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
    '{@global_pkg_dir}/{@local_pkg_name}',
    anchor=lucidity.Template.ANCHOR_END,
    template_resolver=resolver
)

for_approval_dir = lucidity.Template(
    'for_approval_dir',
    '{@shot_pkg_dir}/for_approval/{@workfile_name}',
    anchor=lucidity.Template.ANCHOR_END,
    template_resolver=resolver
)

element_dir = lucidity.Template(
    'element_dir',
    '{@shot_pkg_dir}/element/{@workfile_name}',
    anchor=lucidity.Template.ANCHOR_END,
    template_resolver=resolver
)


workfile_filepath_template = lucidity.Template(
    'workfile',
    '{@shot_pkg_dir}/workfile/{@workfile_name}.{ext}',
    anchor=lucidity.Template.ANCHOR_END,
    template_resolver=resolver
)

for_approval_filepath_template = lucidity.Template(
    'for_approval_filepath',
    '{@for_approval_dir}/{@seq_file_name}.{ext}',
    anchor=lucidity.Template.ANCHOR_END,
    template_resolver=resolver
)


element_filepath_template = lucidity.Template(
    'element_filepath',
    '{@element_dir}/{@seq_file_name}.{ext}',
    anchor=lucidity.Template.ANCHOR_END,
    template_resolver=resolver
)


resolver_target_list = [GLOBAL_PKG_NAME, LOCAL_PKG_NAME, WORKFILE_NAME, SEQ_FILE_NAME,
                        main_pkg_dir, global_pkg_dir, shot_pkg_dir, for_approval_dir,
                        element_dir,
]


for each_target in resolver_target_list:
    resolver[each_target.name] = each_target
