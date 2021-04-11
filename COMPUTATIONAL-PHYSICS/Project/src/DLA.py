# Stickiness factor

from walkers_grid import WalkersGrid


class DLA(WalkersGrid):
    def __init__(self, size):
        super().__init__(size)


if __name__ == "__main__":
    size = 100
    dla_original = DLA(size=100)
