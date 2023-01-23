def _convert_group(number, ones, tens):
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

def number_to_word(number):
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