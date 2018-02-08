#!/usr/bin/env python
# 
# Usage example of fitLine() and fitPlane()
#
# Draw a line in 3D that fits a cloud of 20 points,
# also show the first set of 20 points and fit a plane to them
#
import plotter
import numpy as np

# declare the class instance
vp = plotter.vtkPlotter(verbose=False, title='linear fitting')

# draw 500 fit lines superimposed and very transparent
for i in range(500): 
    
    x = np.linspace(-2, 5, 20) # generate each time 20 points
    y = np.linspace( 1, 9, 20)
    z = np.linspace(-5, 3, 20)
    data = np.array(list(zip(x,y,z)))
    data+= np.random.normal(size=data.shape)*0.8 # add gauss noise
    
    vp.fitLine(data, lw=4, alpha=0.03) # fit a line

# 'data' still contains the last iteration points
vp.points(data, c='red', legend='random points')

# the last fitted slope direction is stored in vp.result dictionary
print ('Line Fit slope= ', vp.result['slope']) 

vp.fitPlane(data, legend='fit plane') # fit a plane
print ('Plan Fit normal=', vp.result['normal']) 

vp.show()
