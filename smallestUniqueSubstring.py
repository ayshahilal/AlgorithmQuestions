class Solution:
    
    def smallestUniqueSubstring(arr, string):

        arrMap = {}
        index = 0
        substring = ""
   
        while index < len(string):
            ch = string[index]
            
            if ch not in arrMap:
                arrMap[ch] = index
                index += 1
                
            elif ch in arrMap:
                index = arrMap[ch] + 1
                arrMap = {} 
                
            if len(arrMap) == len(arr):
                for key in arrMap.keys():
                    substring += key
                return substring
        
        return ""
               
            

if __name__ == '__main__':
    arr  = ['x', 'y', 'z']
    string = "xyyzyzyxz"
    a = Solution.smallestUniqueSubstring(arr, string)
    print("Substring:", a)
