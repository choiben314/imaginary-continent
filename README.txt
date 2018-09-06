Imaginary Continent
The goal of imaginary continent is to provide a reasonable hypothesis for spatially discrete climate zones defined by 
the Koppen system of classification based on the application of a neural network to a user-defined map of geographic
elevation, proximity/direction to water features, and latitude.

Geographic Elevation

	-> Elevation effects on climate
	-> Physical effects of elevation on surroundings
		- orographic lifting

Proximity/Direction to Water Features
	-> Effects of specific heat and relative humidity
	-> Precipitation effects

Latitude
	-> Effects of global circulation cells
	-> Deviations in insolation

Potential feature: 
Prevailing wind direction and speed; upper and lower
	-> convergence/divergence
	-> relation to mountains/bodies of water

Datasets Used:

NOAA Global Surface Summary of the Day (GSOD) from Integrated Surface Hourly (ISH) Dataset (WMO Stations/Elevation)
Koppen Classification Data - Hans Chen
0.04 Degree Distance to Nearest Coast - NASA Ocean Biology Processing Group


1. Get Data

For each latitude/longitude:
	- proximity to coast
	- elevation
	- koppen classification
	- (avg wind direction and speed)

2. Create common dataset with:
	- latitude
	- longitude
	- elevation
	- koppen
	- (avg wind direction and speed)

3. Calculate the following:
	- closest coastal point
	- cardinal direction to point

4. Run neural network on input nodes with y=koppen classification:
	- distance to coastal point
	- direction to coastal point
	- elevation

5. Make GUI interface for imaginary continent
	- run neural network	



























