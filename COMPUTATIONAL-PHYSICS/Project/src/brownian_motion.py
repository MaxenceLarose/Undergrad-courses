from grid_environment import GridEnvironment
from animation import Animation


class Brownian_Motion(GridEnvironment):
    def __init__(self, size):
        super().__init__(size)


if __name__ == "__main__":
    size = 100
    brownian = Brownian_Motion(size=size)
