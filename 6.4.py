print("ĐẬU THẾ HOÀNG")
print("MSSV:235752021610017")
class RomanToInteger:
    def __init__(self):
        self.roman_to_int = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }

    def romanToInt(self, s):
        result = 0
        prev_value = 0
        for i in range(len(s) - 1, -1, -1):
            current_value = self.roman_to_int[s[i]]
            if current_value >= prev_value:
                result += current_value
            else:
                result -= current_value
            prev_value = current_value
        return result


converter = RomanToInteger()
roman_numeral = "MDCLXVI"
integer = converter.romanToInt(roman_numeral)
print(integer)  
