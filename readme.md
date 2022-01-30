# Conversion of KML to SHP for multiple files at once

This code 
1) converts single kml-files into single shp-files,
2) compiles multiple shp-files into a single shp-file, 
3) adds an attribute field for each future to the compiled shp-file,
4) fills the added attribute field for each future with the name of the original kml-file.

The code is split into two files.
- "1_Converting_KML2SHP", covers step 1 and 2 listed above
- "2_Merging_SHP", covers step 3 and 4 listed above

The code was written in PyCharm Community Edition 2021.1.1 using Python 2.7.



## Description
The Keyhole Markup Language (KML) is used to express and store geographic information in .kml-files and .kmz-files. 
They can be read for instance with Google Earth. However, the files need to be converted in order to open them in Esri ArcMap. 
There is an existing conversion tool "KML To Layer" that allows to convert a .kml or .kmz-file into feature classes and a 
layer file. It does not offer the possibility to convert multiple .kml or .kmz-files at once. 

This code was written to convert multiple .kml or .kmz-files (input data) into one single feature class saved in a shapefile 
(.shp), that can be read and edited in Esri ArcMap. In order to distinguish the different input data in the shapefile, each 
feature is labelled with the name of the original .kml or .kmz-file.



## How to use
The code is commented and should therefore be easy to use. All lines that need adapting are marked as such with "###" at the 
beginning of the comment. 
Generally, the code is split into the four steps listed above. They are explained in more detail here.
1) Converting:
	In this step each .kml or .kmz-file is converted into a layer, based on the ArcMap tool "KML To Layer". While looping 
	through the .kml or .kmz-file, the code prints "converting: filename" for each file in order to keep track of progress.
	The statement "FINISHED CONVERTING" marks the end of this step.
2) Copying
	In this step, each created feature class is copied into the master geodatabase and named as the original .kml or .kmz-file.
	While looping through the feature classes, the code prints "copying: filename" for each feature class in order to keep 
	track of progress. The statement "FINISHED COPYING" marks the end of this step.
3) Creating attribute field
	In this step, an attribute field is added to each feature class and filled with the name of the feature class. While 
	looping through the feature classes, the code prints "filling attribute field: filename" for each feature class in order 
	to keep track of progress. The statement "FINISHED ATTRIBUTES" marks the end of this step.
4) Merging
	In this final step, all feature classes are merged into one single feature class. The statement "FINISHED MERGING" marks 
	the end of this step.



## Tips & Potential for improvement
While executing the code multiple times, it seemed rather slow. Therefore, a timer has been added and multiple runs of the code 
showed that the code execution gets slower (especially in step 1) when handling big amounts of data (>500 .kml-files). To avoid 
that, the file "1_Converting_KML2SHP" should be executed for smaller amounts of input data and only file "2_Merging_SHP" should be executed for the 
entirety of data. 
The code could be revised in order to improve execution time. 



## Credits & Contact
This code was written by Marianne Greber as part of the seminar "Geodata Analysis and Modelling" at the University of Bern. 
It was applied in the master thesis "Characteristics and high-resolution spatio-temporal evolution of glacial lakes in the 
Rhine catchment (Swiss Alps) since 1980" written by Marianne Greber at the University of Bern.
Name: Marianne Greber
E-Mail: marianne.greber@students.unibe.ch
