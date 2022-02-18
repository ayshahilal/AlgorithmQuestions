class Solution:
    def lengthOfLongestSubstring(s):

        maxlen = 0
        charIndexMap = {}
        end = 0
        while end<len(s):
            ch = s[end]       
            if ch not in charIndexMap:
                charIndexMap[ch] = end
                end = end+1
            else:
                maxlen = max(end-start, maxlen)
                start = charIndexMap[ch]+1
                end = charIndexMap[ch]+1
                charIndexMap = {}
        maxlen = max(len(charIndexMap), maxlen)
        return maxlen    
            
            

if __name__ == '__main__':
    a = Solution.lengthOfLongestSubstring("jbbhsdoke")
    print(a)
