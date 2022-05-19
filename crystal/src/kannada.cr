module Kannada
  extend self

  HALANT = "0ccd"
  NO_BREAK_CHARS = [
    "0cbe", "0cbf", "0cc0", "0cc1",
    "0cc2", "0cc3", "0cc4", "0cc6",
    "0cc7", "0cc8", "0cca", "0ccb",
    "0ccc", "0ccd", "0c82", "0c83", "200d"
  ]


  private def to_hex(letter)
    "%04s" % letter.char_at(0).ord.to_s(16)
  end

  private def part_of_same_letter?(data, prev_char, char)
    prev_char_halant = prev_char != "" && to_hex(prev_char) == HALANT
    no_break_char = NO_BREAK_CHARS.includes?(to_hex(char))

    # If the current char is one of dependent vowels or
    # previous char is Halant (That means possible Vattakshara)
    data.size > 0 && (no_break_char || prev_char_halant)
  end

  # ## Letters
  #
  # Split the given Kannada text into letters. It handles the
  # complex letters including Vattaksharas.
  #
  # ```crystal
  # require "kannada"
  #
  # puts Kannada.letters("ನನ್ನಂತೆ") # ["ನ", "ನ್ನಂ", "ತೆ"]
  # ```
  def letters(txt)
    data = [] of String
    prev_char = ""
    txt.split("").each do |char|
      if part_of_same_letter?(data, prev_char, char)
        data[-1] += char
      else
        data << char
      end

      prev_char = char
    end
    data
  end
end
