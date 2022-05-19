import re

import kannada
from kannada import knutils


def fix_doc_indent(txt):
    """Replace first four space"""
    lines = txt.split("\n")
    return "\n".join([re.sub("^    ", "", line) for line in lines])

print(kannada.__doc__)

for attr_name in dir(knutils):
    # Ignore internal functions
    if attr_name.startswith("_"):
        continue

    attr = getattr(knutils, attr_name)
    # Ignore if it is not callable or empty doc.
    if callable(attr) and attr.__doc__ is not None:
        print(fix_doc_indent(attr.__doc__))
