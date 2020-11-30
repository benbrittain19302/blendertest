import bpy
import math
import random
import os

bpy.ops.object.select_all(action='DESELECT')
for obj in bpy.data.objects:
    if obj.type == 'MESH':
        obj.select_set(True)
bpy.ops.object.delete()

def create_cube(name, position, scale):
    bpy.ops.mesh.primitive_cube_add()
    cube = bpy.context.selected_objects[0]
    cube.name = name
    cube.location = position
    cube.scale = scale
    
"""
create_cube("floor",[0,0,0],[10,10,.1])

for x in range(10):
    if x % 2 == 0:    
        create_cube("stair",[0,x,1+(x/2)],[3,1,1+(x/2)])
           
        
for env in os.environ:
    print(env)
"""
path = 'export/myfile.obj'
bpy.ops.import_scene.obj(filepath=path)
obj = bpy.context.selected_objects[0]


 
 
 
 