from unittest import TestCase
from tnltk.normalizer import Deasciifier

class TestDeasciifier(TestCase):
    """
    TestDeasciifier class is a unit test case for the Deasciifier class.
    It includes a single test method, test_deasciify, which tests the deasciify method of the Deasciifier class.
    The test creates an instance of the Deasciifier class with a sample string as input and calls the deasciify method on it.
    The expected result is then compared with the actual result using the assertEqual method from the unittest.TestCase class.
    This test ensures that the deasciify method correctly replaces ASCII characters with their Turkish equivalents in the given string.
    """
    def test_deasciify(self):
        deasciifier = Deasciifier("O sirada bahcede cıcekleri kokluyorduk. Hersey bahcıvanın islik calmasiyla yasandi...")
        result = deasciifier.deasciify()
        expected_result = "O sırada bahçede çiçekleri kokluyorduk. Herşey bahçıvanın ıslık çalmasıyla yaşandı..."
        self.assertEqual(result, expected_result)