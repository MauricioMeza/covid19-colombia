""" ------------------------------------------------------------------------
-------------- Take formated, sorted, 0ed data -----------------------------
------------- create 3D visualization in blender  --------------------------
------------------------------------------------------------------------ """

"""Only Works inside blender SOFTWARE with the Blender python API bpy"""
import bpy
import json
import math
from mathutils import Color

with open('4-formatedSortedWeeks0sFinal.json') as json_file:
    covi = json.load(json_file)
    i = 0
    date = 1    
    initial = True
    
    """--- Initial parameters for the scene ----"""
    bpy.context.scene.frame_set(0)
    for material in bpy.data.materials:
        c = Color()
        c.hsv = 0.95, 0, 0.5
        material.diffuse_color = (c.r, c.g, c.b, 1)
        material.keyframe_insert(data_path='diffuse_color')
       
    """--- For every weekly registry of data by municipio ----""" 
    for day in covi:
        event = day['mun']
        
        for mun in event: 
            """Get name of object in 3D scene from municipal code"""
            if int(mun['mun_cod']) < 10000:
                name = '0' + str(mun['mun_cod'])
            else: 
                name = str(mun['mun_cod'])
            
            """Get the object in the 3D scene"""        
            obj = bpy.data.objects[name]

            """Change Size of the Municipio from the number of cases"""
            value = math.log(float(mun['casos'])+1, 1.45)
            obj.scale[2] = value
            obj.keyframe_insert(data_path='scale')
            
            """Change color of the Municipio by number of cases"""
            mat = bpy.data.materials[name]
            c = Color()
            c.hsv = 0.95, value/22.29, 0.5
            mat.diffuse_color = (c.r, c.g, c.b, 1)
            mat.keyframe_insert(data_path='diffuse_color')    
    
        """After presenting the weekly data cases go 25 frames forward and repeat with data from next week"""
        bpy.context.scene.frame_set(date * 25)
        date +=1
            