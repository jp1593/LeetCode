class Solution:
    def reverse(self, x: int) -> int:
        string = str(x)
        reverse = []
        for digit in reversed(string):
            if digit == "-":
                reverse.insert(0, digit)
            else:
                reverse.append(digit)
        reverse_string = "".join(reverse)
        if int(reverse_string) > 2**31 or int(reverse_string) < -2**31: 
            return 0
        return int(reverse_string)
