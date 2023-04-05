from package_maker.src.utils import mpc_utils, filmgate_utils


def get_global_pkg_data(job, destination, pkg_dir, pkk_for, vendor_name):
    return dict(
        asterix=mpc_utils.global_pkg_data(job, destination, pkg_dir, pkk_for, vendor_name),
        trm=filmgate_utils.global_pkg_data(job, destination, pkg_dir, pkk_for, vendor_name),
        kill=filmgate_utils.global_pkg_data(job, destination, pkg_dir, pkk_for, vendor_name),
        boderland=filmgate_utils.global_pkg_data(job, destination, pkg_dir, pkk_for, vendor_name)
    ).get(
        job,
        mpc_utils.global_pkg_data(job, destination, pkg_dir, pkk_for, vendor_name)
    )


