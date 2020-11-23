import bpy
import math
import random

def create_cube(name, position, scale, rotateB):
    bpy.ops.mesh.primitive_cube_add()
    cube = bpy.context.selected_objects[0]
    cube.name = name
    cube.location = position
    cube.scale = scale
    if rotateB:
        cube.rotation_euler = [math.radians(random.randint(10,30)),math.radians(random.randint(10,30)),math.radians(random.randint(10,30))]
    
create_cube("floor",[0,0,0],[10,10,.1], False)

for x in range(10):
    if x % 2 == 0:    
        create_cube("stair",[0,x,1+(x/2)],[3,1,1+(x/2)], True)

 
 
 
 