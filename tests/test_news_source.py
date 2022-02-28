import  unittest
from  app.models import Source

class SourcesTest(unittest.TestCase):
    """
    Test class to test the behavior of our source class.
    """

    def setUp(self):
        """
        Set up method that is run before every test.
        """
        self.new_source = Source('Tuko', 'opera news hub',
                                 'silvano news', 'ntv','twitter', 'bbc')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))