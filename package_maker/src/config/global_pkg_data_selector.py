from package_maker.src.utils import mpc_utils, filmgate_utils


def get_global_pkg_data(job, destination, pkg_dir):
    return dict(
        asterix=mpc_utils.global_pkg_data(job, destination, pkg_dir),
        trm=filmgate_utils.global_pkg_data(job, destination, pkg_dir),
        kill=filmgate_utils.global_pkg_data(job, destination, pkg_dir),
        boderland=filmgate_utils.global_pkg_data(job, destination, pkg_dir)
    ).get(
        job,
        mpc_utils.global_pkg_data(job, destination, pkg_dir)
    )
