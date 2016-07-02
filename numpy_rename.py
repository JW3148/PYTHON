# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 14:03:33 2016

@author: Jiahe Wang
"""

"""
NummPy Array
"""
import numpy as np

npa=np.arange(10)


npa.mean()
npa.max()
npa.min()

npa**2 #vectorization

#below is not recommended
[x**2 for x in npa]


"""
Boolean Selection
"""
npa=np.arange(20)

npa%2==0 #this returns a booleana array
npa[npa%2==0]

"""
Helpful methods and Shortcuts
"""

npa=np.arange(25)

print type(npa)

print npa.dtype

#create array by passing a list
np.array(range(20))

np.array([1.0,0,2,3])
np.array([1.0,0,2,3]).dtype
np.array([True,2,2.0]).dtype

np.array([True,1,2.0],dtype='bool_')
np.array([True,1,2.0],dtype='float_')
np.array([True, 1, 2.0], dtype='uint8')

npa.size
npa.shape
npa.std()
npa.argmin()
npa.argmax()

np.linspace(1,2,5)

np.linspace(0,10,11).astype('int')
np.linspace(0,10,11).astype(np.float32)

np.float32(5)

"""
NaN
"""
problem=np.array([0.])/np.array([0.])
problem[0]

ar=np.linspace(0,10,11).astype(np.float32)
ar[0]=np.nan

ar.sum()
ar.max()


"""
Vectorization

np.vectorize(function)
"""
import numpy as np

npa=np.random.random_integers(0,50,20)


def new_func(numb):
    if numb<10:
        return numb**3
    else:
        return numb**2

vect_new_func=np.vectorize(new_func)

type(vect_new_func)
vect_new_func(npa)

"""
Multi-dimensional Arrays

.reshape(m,n)
"""
import numpy as np

npa=np.arange(25)
npa

npa.reshape(5,5) #not in place

npa2=np.zeros((5,5))

npa2.size
npa2.shape
npa2.ndim

np.arange(8)
np.arange(8).reshape(2,2,2)


npa2
npa

np.random.seed(10)

npa2=np.random.random_integers(1,10,25).reshape(5,5)
npa2

np.random.seed(10)

npa3=np.random.random_integers(1,10,25).reshape(5,5)
npa3
 
npa2>npa3
npa2.min()
npa2.max(axis=0)  #max value in each column
npa2.T
npa2.T==npa2.transpose()
npa2.T * npa2

npa2.flatten()


"""
Querying, Slicing, Combining and Spilitting
"""
import numpy as np

np.random.seed(10)

ar=np.arange(12)
ar2=np.random.random_integers(12,size=12)
ar2

ndim_ar=np.arange(12).reshape(3,4)
ndim_ar

ndim_ar2=np.random.random_integers(12,size=(3,4))
ndim_ar2

ndim_ar3d=np.arange(8).reshape(2,2,2)
ndim_ar3d

ar
ar[5]  #index 5 actuarially 6 rank
ar[5:]
ar[1:6:2] #index starting 1, to 5, step=2
ar[-1:-6:-1] #index staring -1 to -5, step=2,  -1 = last

ndim_ar
ndim_ar[:,1:3]
ndim_ar[1:3,:]
ndim_ar[1:3,1:3]


ndim_ar3d
ndim_ar3d[0,:,1:]

ar
ar2
np.vstack((ar,ar2))

ndim_ar
ndim_ar2
np.vstack((ndim_ar,ndim_ar2))

np.hstack()

ndim_ar3d=np.dstack((ndim_ar,ndim_ar2))
ndim_ar3d
ndim_ar3d_split=np.dsplit(ndim_ar3d,2)
ndim_ar3d_split



ar3 = np.hstack((ar,ar2))
ar3

ar4=np.hsplit(ar3,2)

type(ndim_ar)



