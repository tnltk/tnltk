import string
import warnings
from ._normalizer_builtin import number_to_word
import re

class Normalizer:

    @staticmethod
    def lower_case(text: str) -> str:
        """
        Converts a string of text to lowercase for Turkish language.
        
        This function handles all Turkish characters which are not handled properly by python lower() method, 
        e.g., "İ" -> "i", "I" -> "ı", "Ğ" -> "ğ", "Ü" -> "ü", "Ö" -> "ö", "Ş" -> "ş", "Ç" -> "ç".

        Parameters
        ----------
        text : str 
            Input text.

        Returns
        -------
        output : str
            Text in lowercase form.

        Example:
        --------
        >>> from tnltk.normalizer import Normalizer
        >>> Normalizer.lower_case("Ex: İIĞÜÖŞÇ")
        'ex: iığüöşç'
        """
        turkish_lowercase_dict = {"İ": "i", "I": "ı", "Ğ": "ğ", "Ü": "ü", "Ö": "ö", "Ş": "ş", "Ç": "ç"}
        for k, v in turkish_lowercase_dict.items():
            text = text.replace(k, v)
        return text.lower()

    @staticmethod
    def remove_punctuations(text: str)-> str:
        """
        Removes punctuations (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~) from the given string.
        
        This function removes all the punctuation characters from the given text.

        Parameters
        ----------
        text : str 
            Input text.

        Returns
        -------
        output : str
            Text stripped from punctuations.

        Example:
        --------
        >>> from tnltk.normalizer import Normalizer
        >>> Normalizer.remove_punctuations("#Merhaba, Dünya!")
        'Merhaba Dünya'
        """
        return re.sub(f'[{string.punctuation}]', '', text)


    @staticmethod
    def remove_accent_marks(text: str)-> str:
        """
        Removes accent marks from the given string.

        Parameters
        ----------
        text : str 
            Input text.

        Returns
        -------
        text : str
            Text stripped from accent marks.

        Example:
        --------
        >>> from tnltk.normalizer import Normalizer
        >>> Normalizer.remove_accent_marks("merhâbâ")
        'merhaba'
        """
        accent_marks = {'â':'a', 'ô':'o', 'î':'i', 'ê':'e', 'û':'u',
                        'Â':'A', 'Ô':'O', 'Î':'İ', 'Ê':'E', 'Û': 'U'}
        for mark, letter in accent_marks.items():
            text = text.replace(mark, letter)
        return text


    @staticmethod
    def convert_text_numbers(text):
        """
        Convert numbers in a text to words in Turkish language

        This function converts numbers in a given text to words in Turkish language.
        The function uses regular expressions to find and extract numbers in the text,
        and then uses the number_to_word function to convert the numbers to words.
        If the number is too large, a warning is issued. If the decimal number is represented by a period,
        a warning is issued. (because in Turkish language decimal number is represented by comma.)
        The last text where numbers were converted to words is returned.

        Parameters
        ----------
        text : str
            The text containing numbers to be converted to words

        Returns
        -------
        text : str
            The text with the numbers converted to words in Turkish language

        Example:
        --------
        >>> from tnltk.normalizer import Normalizer
        >>> Normalizer.convert_text_numbers("Evi 1000000 TL Değerinde! Çok güzel bir evi var ama 3,5 ay boyunca satamamışlar...")
        'Evi bir milyon TL Değerinde! Çok güzel bir evi var ama üç virgül beş ay boyunca satamamışlar...
        """
        def convert_number(match):
            number = float(match.group(0).replace(",", "."))
            if number >= 1e21:
                return warnings.warn("The number is too big to convert it to words in Turkish language.")
            elif number == int(number):
                return number_to_word(int(number))
            else:
                return warnings.warn("In Turkish language, decimal numbers are expressed with commas.")
        return re.sub(r"[-+]?\d*.\d+|\d+", convert_number, text.replace(","," virgül ")).lstrip()
    