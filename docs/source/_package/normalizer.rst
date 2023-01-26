==================
Normalizer Package
==================

Deasciifier Module
------------------
Deasciifier is a class that allows for the conversion of an ASCII-only string to a Turkish string. The class takes in an ``ascii_string`` parameter and converts it to a ``converted_string`` attribute, taking into account the context of the surrounding characters during the conversion process. The class utilizes the ``deasciify()`` method for the conversion, which checks for necessary corrections using the ``turkish_need_correction()`` and ``turkish_toggle_accent()`` methods. The class also offers the ability to replace a specific character at a given position using the ``set_char_at()`` method. This class is useful for making Turkish strings written with ASCII equivalents more readable. Additionally, it has methods to get context of a point and match pattern in the text which makes it more powerful.

* **Improved Readability:** The Deasciifier class allows for the conversion of ASCII-only Turkish strings to their true Turkish character equivalents, making the resulting text more readable for Turkish speakers.
* **Contextual Conversion:** The class takes into account the surrounding characters during the conversion process, ensuring that the resulting text is grammatically and semantically correct.
* **Additional Functionality:** The class provides additional functionalities such as getting context of a point, matching pattern in the text and replacing a specific character at a given position which makes it more powerful and versatile.


.. autoclass:: tnltk.normalizer.deasciifier.Deasciifier
   :exclude-members: turkish_match_pattern
   :members:


Normalizer Module
-----------------
The Normalizer module is a collection of static methods that allow for the normalization of text in Turkish language. It includes methods for ``converting text to lowercase``, ``removing punctuation`` and ``accent marks`` and ``converting numbers to words``. The module utilizes a combination of built-in Python functions and regular expressions to achieve these normalizations. Each method takes in a string of text as an input and returns the normalized version of the text. The module also includes a built-in functions at ``_normalizer_builtin module`` for converting numbers to words in Turkish language. Overall, this module is useful for preparing text for further processing, such as natural language understanding and machine learning tasks.

* **Advanced  Context-aware Replacements:** The class is able to replace specific characters at a given position, taking into account the context of the surrounding characters. This ensures that the resulting text is grammatically and semantically correct, and makes the text more natural and readable.
* **Flexibility:** The class can be easily integrated into various NLP tasks such as text classification, sentiment analysis and text summarization.
* **Language Specific:** The class is specifically designed to handle Turkish text, and is able to handle the unique characteristics and complexities of the language. This makes it more accurate and efficient compared to general-purpose normalization methods that do not take into account the specific language.

.. autoclass:: tnltk.normalizer.normalizer.Normalizer
   :members: