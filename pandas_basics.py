# -*- coding: utf-8 -*-
"""
Created on Sat Jul 02 19:01:19 2016

@author: Jiahe Wang
"""

"""
Series(array + index)
"""

import sys
import numpy as np
import pandas as pd

pd.Index
pd.Series


series_ex=pd.Series(np.arange(26))
series_ex

series_ex.index

import string
lcase = string.ascii_lowercase
ucase = string.ascii_uppercase
print lcase,ucase

lcase=list(lcase)
ucase=list(ucase)
print lcase
print ucase


series_ex.index=lcase
series_ex.index 
series_ex

series_ex.ix['d':'k']
series_ex.ix['f']

"""
DataFrame
"""

pd.DataFrame

letters = pd.DataFrame([lcase,ucase, range(26)])
letters

letters=letters.transpose()


letters.head()  #return first five rows

letters.columns
letters.index

#adding customized columns
letters.columns=['lowercase','uppercase','number']


letters
letters.lowercase
letters['lowercase']


"""
pd.date_range
"""
pd.date_range


letters.index=pd.date_range('9/1/2012','9/26/2012',peroids=26)
letters

letters['9-10-2012':'9-15-2012']





