bl_info = {
    "name": "Velocity NLA",
    "blender": (4, 0, 0),
    "category": "Object",
    "version": (0, 1),
    "author": "DJDJDJDJD KALED",
    "description": "Add velocity to animation",
}

import bpy

def update_remap(self, context):
    # Toggle the velocity_enabled property to trigger update
    bpy.context.scene.velocity_enabled = not bpy.context.scene.velocity_enabled
    bpy.context.scene.velocity_enabled = not bpy.context.scene.velocity_enabled

class OBJECT_OT_add_to_velo(bpy.types.Operator):
    """Add Action to NLA Track and Add Driver"""
    bl_idname = "object.add_to_velo"
    bl_label = "Add to Velo"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        try:
            # Iterate over all selected objects
            for obj in context.selected_objects:
                # Ensure the object has animation data
                if obj.animation_data and obj.animation_data.action:
                    action = obj.animation_data.action

                    # Create a new NLA track
                    nla_track = obj.animation_data.nla_tracks.new()

                    # Calculate the start and end frames of the action
                    start_frame = int(action.frame_range[0])
                    end_frame = int(action.frame_range[1])

                    # Create a new NLA strip using the action
                    nla_strip = nla_track.strips.new(action.name, start_frame, action)
                    nla_strip.frame_end = end_frame

                    # Clear the current action from the object
                    obj.animation_data.action = None

                    # Add driver to NLA strip
                    nla_strip.use_animated_time = True
                    fcurve = nla_strip.driver_add("strip_time")
                    driver = fcurve.driver
                    driver.type = 'SCRIPTED'
                    var = driver.variables.new()
                    var.name = "remap"
                    var.type = 'SINGLE_PROP'
                    target = var.targets[0]
                    target.id_type = 'SCENE'
                    target.id = bpy.context.scene
                    target.data_path = "remap"
                    driver.expression = "remap"

                    # Optional: Print some information to the console
                    self.report({'INFO'}, f"Added {action.name} to NLA with driver for {obj.name}")
                    print(f"Added {action.name} to NLA with driver for {obj.name}")

            print("Add to Velo executed")
            return {'FINISHED'}
        except Exception as e:
            print("Error executing operator:", e)
            return {'CANCELLED'}

def update_velocity_enabled(self, context):
    if self.velocity_enabled:
        for obj in bpy.data.objects:
            if obj.animation_data:
                for track in obj.animation_data.nla_tracks:
                    for strip in track.strips:
                        strip.use_animated_time = True
                        print("NLA Strip animated time enabled for:", strip.name)
    else:
        for obj in bpy.data.objects:
            if obj.animation_data:
                for track in obj.animation_data.nla_tracks:
                    for strip in track.strips:
                        strip.use_animated_time = False
                        print("NLA Strip animated time disabled for:", strip.name)

class VelocityPanel(bpy.types.Panel):
    """Creates a Panel in the Tool Shelf of the 3D View"""
    bl_label = "Velocity"
    bl_idname = "VIEW3D_PT_velocity"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        layout.prop(scene, "velocity_enabled", text="Enable Velocity")
        layout.prop(scene, "remap", text="Remap")

        row = layout.row()
        row.scale_y = 2.0
        row.operator("object.add_to_velo", text="Add to Velo")

def register():
    bpy.utils.register_class(VelocityPanel)
    bpy.utils.register_class(OBJECT_OT_add_to_velo)
    bpy.types.Scene.velocity_enabled = bpy.props.BoolProperty(
        name="Enable Velocity",
        description="Enable or disable velocity",
        default=False,
        update=update_velocity_enabled
    )
    bpy.types.Scene.remap = bpy.props.FloatProperty(
        name="Remap",
        description="Remap the strip time",
        default=1.0,
        min=0.0,
        max=5000.0,
        update=update_remap
    )

def unregister():
    bpy.utils.unregister_class(VelocityPanel)
    bpy.utils.unregister_class(OBJECT_OT_add_to_velo)
    del bpy.types.Scene.velocity_enabled
    del bpy.types.Scene.remap

if __name__ == "__main__":
    register()
