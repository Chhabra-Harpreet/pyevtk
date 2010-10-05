# **************************************************************
# * Example of how to use the high level pointsToVTK function. *
# * Author: Paulo A. Herrera                                   *
# * Created: Mon 04 Oct 2010 02:40:35 PM CEST                  *
# * Last Modified: Tue 05 Oct 2010 11:45:45 AM CEST            *
# **************************************************************

from evtk.hlevtk import pointsToVTK
import numpy as np

npoints = 100
x = np.random.rand(npoints)
y = np.random.rand(npoints)
z = np.random.rand(npoints)
pressure = np.random.rand(npoints)
temp = np.random.rand(npoints)

pointsToVTK("./points", x, y, z, data = {"temp" : temp, "pressure" : pressure}) 

