
from package_maker.src.core import for_approval, workfile, geometry, camera, element, custom


def get_for_approval_info(file_data):
    for_approval_obj = for_approval.ForApproval(file_data)
    return for_approval_obj.path_data, for_approval_obj.destination_path


def get_camera_info(file_data):
    camera_obj = camera.Camera(file_data)
    return camera_obj.path_data, camera_obj.destination_path


def get_element_info(file_data):
    print(file_data)
    element_obj = element.Element(file_data)
    return element_obj.path_data, element_obj.destination_path


def get_geometry_info(file_data):
    geometry_obj = geometry.Geomerty(file_data)
    return geometry_obj.path_data, geometry_obj.destination_path


def get_workfile_info(file_data):
    workfile_obj = workfile.Workfile(file_data)
    return workfile_obj.path_data, workfile_obj.destination_path

def get_custom_info(file_data):
    custom_obj = custom.Custom(file_data)
    return custom_obj.path_data, custom_obj.destination_path


def get_select_info(file_data):
    return {}, ''


def get_destination_info(pkg_dir_type, file_data):
    return dict(
        camera=get_camera_info,
        element=get_element_info,
        for_approval=get_for_approval_info,
        geometry=get_geometry_info,
        workfile=get_workfile_info,
        custom=get_custom_info,
        select=get_select_info
    ).get(pkg_dir_type)(file_data)
