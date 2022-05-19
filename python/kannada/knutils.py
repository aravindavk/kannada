HALANT = "0ccd"
NO_BREAK_CHARS = [
    "0cbe", "0cbf", "0cc0", "0cc1",
    "0cc2", "0cc3", "0cc4", "0cc6",
    "0cc7", "0cc8", "0cca", "0ccb",
    "0ccc", "0ccd", "0c82", "0c83", "200d"
]


def _to_hex(letter):
    return hex(ord(letter)).replace("0x", "").zfill(4)


def _is_part_of_same_letter(out, prev_char, char):
    prev_char_halant = prev_char != "" and _to_hex(prev_char) == HALANT
    no_break_char = _to_hex(char) in NO_BREAK_CHARS

    # If the current char is one of dependent vowels or
    # previous char is Halant (That means possible Vattakshara)
    return len(out) > 0 and (no_break_char or prev_char_halant)


def letters(txt):
    """
    ## Letters

    Split the given Kannada text into letters. It handles the
    complex letters including Vattaksharas.

    ```python
    from kannada import knutils

    print(knutils.letters("ನನ್ನಂತೆ")) # ["ನ", "ನ್ನಂ", "ತೆ"]
    ```
    """
    out = []
    prev_char = ""
    for char in txt:
        if _is_part_of_same_letter(out, prev_char, char):
            out[len(out)-1] += char
        else:
            out.append(char)

        prev_char = char

    return out
