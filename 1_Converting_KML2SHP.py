# import libraries
import os
import arcpy

# start timer
begin_time = datetime.datetime.now()
print(begin_time)

# STEP 1 CONVERTING
# ### set workspace
arcpy.env.workspace = r"D:\In_Geodata"
arcpy.env.overwriteOutput = True

# ### set output settings and name MasterGDB
outLocation = r"D:\Out_Geodata"
MasterGDB = 'AllKMLLayers.gdb'
MasterGDBLocation = os.path.join(outLocation, MasterGDB)

# create master file geodatabase
arcpy.CreateFileGDB_management(outLocation, MasterGDB)

# convert all KML files
for kml in arcpy.ListFiles('*.KM*'):
	print ("converting: {0}".format(os.path.join(arcpy.env.workspace, kml)))
	arcpy.KMLToLayer_conversion(kml, outLocation)

print("FINISHED CONVERTING")

# STEP 2 COPYING
# change the workspace to fGDB location
arcpy.env.workspace = outLocation

# loop through all FileGeodatabases within the workspace
wks = arcpy.ListWorkspaces('*', 'FileGDB')

# skip the Master GDB
wks.remove(MasterGDBLocation)

for fgdb in wks:
	# change the workspace to the current FileGeodatabase
	arcpy.env.workspace = fgdb
	# for every Featureclasse, copy it to the Master and use the name from the original fGDB
	featureClasses = arcpy.ListFeatureClasses('*','', 'Placemarks')
	for fc in featureClasses:
		print("copying: {0} FROM: {1}".format(fc, fgdb))
		fcCopy = os.path.join(fgdb, 'Placemarks', fc)
		arcpy.FeatureClassToFeatureClass_conversion(fcCopy, MasterGDBLocation, fgdb[fgdb.rfind(os.sep)+1:-4])

print("FINISHED COPYING")


# clean up
del kml, wks, featureClasses, fgdb

# stopping timer
end_time = datetime.datetime.now()
print(end_time)
run_time = (end_time - begin_time)
print("The execution time was")
print (run_time)