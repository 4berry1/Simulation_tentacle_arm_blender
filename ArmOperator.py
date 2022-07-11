import bpy
import time
import os, sys
sys.path.append( 'BlenderProject/' )
import test
from bpy.props import IntProperty, FloatProperty


class ModalOperator(bpy.types.Operator):
    """Move an object with the mouse, example"""
    bl_idname = "object.modal_operator_input"
    bl_label = "Tentacle Arm Operator"
    bl_options = {'REGISTER'}

    first_mouse_x: IntProperty() # test items to see if modal works
    first_value: FloatProperty() 
    
    # created variables for the class
    finalp = [-.07,-.01,-.094784]
    startp = [-.47438,.010361,-.84285]
    X = 0
    Y = 0
    Z = 0
    Tdir = -1
    grab = 0

    def modal(self, context, event):
        if event.type == 'ESC':     # if escape key pressed exit program
            context.window_manager.event_timer_remove(self.timer)
            return {'FINISHED'}
        elif event.type == 'R':     # if r is pressed reset
            test.reset()
            finalp = [-.07,-.01,-.094784]
            startp = [-.47438,.010361,-.84285]
            X = 0
            Y = 0
            Z = 0
        elif event.type == 'S':     # if S is pressed send data to output file
            self.grab = 0
            finalp = [float(test.bone3.location.x) , float(test.bone3.location.y) ,float(test.bone3.location.z)]
            test.OutputTest(float(test.bone3.location.x) , float(test.bone3.location.y) ,float(test.bone3.location.z))
        elif event.type == 'G':     # if G is pressed stop input coords for user to move around the arm
            if (self.grab == 0):
                startp = [float(test.bone3.location.x) , float(test.bone3.location.y) ,float(test.bone3.location.z)]
            self.grab = 1
            return {'PASS_THROUGH'}
        else:                       # else update arm position with coords from file

            finalp = test.GetFinalp()
            startp = [-.47438,.010361,-.84285]
            if (self.grab == 0):
                if ((self.X <= startp[0] and startp[0] < finalp[0]) or (self.X <= finalp[0] and startp[0] > finalp[0])): 
                     self.Tdir = 1
                if ((self.X >= startp[0] and startp[0] > finalp[0]) or (self.X >= finalp[0] and startp[0] < finalp[0])):
                    self.Tdir = -1
                
                self.X+= ((finalp[0] - startp[0])/ 300.0)* self.Tdir
                self.Y+= ((finalp[1] - startp[1])/ 300.0)* self.Tdir
                self.Z+= ((finalp[2] - startp[2])/ 300.0)* self.Tdir
                test.CreateTest(self.X,self.Y,self.Z)
                test.RunTestFile()
            return {'PASS_THROUGH'}
            
            

        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        if context.object:
            self.timer = context.window_manager.event_timer_add(.01, window=context.window)
            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}
        else:
            self.report({'WARNING'}, "No active object, could not finish")
            context.window_manager.event_timer_remove(self.timer)
            return {'CANCELLED'}

def menu_func(self, context):
    self.layout.operator(ModalOperator.bl_idname, text=ModalOperator.bl_label)

# Register and add to the "view" menu (required to also use F3 search "Simple Modal Operator" for quick access)
def register():
    bpy.utils.register_class(ModalOperator)
    bpy.types.VIEW3D_MT_object.append(menu_func)


def unregister():
    context.window_manager.event_timer_remove(self.timer)
    bpy.utils.unregister_class(ModalOperator)
    bpy.types.VIEW3D_MT_object.remove(menu_func)


if __name__ == "__main__":
    register()

    # test call


