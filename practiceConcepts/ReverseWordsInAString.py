class Solution:
    def reverseWords(self, s: str) -> str:
        word = ""
        output = ""
        for i, char in enumerate(s):
            # print("word: " , word, len(word))
            if char == ' ' and word != "":
                if output == "":
                    output = word
                    # print("was here")
                else:
                    # print("was here")
                    output = word + ' ' + output
                word = ""
            elif i == len(s) -1 and char != ' ':
                if output == "":
                    output = word + char
                else:
                    output = word + char + ' ' + output
            elif char != ' ':
                word += char
            # print("output", output, len(output))
                
        return output
        