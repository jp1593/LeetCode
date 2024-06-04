class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = int(''.join(map(str, digits)))
        addition = number + 1
        output = list(map(int, str(addition)))
        return output