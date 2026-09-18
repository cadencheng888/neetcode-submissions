class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digitsString = ""
        for num in digits:
            digitsString += str(num)
        digitsNum = int(digitsString) + 1
        digitsString = str(digitsNum)
        result = []
        for char in digitsString:
            result.append(int(char))
        return result