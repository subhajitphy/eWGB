The required files can be found tapti: /Data/sdandapat/Research@TIFR/recent/runK0.9

split.py splits the code into equal parts depending upon the number of core inputs given for multicore computation. (If the number of the array size (Mass) is 60 and ncore =30, it split the code into 30 parts, afterward computes each part parallelly and gives the combined output in .pkl format)

while split2.py compute the spectrum after incorporating comoving density in a similar fashion. 
