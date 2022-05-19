require "../src/*"

require "spec"

describe Kannada do
  describe ".letters" do
    it "Split Kannada Text into letters" do
      Kannada.letters("ನನ್ನಂತೆ").should eq ["ನ", "ನ್ನಂ", "ತೆ"]
    end
  end
end
