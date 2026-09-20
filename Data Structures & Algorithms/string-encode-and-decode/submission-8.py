class Solution:

    def encode(self, strs: List[str]) -> str:
        self.encoded = ""
        for string in strs:
            self.encoded += str(len(string))
            self.encoded += "#"
            for char in string:
                self.encoded += char
        return self.encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        index = 0
        while index < len(s):
            print("hi")
            lenIndex = index
            lenStr = ""
            while s[lenIndex] != "#":
                lenStr += s[lenIndex]
                lenIndex += 1
                print(lenStr)

            index = lenIndex

            if s[index] == "#":
                length = int(lenStr)
                index += 1
                word = ""
                for i in range(length):
                    word += s[index]
                    index += 1
                decoded.append(word)
        return decoded