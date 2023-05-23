#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### SCIPY
"""
USED IN STATISTICS, 
SPATIAL DATA//DATA RETRIEVAL, 
IMAGE SCIENCE, 
MATHEMATICAL EQUATION INCLUDING DIFFERENTIATION AND OTHER MATHEMATICAL EQUATIONS
PLATFORM INTEGRATION
SIGNA PROCESSING LIKE ANALOG AND DIGITAL
OPIMIZATION
"""

"""
HAS MATHEMATICAL LIBRARIES
SUBPACKAGES FOR SCIENTIFIC DOMAINS
SCIENTIFIC COMPUTING DOMAINS
#### SUBPACKAGES ####
STATS
SPECIAL
CONSTANTS
CLUSTER ALGORITHMS
FFT//DFT USING 
SPATIAL DATA STRUCTURES
INTERPOLATE
INPUT AND OUTPUT/// IO
NDIMAGE
ODR///IMPLICIT AND EXPLICIT FUNCTIONS
SIGNALS
SPARSE
WEAVE
OPTIMIZE
LINAG
"""


# In[1]:


#### IMPORT THE LIBRARY
import numpy as np
from scipy import linalg


# In[2]:


### a test has 30 questions worth 150 points
###### true and false answer questions worth 4 points each
###### mcqs worth 9 points each

# let x be the number of questions with true or false answers
# let y be the number of mcqs

# (x + y = 30)
# (4x + 9y = 150)
testQuestionVariable = np.array([[1,1],[4,9]])
testQuestionValue = np.array([30,150])


# In[3]:


# we use the linalg function of the scipy package
# use teh solve method to solve linear equation and find value for x and y
linalg.solve(testQuestionVariable,testQuestionValue)


# In[ ]:




