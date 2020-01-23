

class ToRoman():

    def __init__(self, num):
        self.arabic = [1, 4, 5, 9, 10, 40, 50, 90,
                       100, 400, 500, 900, 1000]
        self.roman = ["I", "IV", "V", "IX", "X", "XL",
                      "L", "XC", "C", "CD", "D", "CM", "M"]

        self.arabic_num = num
        self.roman_num = self.to_roman()
        self.__call__()

    def __call__(self):
        print(f"Arabic: {self.arabic_num}")
        print(f"Roman: {self.roman_num}")


    def to_roman(self):
        # we assert that the number is in range because we cannot represent
        # numbers below 1 or above 3999
        assert self.arabic_num > 0
        assert self.arabic_num < 4000
        tmp = self.arabic_num
        i = len(self.arabic) - 1 # should always be 12
        roman = ""
        while tmp:
            digit = tmp // self.arabic[i] # this gets us the most significant digit
            tmp %= self.arabic[i] # this removes the most significant digit for the next pass

            # this appends the desired number of roman numerals to the string
            roman += (self.roman[i] * digit)

            i -= 1

        return roman




if __name__ == '__main__':
    ToRoman(123)
    ToRoman(1)
    ToRoman(3)
    ToRoman(4)
    ToRoman(3999)
    ToRoman(0)
    ToRoman(5000)
