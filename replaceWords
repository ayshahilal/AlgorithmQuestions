class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split()
        newSentence = []
        for word in words:
            found = False
            for i in range(len(word)):
                if word[:i] in dictionary:
                    found = True
                    newSentence.append(word[:i])
                    break
            if found == False:
                newSentence.append(word)
 
        return " ".join(newSentence) 
    
                
            
            
