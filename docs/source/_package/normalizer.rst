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
   :exclude-members: set_char_at, turkish_get_context, turkish_need_correction, turkish_toggle_accent, turkish_match_pattern
   :members:


Normalizer Module
-----------------
.. autoclass:: tnltk.normalizer.normalizer.Normalizer
   :members: