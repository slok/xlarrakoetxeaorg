
#append the application for the tests
import sys
import os
import unittest


# Add dirs inside the python path (need for travis)
BASE_DIR = os.path.dirname(__file__)
sys.path.append(BASE_DIR + '/mysite')
sys.path.append(BASE_DIR)

# Import tests (add)
from tests.blog.test_index import *

# Cross fingers and execute tests!!
unittest.main()
