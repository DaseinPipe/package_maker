from package_maker.src.utils.general_utils import update_shot_version

__name = 'create client package'

def run(**data):
    for file_data in data['files']:
        pass
        # update_shot_version(file_data)
    return 0, {
        'info': '', 
        'return_data': {}
    }


