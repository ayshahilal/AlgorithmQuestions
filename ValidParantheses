class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {")":"(",
                     "]":"[",
                     "}":"{"
                     }
        queue = []
        for character in s:
            if character in dictionary.values():
                queue.append(character)
            elif character in dictionary.keys():
                if queue:
                    flag = Solution.checkQue(queue, character, dictionary)
                    if flag == False:
                        return False
                else:
                    return False
        if queue:
            return False
        else: 
            return True
    
    def checkQue(queue, character, dictionary):
        if queue.pop() != dictionary[character]:
            return False
        else:
            return True
