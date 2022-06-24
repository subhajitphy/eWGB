scaleQ.ipynb is the scaling approach by siyuan2017 paper.
Whereas, model_AN_Q.ipynb is the fully numerical approach that doe's not make use of the scaling procedure. 


SplitQ.py splits the code into equal parts depending upon the number of core inputs given for multicore computation.
(If the number of the array size (Mass) is 60 and ncore =30, it split the code into 30 parts, afterward computes each part parallelly and gives the combined output in .pkl format)
