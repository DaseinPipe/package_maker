import os
__name = 'upload to s3 bucket'

def run(**data):
    s3_root = 's3://dsvfx-sitw-editorial/main/to_dasein'
    print(data)
    for file_data in data['files']:
        source_path = file_data['source_path']
        pkg_dir = file_data['pkg_dir']
        ext = os.path.splitext(source_path)[-1][1:]
        print(ext)
        if ext not in ['mov', 'mp4']:
            continue
        destination_path = file_data['destination_path']
        print(destination_path)
        print(pkg_dir)
        s3_destination_path = destination_path.replace(pkg_dir, s3_root)
        if not s3_destination_path.startswith(s3_root):
            continue
        print(1111111111)
        print(s3_destination_path)
        cmd = f'aws s3 cp {source_path} {s3_destination_path}'
        print(cmd)
        os.system(cmd)

    return 0, {
        'info': '', 
        'return_data': {}
    }


if __name__ == '__main__':
    data = {'discipline': 'paint', 'files': [{'source_path': '/mnt/sitw/editorial/exports/230217_SITW_VFX_LIST_2_Uel_Dasein_VFX_mos_CLEAN/001air_0030_list2Clean.mp4', 'ext': 'mp4', 'shot_version_num': '004', 'shot_version_prefix': 'v', 'shot': '001air_0030', 'pkg_dir_type': 'seq_filepath', 'filename': '001air_0030_list2Clean.mp4', 'pkg_version': '1', 'pkg_type': 'shot', 'job': 'sitw', 'discipline': 'paint', 'date': '2023_04_20', 'vendor': 'dasein', 'show': 'sitw', 'pkg_version_prefix': 'send_', 'pkg_version_num': '02', 'pkg_dir': '/mnt/sitw/io/to-sitw', 'pkg_for': 'client', 'vendor_name': 'UNKNOWN', 'destination_path': '/mnt/sitw/io/to-sitw/2023_04_20/SITW_dasein_2023_04_20_send_02/001air_0030/4448 x 3096/001air_0030_v004.UNKNOWN.mp4'}], 'date': '2023_04_20', 'vendor': 'dasein', 'show': 'sitw', 'pkg_version_prefix': 'send_', 'pkg_version_num': '02', 'pkg_dir': '/mnt/sitw/io/to-sitw', 'pkg_for': 'client', 'vendor_name': 'UNKNOWN', 'pkg_type': 'shot', 'update_sitw_db': {'info': '', 'return_data': {}}, 'make_nonseq_link': {'info': '', 'return_data': {}}, 'make_seq_link': {'info': '', 'return_data': {}}}
    run(**data)



