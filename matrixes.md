# Matrixes

Matrixes are nested 2 dimensional arrays arranged in rows and columns. 
We'll focus on matrixes typically being represented as graphs and how to approach/traverse these problems.

### coordinates of a 4x5 matrix

|-- |-- |-- |-- |-- |
|:--|:--|:--|:--|:--|  
|0,0|0,1|0,2|0,3|0,4|
|1,0|1,1|1,2|1,3|1,4|
|2,0|2,1|2,2|2,3|2,4|
|3,0|3,1|3,1|3,3|3,4|


in an m * n matrix we traverse the matrix using 2 loops. 
    - the outer loop represents the current row
    - the inner loop represents the current column

```python

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            print(f'the current coordinates of the matrix are ({row}, {col}) - row:{row}, col: {col}')

```

#### moving in 4 directions

    - going right `-->` we add (0,1) to our current coordinates
    - going left  `<--` we add (0,-1) to our current coordinates
    - going down  `V` we add (1,0) to our current coordinates
    - going up    `^` we add (-1,0) to our current coordinates

    we can manually add these 4 directions in code or we can create a list of tuples representing each direction

    `directions = [(0,1), (0,-1), (1,0), (-1,0)] # right, left, down, up`

```python

    # matrix traversal going all 4 directions in DFS 

    matrix = [[0, 1, 0, 1],
              [1, 1, 0, 1],
              [0, 0, 0, 0]]

    visited = set() # set of tuples(row, col)

    def dfs(row, col, matrix, visited):
        # check to make sure we are inbounds of the matrix
        if row >= 0 and row < len(matrix) and col >= 0 and col < len(matrix[0]):
            # check to make sure we have not visited the current coordinate to avoid infinite loops
            if (row, col) not in visited:
                print(f'({row},{col})')
                visited.add(row, col)
                dfs(row + 1, col, matrix, visited) # Right
                dfs(row - 1, col, matrix, visited) # Left
                dfs(row, col + 1, matrix, visited) # Down
                dfs(row, col - 1, matrix, visited) # Up

    # matrix traversal using directions tuple 

    directions = [(0,1), (0,-1), (1,0), (-1,0)] # right, left, down, up

    def dfs_with_directions(row, col, matrix, visited, directions):
        # same logic of checking we're inbounds of the matrix and that we havent visited coordinates, but more condensed
        if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]) and (row, col) not in visited:
            print(f'({row},{col})')
            visited.add(row, col)
            for inc_row, inc_col in directions: 
                new_row = row + inc_row
                new_col = col + inc_col
                dfs(new_row, new_col, matrix, visited, directions)

```


### moving in 8 directions

    - south east    ↘   add (1,1) to current coordinates
    - north east    ↗   add (-1,1) to current coordinates
    - south west    ↙   add (-1,-1) to current coordinates
    - north west    ↖   add (1,-1) to current coordinates
