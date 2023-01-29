from typing import List
import re

non_breaking_prefixes_tr = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
    "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "Ç", "Ğ", "İ", "Ö",
    "Ş", "Ü", "ab", "abd", "alt", "ara", "arc", "ard", "at", "av", "bak",
    "baz", "bel", "ben", "ber", "beş", "bi", "bir", "biz", "bu", "çok", "da",
    "daha", "de", "def", "del", "dem", "den", "der", "değ", "di", "dil", "din",
    "dir", "dol", "don", "dört", "du", "dur", "düş", "e", "ed", "ek", "el",
    "en", "er", "et", "ev", "faz", "gaz", "gen", "gez", "gid", "gör", "gün",
    "haz", "iç", "iş", "il", "it", "iz", "ka", "kad", "kar", "kaz", "kez",
    "ki", "kim", "kur", "la", "laz", "le", "li", "lü", "mah", "mak", "mal",
    "man", "mas", "me", "mev", "mil", "müt", "na", "nam", "ne", "ni", "nın",
    "nin", "nit", "nun", "o", "ok", "ol", "on", "ot", "öt", "öz", "öğ", "ra",
    "rak", "ral", "ran", "ras", "rat", "ray", "ri", "rü", "sa", "sak", "sal",
    "sam", "san", "sar", "sat", "say", "se", "seb", "sen", "ser", "set", "sev",
    "sey", "si", "siz", "ta", "tak", "tal", "tam", "tan", "tar", "tat", "tay",
    "te", "teb", "ten", "ter", "tes", "tet", "tev", "tey", "ti", "tü", "u",
    "ul", "un", "ut", "ün", "ür", "üst", "ya", "yak", "yan", "yap", "yat",
    "yaz", "ye", "yen", "yer", "yet", "yeş", "yıl", "yo", "yor", "yu", "yü",
    "zat", "zor", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X",
    "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX",
    "Mr", "Mrs", "No", "pp", "St", "no", "Sr", "Jr", "Bros", "etc", "vs",
    "esp", "Fig", "fig", "Jan", "Feb", "Mar", "Apr", "Jun", "Jul", "Aug",
    "Sep", "Sept", "Oct", "Okt", "Nov", "Dec", "Ph.D", "PhD", "al", "cf",
    "Inc", "Ms", "Gen", "Sen", "Prof", "Dr", "Corp", "Co", "Av", "no",
    "Başk.yard", "Bşk.yrd", "Akad", "Alb", "Alm", "anat", "ant", "Apt", "Ar",
    "Ar. Gör", "ark", "As", "Asb", "Asist", "astr", "astrol", "Atğm", "atm",
    "Av", "bağ", "Bçvş", "B.E", "bitb", "biy", "bk", "Bl", "Bn", "Bnb", "bot",
    "Böl", "bs", "Bşk", "Bul", "Bulg", "C", "Cad", "coğ", "çev", "Çvş", "D",
    "dam", "db", "dbl", "Doç", "doğ", "Dr", "Dz. Kuv. K", "dzş", "e", "Ecz",
    "ed", "ekon", "Ens", "Erm", "F", "f", "Fak", "Far", "fel", "fil", "fiz",
    "Fr", "Gen", "geom", "gn", "Gnkur", "Gön", "H.O", "Hv. Kuv", "Hv. Kuv. K",
    "Hz", "İbr", "is", "İsp", "İt", "hayır", "1", "2", "3", "4", "5", "6", "7",
    "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
    "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32",
    "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44",
    "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56",
    "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68",
    "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80",
    "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92",
    "93", "94", "95", "96", "97", "98", "99"
]


class SentenceSplitter:
    """
    SentenceSplitter is a class used for splitting a text into sentences by considering `Turkish non-breaking prefixes <https://github.com/tnltk/tnltk/blob/main/resources/TR_non_breaking_prefixes.txt>`_
     
    Methods: 
    --------
    split_sentences(text: str) : List[str]
        Split the given text into sentences by considering Turkish non-breaking prefixes.
    
    """
    def split_sentences(self, text: str) -> List[str]:
        """
        Split the given text into sentences by considering Turkish non-breaking prefixes.
        
        Parameters
        ----------
        text : str
            The input text to be split into sentences.

        Returns
        ----------
        sentences : list
            A list of sentences

        Example:
        ----------
        >>> from tnltk.sentence_splitter import SentenceSplitter
        >>> splitter = SentenceSplitter()
        >>> text = "Bu cümle bir örnektir. Bu cümle de bir örnektir!"
        >>> splitter.split_sentences(text)
        Output: ["Bu cümle bir örnektir.", "Bu cümle de bir örnektir!"]
        """

        # Create a regex pattern for prefixes
        prefix_pattern = "(" + "|".join(non_breaking_prefixes_tr) + r")\."
        # Replace all prefixes followed by a period with the prefix
        text = re.sub(prefix_pattern, r"\1", text)
        # Use the regular expression to split the text into sentences
        sentences = re.split(r"(?<=[.!?])\s", text)

        return sentences
