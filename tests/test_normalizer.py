from unittest import TestCase
from tnltk.normalizer import Normalizer

class TestNormalizer(TestCase):
    """
    TestNormalizer is a subclass of unittest.TestCase, and it contains methods for testing the functionality of the Normalizer class.

    The test methods in this class check the output of Normalizer class' methods against expected results.

    Methods
    -------
    test_lower_case()
        Test the lower_case method of Normalizer class by passing a sample text and comparing its output with the expected output.
    test_remove_punctuations()
        Test the remove_punctuations method of Normalizer class by passing a sample text and comparing its output with the expected output.
    test_remove_accent_marks()
        Test the remove_accent_marks method of Normalizer class by passing a sample text and comparing its output with the expected output.
    test_convert_text_numbers()
        Test the convert_text_numbers method of Normalizer class by passing a sample text and comparing its output with the expected output.
    """
    def test_lower_case(self):
        text = "Ex: İIĞÜÖŞÇ"
        self.assertEqual(Normalizer.lower_case(text), 'ex: iığüöşç')

    def test_remove_punctuations(self):
        text = "#Merhaba, Dünya!"
        self.assertEqual(Normalizer.remove_punctuations(text), 'Merhaba Dünya')

    def test_remove_accent_marks(self):
        text = "merhâbâ"
        self.assertEqual(Normalizer.remove_accent_marks(text), 'merhaba')

    def test_convert_text_numbers(self):
        text = "2,5 kilgoram şeker ve 20 adet sucuk alabilir miyim?"
        self.assertEqual(Normalizer.convert_text_numbers(text), "iki virgül beş kilgoram şeker ve yirmi adet sucuk alabilir miyim?")