import arcpy
import os
file_GDB_path = r"D:\3rd_semester\Programming_for_GIS_III\P2_describing_data\Practical_2_ProProject\02_Describing_Data.gdb"
majorAttraction_fc_name = "MajorAttractions"
freeways_fc_name = "Freeways"
majorAttraction_fc_full_path = os.path.join(file_GDB_path, majorAttraction_fc_name)
freeWays_path = os.path.join(file_GDB_path, freeways_fc_name)

majorAttraction_desc_obj = arcpy.Describe(majorAttraction_fc_full_path)
freeways_desc_obj = arcpy.Describe(freeWays_path)

print("The type of shape is {}".format(majorAttraction_desc_obj.shapeType))
print(freeways_desc_obj.shapeType)
print("Process Complete")