bl_info = {
    "name": "Quick Join",
    "description": "This addon allows you to quickly join selected objects together, remove duplicate vertices, and assign the joined mesh the name of the last selected object.",
    "author": "F1dg3t",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Sidebar > Quick Join",
    "category": "Object",
}

import bpy


# Define the custom panel class
class QuickJoinPanel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_quick_join"
    bl_label = "Quick Join"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Quick Join'

    # Draw the panel
    def draw(self, context):
        layout = self.layout
        scene = context.scene

        # Add the description text
        layout.label(text="Join selected objects and remove duplicates:")
        layout.label(text="Made by F1dg3tXD")

        # Add a button to execute the join operation
        layout.operator("object.quick_join", text="Join Selected Objects")

# Define the operator class for the join operation
class OBJECT_OT_quick_join(bpy.types.Operator):
    bl_idname = "object.quick_join"
    bl_label = "Join Selected Objects"

    def execute(self, context):
        # Get the selected objects
        selected_objects = bpy.context.selected_objects

        # Check if there are at least two objects selected
        if len(selected_objects) < 2:
            self.report({'WARNING'}, "Please select at least two objects to join.")
            return {'CANCELLED'}

        # Select the active object (the first selected object)
        bpy.context.view_layer.objects.active = selected_objects[0]

        # Join the selected objects
        bpy.ops.object.join()

        # Enter edit mode
        bpy.ops.object.mode_set(mode='EDIT')

        # Select all vertices
        bpy.ops.mesh.select_all(action='SELECT')

        # Remove duplicate vertices
        bpy.ops.mesh.remove_doubles()

        # Exit edit mode
        bpy.ops.object.mode_set(mode='OBJECT')

        # Rename the joined object with the name of the last selected object
        joined_object = bpy.context.active_object
        last_selected_object = selected_objects[-1]
        joined_object.name = last_selected_object.name

        return {'FINISHED'}

# Register the panel and operator
def register():
    bpy.utils.register_class(QuickJoinPanel)
    bpy.utils.register_class(OBJECT_OT_quick_join)

def unregister():
    bpy.utils.unregister_class(QuickJoinPanel)
    bpy.utils.unregister_class(OBJECT_OT_quick_join)

# Run the registration
if __name__ == "__main__":
    register()
