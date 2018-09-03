Köppen climate classification
=============================

Description
-----------

Data from Chen and Chen (2013). The .tsv files contain the Köppen climate
types for the period 1901-2010 on different time scales.

Last updated: 5 May 2013.

See the website for more information: http://hanschen.org/koppen


File format
-----------

Tab delimited ASCII text files with CRLF line endings.

Line 1: Header.
Line 2-85795: Data.

Column 1: Longitude.
Column 2: Latitude.
Column 3-: Köppen type for the time period indicated in the header.

The first two columns give the center grid coordinates, where each grid box
has a horizontal resolution of 0.5 degree by 0.5 degree longitude/latitude.


References
----------

Chen, D. and H. W. Chen, 2013: Using the Köppen classification to quantify 
climate variation and change: An example for 1901-2010. Environmental 
Development, 6, 69-79, 10.1016/j.envdev.2013.03.007.


Contact
-------

Hans Chen <hans.chen@psu.edu>

