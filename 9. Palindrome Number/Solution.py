class Solution:
    def isPalindrome(self, x: int) -> bool:
        forward = []
        backward = []
        string = str(x)
        for i in string: 
            forward.append(i)
        for j in reversed(string): 
            backward.append(j)
        if "".join(forward) == "".join(backward): 
            return True 
        else: 
            return False 