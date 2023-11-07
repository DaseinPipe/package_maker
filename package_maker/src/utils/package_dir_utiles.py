
from package_maker.src.core import for_approval, workfile, geometry, camera, element, custom
from package_maker.src.core.sitw import seq, final_mov, mov



def get_for_approval_info(file_data):
    for_approval_obj = for_approval.ForApproval(file_data)
    return for_approval_obj.path_data, for_approval_obj.destination_path


def get_camera_info(file_data):
    camera_obj = camera.Camera(file_data)
    return camera_obj.path_data, camera_obj.destination_path


def get_element_info(file_data):
    # print(file_data)
    element_obj = element.Element(file_data)
    return element_obj.path_data, element_obj.destination_path


def get_geometry_info(file_data):
    geometry_obj = geometry.Geomerty(file_data)
    return geometry_obj.path_data, geometry_obj.destination_path


def get_workfile_info(file_data):
    workfile_obj = workfile.Workfile(file_data)
    # print(workfile_obj)
    return workfile_obj.path_data, workfile_obj.destination_path

def get_custom_info(file_data):
    custom_obj = custom.Custom(file_data)
    return custom_obj.path_data, custom_obj.destination_path


def get_select_info(file_data):
    return {}, ''

def get_mov_filepath(file_data):
    mov_obj = mov.Mov(file_data)
    return mov_obj.path_data, mov_obj.destination_path


def get_final_mov_filepath(file_data):
    final_mov_obj = final_mov.FinalMov(file_data)
    return final_mov_obj.path_data, final_mov_obj.destination_path

def get_seq_filepath(file_data):
    seq_obj = seq.Seq(file_data)
    return seq_obj.path_data, seq_obj.destination_path

def get_destination_info(pkg_dir_type, file_data):
    return dict(
        camera=get_camera_info,
        element=get_element_info,
        for_approval=get_for_approval_info,
        geometry=get_geometry_info,
        workfile=get_workfile_info,
        custom=get_custom_info,
        select=get_select_info,
        mov_filepath=get_mov_filepath,
        final_mov_filepath=get_final_mov_filepath,
        seq_filepath=get_seq_filepath
    ).get(pkg_dir_type)(file_data)
