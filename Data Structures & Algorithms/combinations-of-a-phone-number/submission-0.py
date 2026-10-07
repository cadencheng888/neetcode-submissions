class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Edge case: if the input is empty, return an empty list immediately
        if not digits:
            return []

        digits_map = {
            2: ["a", "b", "c"], 3: ["d", "e", "f"], 4: ["g", "h", "i"],
            5: ["j", "k", "l"], 6: ["m", "n", "o"], 7: ["p", "q", "r", "s"], 
            8: ["t", "u", "v"], 9: ["w", "x", "y", "z"]
        }

        numbers = []
        for char in digits:
            num_char = int(char)
            numbers.append(digits_map[num_char])
            
        result = []
        path = []
        
        def backtrack(index):
            # Base case: if our path is as long as the input digits, we are done
            if len(path) == len(digits):
                result.append("".join(path))
                return
            
            # 'index' tells us which digit's letters we should loop through
            # If digits="23", when index=0, we loop through ['a', 'b', 'c']
            for letter in numbers[index]:
                path.append(letter)
                
                # Move to the NEXT digit by passing index + 1
                backtrack(index + 1)
                
                # Backtrack: remove the letter to try the next one in the loop
                path.pop()

        # Start the backtracking at the first digit (index 0)
        backtrack(0)
        return result