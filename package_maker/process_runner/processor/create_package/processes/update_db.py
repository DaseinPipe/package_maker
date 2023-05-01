from package_maker.src.utils.general_utils import update_shot_version

__name = 'create client package'

def run(**data):
    print(data)
    update_shot_version(data)
    return 0, {
        'info': '', 
        'return_data': {}
    }


