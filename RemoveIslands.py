
class RemoveIslands:


    def is_border(i,j,matrix):
        if i == 0 or i == (len(matrix)-1) or j == 0 or j == (len(matrix[0])-1) :
            return True
        return False

        
    def is_out_matrix(i,j,matrix):
        if i < 0 or i > (len(matrix)-1) or j < 0 or j > (len(matrix[0])-1):
            return True
        return False

        
    def removeIslands(matrix):
        # 1 black, 0 white
        
        row = len(matrix)
        col = len(matrix[0])

        islands = {}

        for i in range(row):
            for j in range(col):
                if RemoveIslands.is_border(i,j,matrix) and matrix[i][j] == 1:
                    islands[i,j] = True
                    RemoveIslands.dfs(islands,matrix, i, j)
    
            
        for i in range(row):
            for j in range(col):
                if matrix[i][j]== 1 and (i,j) not in islands.keys():
                    matrix[i][j] = 0

        return matrix

    

    def dfs(islands,matrix, i, j):

        steps = [
            (0,1),
            (1,0),
            (0,-1),
            (-1,0)
            ]
        
        for (x,y) in steps:
            new_i = i + x
            new_j = j + y
        
            if RemoveIslands.is_out_matrix(new_i, new_j,matrix):
                continue
            neighbour = matrix[new_i][new_j]
            if (new_i,new_j) not in islands.keys() and neighbour == 1:
                islands[new_i,new_j] = True
                RemoveIslands.dfs(islands, matrix, new_i, new_j)
                
        


if __name__ == '__main__':


    matrix = [[1,0,0,0,0,0],
              [0,1,0,1,1,1],
              [0,0,1,0,1,0],
              [1,1,0,0,1,0],
              [1,0,1,1,0,0],
              [1,0,0,0,0,1],
              ]

    matrix = RemoveIslands.removeIslands(matrix)

    print(matrix)
