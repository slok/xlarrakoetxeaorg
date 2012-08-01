
#append the application for the tests
import sys
sys.path.append("mysite")
import unittest

#Import tests (add)
from tests.blog.test_index import *


#Cross fingers and execute tests!!
unittest.main()