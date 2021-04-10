# Stickiness factor

from grid_environment import GridEnvironment


class DLA(GridEnvironment):
    def __init__(self, size):
        super().__init__(size)


if __name__ == "__main__":
    size = 100
    dla_original = DLA(size=100)
