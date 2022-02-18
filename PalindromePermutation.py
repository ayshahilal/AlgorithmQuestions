def isPalindromePer(s1):
    s1.upper()
    chars = {}
    for char in s1:
        if char in chars.keys():
            chars[char] += 1
        else:
            chars[char] = 1
    print(chars.values())
    count = 0
    
    for val in chars.values():
        if val%2 != 0:
            count +=1
    if count > 1:
        return False
    return True
            

    
if __name__ =='__main__':
    s1 = "tactcxoapapa"
   
    print(isPalindromePer(s1))
    
