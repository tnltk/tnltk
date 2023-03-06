import re
from typing import List

with open("../../resources/TR_non_breaking_prefixes.txt", "r", encoding="utf-8") as file:
    non_breaking_prefixes_tr = file.read().splitlines()

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
        >>> from tnltk import SentenceSplitter
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
