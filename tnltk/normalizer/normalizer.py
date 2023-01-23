import string
import warnings
import re 

class Normalizer:
    def __init__(self):
        pass

    @staticmethod
    def lower_case(self,text: str) -> str:
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
        >>> from tnltk import Normalizer
        >>> Normalizer.lower_case("Ex: İIĞÜÖŞÇ")
        'ex: iığüöşç'
        """
        turkish_lowercase_dict = {"İ": "i", "I": "ı", "Ğ": "ğ", "Ü": "ü", "Ö": "ö", "Ş": "ş", "Ç": "ç"}
        for k, v in turkish_lowercase_dict.items():
            text = text.replace(k, v)
        return text.lower()


    @staticmethod
    def remove_punctuations(self, text: str)-> str:
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
        >>> from tnltk import Normalizer
        >>> Normalizer.remove_punctuations("#Merhaba, Dünya!")
        'Merhaba Dünya'
        """
        return re.sub(f'[{string.punctuation}]', '', text)


    @staticmethod
    def remove_accent_marks(self, text: str)-> str:
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
        >>> from tnltk import Normalizer
        >>> Normalizer.remove_accent_marks("merhâbâ")
        'merhaba'
        """
        accent_marks = {'â':'a', 'ô':'o', 'î':'ı', 'ê':'e', 'û':'u',
                        'Â':'A', 'Ô':'o', 'Î':'ı', 'Ê':'e', 'Û': 'u'}
        for mark, letter in accent_marks.items():
            text = text.replace(mark, letter)
        return text


    @staticmethod
    def number_to_word(self, number):
        negative_expression = None
        if int(number) < 0:
            number = str(number).split('-')[1]
            negative_expression = 'eksi '
            number = int(number)

        ones = ["sıfır", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
        tens = ["on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]
        scales = ["", "bin", "milyon", "milyar"]
        word = ""

        if number == 0:
            return ones[0]

        group = 0
        while number > 0:
            number, remainder = divmod(number, 1000)
            if remainder > 0:
                group_description = _convert_group(remainder, ones, tens)
                if group > 0:
                    group_description += " " + scales[group]
                ne = " " if negative_expression is None else f"{negative_expression}"
                word = ne + group_description + word
            group += 1

        return word

    @staticmethod
    def _convert_group(self, number, ones, tens):
        word = ""
        if number >= 100:
            if number // 100 != 1:
                word += ones[number // 100] + " yüz"
            else:
                word += "yüz"
            number = number % 100
        if number >= 10:
            word += " " + tens[number // 10 - 1]
            number = number % 10
        if number > 0:
            word += " " + ones[number]
        return word.strip()

    @staticmethod
    def convert_text_numbers(text):
        def convert_number(match):
            number = float(match.group(0).replace(",", "."))
            if number == int(number):
                return number_to_word(int(number)).replace("", "")
            else:
                return warnings.warn("In Turkish language, decimal numbers are expressed with commas.")
        return re.sub(r"[-+]?\d*.\d+|\d+", convert_number, text.replace(',', ' virgül '))