# import libraries
import os
import arcpy


# start timer
begin_time = datetime.datetime.now()
print(begin_time)


# STEP 3 CREATING + FILLING ATTRIBUTE
# ### set workspace
arcpy.env.workspace = r"D:\Out_Geodata\AllKMLLayers.gdb"
arcpy.env.overwriteOutput = True

datasets = arcpy.ListDatasets(feature_type='feature')
datasets = [''] + datasets if datasets is not None else []

# loop through all feature classes within the workspace
for ds in datasets:
    featureclasses = arcpy.ListFeatureClasses(feature_dataset=ds)
    for polyID in featureclasses:
        print("filling attribute field: {0}".format(polyID))

        inFeatures = polyID
        # ### set name of Attribute Field
        fieldName1 = "PolygonID"
        fieldContent = '"' + polyID + '"'
        arcpy.AddField_management(inFeatures, fieldName1, "TEXT", field_length=30)
        arcpy.CalculateField_management(inFeatures, fieldName1, fieldContent)

print("FINISHED ATTRIBUTES")


# STEP 4 MERGING
# ### set output settings and name the final GDB
outLocation = r"D:\Res_Geodata"
SGLIgdb = 'Geodata.gdb'
SGLIlocation = os.path.join(outLocation, SGLIgdb)

# create master file geodatabase
arcpy.CreateFileGDB_management(outLocation, SGLIgdb)

fcs = arcpy.ListFeatureClasses()

# ### set name of the final output feature class shapefile
mergeOutput = 'Final_Output_mergedSHP'
mergeOutLocation = os.path.join(SGLIlocation, mergeOutput)

arcpy.Merge_management(fcs, mergeOutLocation)

print("FINISHED MERGING")


# stopping timer
end_time = datetime.datetime.now()
print(end_time)
run_time = (end_time - begin_time)
print("The execution time was")
print (run_time)


