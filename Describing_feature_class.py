import arcpy
majorAttractions_features_path = r"D:\3rd_semester\Programming_for_GIS_III\P2_describing_data\Practical_2_ProProject\02_Describing_Data.gdb\MajorAttractions"

majorAttraction_desc_obj = arcpy.Describe(majorAttractions_features_path)
print("The type of shape is {}".format(majorAttraction_desc_obj.shapeType))
print("Process Complete")