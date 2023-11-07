import os
import fileseq
__name = 'upload to s3 bucket'

def run(**data):
    s3_root = 's3://dsvfx-sitw-editorial/main/from_dasein'
    print(data)
    for file_data in data['files']:
        source_path = file_data['source_path']

        # print(fileseq.FileSequence(source_path)
        pkg_dir = file_data['pkg_dir']
        ext = os.path.splitext(source_path)[-1][1:]
        # print(ext)
        if ext not in ['mov', 'mp4']:
            continue
        destination_path = file_data['destination_path']
        # print(destination_path)
        # print(pkg_dir)
        s3_destination_path = destination_path.replace(pkg_dir, s3_root)
        if not s3_destination_path.startswith(s3_root):
            continue
        # print(1111111111)
        # print(s3_destination_path)
        cmd = f'aws s3 cp {source_path} {s3_destination_path}'
        # print(cmd)
        os.system(cmd)

    return 0, {
        'info': '', 
        'return_data': {}
    }


if __name__ == '__main__':
    data = {'pkg_dir': '/mnt/sitw/io/to_client', 'shot': '014hot_0010', 'discipline': 'comp', 'source_path': '/mnt/sitw/movs/shots/test/014hot_0010_comp_v1@@@.mov'}
    run(**data)



