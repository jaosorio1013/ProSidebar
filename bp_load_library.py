import bpy
from .bp_utils import utils_library
from bpy.app.handlers import persistent

@persistent
def load_library_on_file_load(scene=None):
    utils_library.update_props_from_xml_file()
    utils_library.get_script_libraries()

def register():
    bpy.app.handlers.load_post.append(load_library_on_file_load)

def unregister():
    bpy.app.handlers.load_post.remove(load_library_on_file_load)  