""" ------------------------------------------------------------------------
------------------ Take formated, sorted data ------------------------------
------------- create 3D visualization in blender  --------------------------
------------------------------------------------------------------------ """

"""Only Works inside blender SOFTWARE with the Blender python API bpy"""
import bpy
import json
import math

"""---- Give text format to the number of cases ----"""
def format(val):
    string = ''
    if val <= 999:
        string = str(val)
    elif val > 999:
        val = val/1000
        string = "{:.3f}".format(val)
    print(string)
    return string
        
        
"""---- From the info of the current frame get the cases value in the JSON dataset and put it into the 3D text----"""
def make_text(scene):
    with open('1-formatedSortedCasesByDay.json') as json_file:
        covi = json.load(json_file)
        text = bpy.data.objects['Text']
        frame = bpy.context.scene.frame_current
        if frame%5 == 0:
            i = math.floor(frame/3.6)
            value = covi[i]['casos']
            text.data.body = format(value) 


"""---- Run the script every time there is a frame change ----"""
bpy.app.handlers.frame_change_post.append(make_text)

