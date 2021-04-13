# Stickiness factor

from animation import Animation
from walkers_grid import WalkersGrid


class DLAOriginal(WalkersGrid):
    def __init__(self, size):
        super().__init__(size)


if __name__ == "__main__":
    size = 100
    dla_original = DLAOriginal(size=size)
    # Stickiness factor
