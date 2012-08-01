try:
    from blog import app
except:
    #Add to the path the project (running with python ./test_*.py)
    import sys
    sys.path.append('../../mysite')
    from blog import app	
import unittest

class BlogHelloworldTest(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
    	pass

    def test_hello_world(self):
        rv = self.app.get('/')
        assert 'Hello World!' in rv.data

if __name__ == '__main__':
    unittest.main()