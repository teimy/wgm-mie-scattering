
from scipy import linspace, array

from spher import spher_, spher_sum

(cext, 
 csca, 
 a1, a2, a3, a4, 
 b1, b2, 
 lmax)  = spher_(.41, .015, 1.53, .008, 1.0e-13)





rad = array([.015*(i+1) for i in range(10)])
wrad = 0.0 * rad
wrad[0] += 1.0


(cext, csca, 
 a1, a2, a3, a4, 
 b1, b2, 
 lmax) = spher_sum(.41, rad, wrad, 1.53, .008, 1.0e-13)



