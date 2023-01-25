"""
A Utility Script for the normalizer script (Normalizer Class) in the Normalizer Package

_normalizer_builtin.py is a script that contains helper functions for the normalizer.py script.
These functions are specific to the normalizer module and are used to convert numbers to words in Turkish language.
The script contains two functions, _convert_group and number_to_word.
The _convert_group function converts a given number to words in Turkish language by dividing the number into groups
of 100 and then converting each group to words using the provided lists of ones and tens.

These functions are used by normalizer.py script to perform number to word conversion tasks.
"""

def _convert_group(number: int, ones: list, tens: list) -> str:
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
        number = str(number).split('-')[1]
        negative_expression = 'eksi '
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
            group_description = _convert_group(remainder, ones, tens)
            if group > 0:
                group_description += " " + scales[group]
            ne = " " if negative_expression is None else f"{negative_expression}"
            word = ne + group_description + word
        group += 1

    return word
