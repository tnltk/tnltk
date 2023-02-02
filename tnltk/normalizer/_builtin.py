import string
import pickle

class DeasciifierBuiltin:
    """
    This system is based on the turkish-mode by Dr. Deniz Yüret

    A class to convert an ASCII-only string to a Turkish string.

    Parameters
    ----------
    ascii_string : str
          The ASCII-only string to be converted

    Attributes
    ----------
    ascii_string : str
          The ASCII-only string passed as input.
    converted_string : str
          The converted string, initially set as the input ascii_string.
    context_size : int
          The number of characters to be considered as context when converting a character.
    turkish_asciify_table : dict
          A dictionary containing the mapping of Turkish characters to their ASCII equivalents.
    turkish_downcase_asciify_table : dict
          A dictionary containing the mapping of Turkish characters to their lowercase equivalents.
    turkish_upcase_accents_table : dict
          A dictionary containing the mapping of Turkish characters to their uppercase equivalents.

    Methods
    -------
    get_path()
        This function returns the path to the parent directory of the `tnltk/` folder.
    set_char_at(str, position, char)
          Replaces the character at a specific position in a given string with a new character.
    convert_to_turkish(self)
          Converts an ASCII-only string to a Turkish string by replacing characters with their corresponding Turkish letters.
    turkish_need_correction(char, position)
          Check if the character needs to be corrected.
    turkish_toggle_accent(char, position)
          Toggles the accent of the character.
    """
    
    def get_path():
        """
        This function returns the path to the parent directory of the `tnltk/` folder.
        
        Returns:
        -------
        str:
            Path to the parent directory of the `tnltk/` folder.
        """
        return __file__[:__file__.find('tnltk/') + len('tnltk/')]

    ascii_pickle_path = get_path() + 'resources/ascii_to_str_dict.pickle'

    with open(ascii_pickle_path, 'rb') as file:
        turkish_pattern_table = pickle.load(file)
    del file
    
    context_size = 10

    def __init__(self, ascii_string):
        """
        This function initializes the DeasciifierBuiltin class.
        It takes an ascii_string as input and creates an instance of the DeasciifierBuiltin class.
        The ascii_string is stored in the instance variable 'ascii_string' and also set as the initial value for 'converted_string' which will later be used to store the converted string.

        It also creates three dictionaries:
        -----------------------------------
              - turkish_asciify_table: a dictionary containing the mapping of Turkish characters to their ASCII equivalents.
              - turkish_downcase_accents_table: a dictionary containing the mapping of Turkish characters to their lowercase equivalents.
              - turkish_upcase_accents_table: a dictionary containing the mapping of Turkish characters to their uppercase equivalents.
        """
        self.ascii_string = ascii_string
        self.converted_string = ascii_string
        self.turkish_asciify_table = {
            "ç": "c",
            "Ç": "C",
            "ğ": "g",
            "Ğ": "G",
            "ö": "o",
            "Ö": "O",
            "ü": "u",
            "Ü": "U",
            "ı": "i",
            "İ": "I",
            "ş": "s",
            "Ş": "S",
        }
        self.turkish_downcase_asciify_table = {
            **{ch: ch.lower() for ch in string.ascii_uppercase},
            **{ch.lower(): ch.lower() for ch in string.ascii_uppercase},
            "ç": "c",
            "Ç": "c",
            "ğ": "g",
            "Ğ": "g",
            "ö": "o",
            "Ö": "o",
            "ü": "u",
            "Ü": "u",
            "ı": "i",
            "İ": "i",
            "ş": "s",
            "Ş": "s",
        }
        self.turkish_upcase_accents_table = {
            **{ch: ch.lower() for ch in string.ascii_uppercase},
            **{ch.lower(): ch.lower() for ch in string.ascii_uppercase},
            "ç": "C",
            "Ç": "C",
            "ğ": "G",
            "Ğ": "G",
            "ö": "O",
            "Ö": "O",
            "ü": "U",
            "Ü": "U",
            "ı": "I",
            "İ": "I",
            "ş": "S",
            "Ş": "S",
        }

    def set_char_at(self, str, position, char):
        """
        Replaces the character at a specific position in a given string with a new character.

        Parameters
        ----------
        str : str
              The input string that the character will be replaced in.
        position : int
              The index of the character that will be replaced.
        char : str
              The new character that will be inserted at the specified position.

        Returns
        -------
        str
              The input string with the specified character replaced.

        Example
        --------
        >>> deasciifier = DeasciifierBuiltin("hello world")
        >>> deasciifier.set_char_at("hello world", 5, ",")
        'hello,world'
        """
        return str[0:position] + char + str[position + 1 :]

    def convert_to_turkish(self):
        """
        Converts an ASCII-only string to a Turkish string by replacing characters with their corresponding Turkish letters.
        The function checks if the character needs to be corrected by using the turkish_need_correction() function.
        If the character needs to be corrected, it uses the turkish_toggle_accent() function to correct it.

        Returns
        -------
        str
            The converted Turkish string.
        """
        for index in range(len(self.converted_string)):
            char = self.converted_string[index]
            if self.turkish_need_correction(char, point=index):
                self.converted_string = self.set_char_at(self.converted_string, index, self.turkish_toggle_accent(char))
            else:
                self.converted_string = self.set_char_at(self.converted_string, index, char)

        return self.converted_string
    
    def turkish_toggle_accent(self, c):
        """
        Toggles the accent of a Turkish character.

        Parameters
        ----------
        char : str
              A single character of the Turkish alphabet.

        Returns
        -------
        str
              The character with the accent toggled.

        Example
        -------
        >>> toggle_accent = turkish_toggle_accent('i')
        >>> toggle_accent
        'ı'
        """
        turkish_toggle_accent_table = {
            "c": "ç",
            "C": "Ç",
            "g": "ğ",
            "G": "Ğ",
            "o": "ö",
            "O": "Ö",
            "u": "ü",
            "U": "Ü",
            "i": "ı",
            "I": "İ",
            "s": "ş",
            "S": "Ş",
            "ç": "c",
            "Ç": "C",
            "ğ": "g",
            "Ğ": "G",
            "ö": "o",
            "Ö": "O",
            "ü": "u",
            "Ü": "U",
            "ı": "i",
            "İ": "I",
            "ş": "s",
            "Ş": "S",
        }
        return turkish_toggle_accent_table.get(c, c)

    def turkish_need_correction(self, char, point=0):
        """
        Determine if the given character needs correction in the given point of the text.

        Parameters
        ----------
        char : str
              The character to be checked for correction.
        point : int
              The position of the character in the text.

        Returns
        -------
        bool
              True if the character needs correction, False otherwise.

        Examples
        --------
        >>> deasciifier = DeasciifierBuiltin("Opusmegi cagristiran catirtilar.")
        >>> deasciifier.turkish_need_correction('a', 5)
        True
        >>> deasciifier.turkish_need_correction('g', 4)
        False
        """
        ch = char
        tr = self.turkish_asciify_table.get(ch, ch)
        pl = DeasciifierBuiltin.turkish_pattern_table.get(tr.lower(), False)
        if pl != False:
            m = self.turkish_match_pattern(pl, point)
        else:
            m = False

        if tr == "I":
            if ch == tr:
                return not m
            else:
                return m
        else:
            if ch == tr:
                return m
            else:
                return not m

    def turkish_match_pattern(self, dlist, point=0):
        """
        Check if the given pattern exists in the context of the given point in the text.

        Parameters
        ----------
        pattern_list : dict
              A dictionary of patterns and their corresponding ranks.
        point : int, optional
              The point in the text to check for the pattern, by default 0.

        Returns
        -------
        bool
              True if the pattern exists in the context, False otherwise.

        Example
        -------
        >>> deasciifier = DeasciifierBuiltin("Opusmegi cagristiran catirtilar.")
        >>> pattern_list = {"pus": 1, "me": 2, "agr": 3, "sti": 4, "ran": 5, "cat": 6}
        >>> deasciifier.turkish_match_pattern(pattern_list, point = 2)
        True
        """
        rank = 2 * len(dlist)
        str = self.turkish_get_context(DeasciifierBuiltin.context_size, point=point)
        start = 0
        end = 0

        _len = len(str)
        while start <= DeasciifierBuiltin.context_size:
            end = 1 + DeasciifierBuiltin.context_size
            while end <= _len:
                s = str[start:end]
                r = dlist.get(s, False)
                if r and abs(r) < abs(rank):
                    rank = r
                end = 1 + end
            start = 1 + start

        return rank > 0

    def turkish_get_context(self, size=context_size, point=0):
        """
        Returns the context of the given point in the string.

        Parameters
        ----------
        size : int, optional
            The size of the context to be returned. Default is context_size.
        point : int, optional
            The point in the string for which the context is to be returned. Default is 0.

        Returns
        -------
        str
            The context of the given point in the string.

        Example
        -------
        >>> example_input = 'This is a sample string.'
        >>> context_size = 5
        >>> point = 7
        >>> example_input.get_context(context_size, point)
        'is a sa'
        """
        s = " " * (1 + (2 * size))
        s = s[0:size] + "X" + s[size + 1 :]
        i = 1 + size
        space = False
        index = point
        current_char = self.converted_string[index]

        index = index + 1

        while i < len(s) and not space and index < len(self.ascii_string):
            current_char = self.converted_string[index]
            x = self.turkish_downcase_asciify_table.get(current_char, False)
            if not x:
                if not space:
                    i = i + 1
                    space = True
            else:
                s = s[0:i] + x + s[i + 1 :]
                i = i + 1
                space = False
            index = index + 1

        s = s[0:i]

        index = point
        i = size - 1
        space = False

        index = index - 1
        while i >= 0 and index >= 0:
            current_char = self.converted_string[index]
            x = self.turkish_upcase_accents_table.get(current_char, False)
            if not x:
                if not space:
                    i = i - 1
                    space = True
            else:
                s = s[0:i] + x + s[i + 1 :]
                i = i - 1
                space = False
            index = index - 1

        return s


class NormBuiltin():
    """
    These functions in NormBuiltin are specific to the normalizer module and are used to convert numbers to words in Turkish language.
    The script contains two functions, _convert_group and number_to_word.
    The _convert_group function converts a given number to words in Turkish language by dividing the number into groups
    of 100 and then converting each group to words using the provided lists of ones and tens.

    These functions are used by normalizer.py script to perform number to word conversion tasks.
    """
    def convert_group(number: int, ones: list, tens: list) -> str:
        """
        Convert the given number to words in Turkish language

        This function converts a given number to words in Turkish language.
        The number is first divided into groups of 100, then the groups
        are converted to words using the provided lists of ones and tens.
        The final word is returned after stripping leading and trailing whitespaces.

        Parameters
        ----------
        number : int
            The number to be converted to words
        ones : list
            List of words for numbers from 1 to 9
        tens : list
            List of words for numbers from 10 to 90

        Returns
        -------
        word : str
            The number in words in Turkish language
        """
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

    def number_to_word(number: int) -> str:
        """
        Convert the given number to words in Turkish language

        This function converts a given number to words in Turkish language.
        The number is first checked if it is negative, if so, it is converted
        to positive and 'eksi' is added to the beginning. The number is then
        divided into groups of 1000, and the groups are converted to words
        using the provided lists of ones and tens. The final word is returned.

        Parameters
        ----------
        number : int
            The number to be converted to words

        Returns
        -------
        word : str
            The number in words in Turkish language
        """
        negative_expression = None
        if int(number) < 0:
            number = str(number).split("-")[1]
            negative_expression = "eksi "
            number = int(number)

        ones = ["sıfır", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
        tens = ["on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]
        scales = ["", "bin", "milyon", "milyar", "trilyon", "katrilyon"]
        word = ""

        if number == 0:
            return ones[0]

        group = 0
        while number > 0:
            number, remainder = divmod(number, 1000)
            if remainder > 0:
                group_description = NormBuiltin.convert_group(remainder, ones, tens)
                if group > 0:
                    group_description += " " + scales[group]
                ne = " " if negative_expression is None else f"{negative_expression}"
                word = ne + group_description + word
            group += 1

        return word
    