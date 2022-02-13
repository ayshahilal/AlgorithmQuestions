class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        search = image[sr][sc]
        Solution.dfs(image, sr, sc, newColor,search)
        return image
        
    def dfs(image: List[List[int]], x: int, y: int, newColor: int, search:int):
        print(x,y)
    
        if image[x][y] == newColor :
            return
        elif image[x][y] == search: 
            image[x][y] = newColor
            if x>0:
                Solution.dfs(image, x-1, y, newColor,search)
            if x<len(image)-1:
                Solution.dfs(image, x+1, y, newColor,search)
            if y>0:
                Solution.dfs(image, x, y-1, newColor,search)
            if y<len(image[0])-1:
                Solution.dfs(image, x, y+1, newColor,search)
        else: 
            return
            
            
        
        
