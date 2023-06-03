from pathlib import Path
from package_maker.src.config.config_vendor import CLIENT_LIST

__name = 'make seq symbolic link'

def rename_dir(path, src, dst):
    parts = list(path.parts)
    parts[parts.index(src)] = dst
    return Path(*parts)

def run(**data):
    for file_data in data['files']:
        destination_path = Path(file_data['destination_path'])
        destination_folder = destination_path.name
        client_name = None
        for each in CLIENT_LIST:
            if each in destination_folder:
                client_name = each
                break
        if client_name:
            new_destination_folder = destination_folder.replace(client_name, data['vendor'])
            new_destination_path = rename_dir(destination_path, destination_folder, new_destination_folder)
            destination_path.rename(new_destination_path)

    return 0, {
        'info': '',
        'return_data': {}
    }


if __name__ == '__main__':
    data = {'shot': '', 'files': [{'source_path': '/mnt/mpcparis/LGO/io/from_client/PKG-20230328-mpc-lgo-v0073_to_dasein/20230328-mpc-lgo-v0073/shot-006_040-prep-base-mpc-v001', 'destination_path': '/mnt/mpcparis/LGO/io/to_shakti/packages/PKG-20230401-dasein-lgo-v0003-package/20230401-dasein-lgo-v0003/shot-006_040-prep-base-mpc-v001'}, {'source_path': '/mnt/mpcparis/LGO/io/from_client/PKG-20230328-mpc-lgo-v0073_to_dasein/20230328-mpc-lgo-v0073/shot-006_030-prep-base-mpc-v001', 'destination_path': '/mnt/mpcparis/LGO/io/to_shakti/packages/PKG-20230401-dasein-lgo-v0003-package/20230401-dasein-lgo-v0003/shot-006_030-prep-base-mpc-v001'}, {'source_path': '/mnt/mpcparis/LGO/io/from_client/PKG-20230328-mpc-lgo-v0073_to_dasein/20230328-mpc-lgo-v0073/shot-006_020-prep-base-mpc-v001', 'destination_path': '/mnt/mpcparis/LGO/io/to_shakti/packages/PKG-20230401-dasein-lgo-v0003-package/20230401-dasein-lgo-v0003/shot-006_020-prep-base-mpc-v001'}], 'date': '20230401', 'vendor': 'dasein', 'show': 'lgo', 'pkg_version_prefix': 'v', 'pkg_version_num': '0003', 'pkg_dir': '/mnt/mpcparis/LGO/io/to_shakti/packages', 'pkg_for': 'vendor', 'vendor_name': 'Shakti'}
    run(data)