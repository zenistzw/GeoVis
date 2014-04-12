"""
Example Script for the Python Geographic Visualizer (GeoVis)
https://github.com/karimbahgat/geovis
"""

############
#TEST INPUTS
############
TEMP_GEOVIS_FOLDER = r"C:\Users\BIGKIMO\Documents\GitHub\geovis"
BACKGROUND_SHAPEFILE = r"D:\Test Data\necountries\necountries.shp"
TEST_SHAPEFILE = r"D:\Test Data\GTD_georef\gtd_georef.shp"
ATTRIBUTE_TO_CLASSIFY = "nkill"
##TEST_SHAPEFILE = r"D:\Test Data\GTD_georef\intnat_source.shp"
##ATTRIBUTE_TO_CLASSIFY = "Average_nk"
CLASSIFYTYPE = "natural breaks"
NRCLASSES = 5
############

#importing geovis from temporary location
import sys
sys.path.append(TEMP_GEOVIS_FOLDER)
import geovis

#create map with background
geovis.SetMapBackground(geovis.Color("blue",style="pastelle"))
newmap = geovis.NewMap()
newmap.AddToMap(BACKGROUND_SHAPEFILE, fillcolor=geovis.Color("green",style="pastelle"), outlinecolor=geovis.Color("green",style="pastelle"))

#classify shapefile
classifier = geovis.Classifier()
##classifier.AddClassification(symboltype="fillcolor",
##                             valuefield=ATTRIBUTE_TO_CLASSIFY,
##                             symbolrange=[geovis.Color("green", intensity=0.9, brightness=0.5),
##                                          geovis.Color("yellow", intensity=0.9, brightness=0.5),
##                                          geovis.Color("red", intensity=0.9, brightness=0.5)],
##                             classifytype=CLASSIFYTYPE,
##                             nrclasses=NRCLASSES,
##                             excludevalues=[0,-1])
classifier.AddClassification(symboltype="outlinecolor",
                             valuefield=ATTRIBUTE_TO_CLASSIFY,
                             symbolrange=[geovis.Color("yellow", style="strong"),
                                          geovis.Color("red", style="weak"),
                                          geovis.Color("red", style="strong"),
                                          geovis.Color("red", intensity=1)],
                             classifytype=CLASSIFYTYPE,
                             nrclasses=NRCLASSES,
                             excludevalues=[0,-1])
classifier.AddClassification(symboltype="fillsize",
                             valuefield=ATTRIBUTE_TO_CLASSIFY,
                             symbolrange=[3,
                                          150,
                                          200],
                             classifytype=CLASSIFYTYPE,
                             nrclasses=NRCLASSES,
                             excludevalues=[0,-1])
classifier.AddClassification(symboltype="outlinewidth",
                             valuefield=ATTRIBUTE_TO_CLASSIFY,
                             symbolrange=[0.8,
                                          3],
                             classifytype=CLASSIFYTYPE,
                             nrclasses=NRCLASSES,
                             excludevalues=[0,-1])

#add shapefile to map along with the created classifier
newmap.AddToMap(shapefilepath=TEST_SHAPEFILE,
                classifier=classifier,
                pointtype="pyramid",
                fillwidth=9)

#view map
newmap.ViewMap()

