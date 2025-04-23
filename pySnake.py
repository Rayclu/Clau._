import random
class SnakeGame:
    def __init__(self, type_fruit:dict, DefaultSnakeLen = 1):
        
        self.random_fruit = type_fruit.get(random.randint(0, len(type_fruit)-1), 1)
        self.snake = DefaultSnakeLen
        self.limits = (int(input("X:")), int(input("Y:")))
        self.grid = [[0 for _ in range(0, self.limits[0])] for _ in range(0, self.limits[1])]
        self.leny = len(self.grid)
        self.lenx = len(self.grid[0])

    @classmethod()
    def put_fruits(self, grid:list)-> list:
        from random import randint
        def get_coords(grid):
            x = randint(0, len(grid[0])-1)
            y = randint(0, len(grid)-1)
            return x,y

        x,y = get_coords(grid)
        grid[y][x] = self.random_fruit
        return grid
    



    
    