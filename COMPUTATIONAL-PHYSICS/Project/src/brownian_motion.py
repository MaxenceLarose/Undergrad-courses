import logging
import matplotlib.pyplot as plt

from src.tools import logs_file_setup
from grid_environment import GridEnvironment
from animation import Animation


class BrownianMotion(GridEnvironment):
    def __init__(self, **kwargs):
        super().__init__(kwargs.get("grid_size", 101))

    def random_walk(self, position, walk_length: int):
        self.set_state(position=position, state=1, add_new_walker=True)
        plt.imshow(self.state, cmap='gray')
        plt.show()

        current_position = position

        for jump in range(walk_length):
            next_position = self.get_random_next_position(
                position=current_position,
                avoid_other_walkers=False,
                filter_positions_outside_bounds=True,
                filter_diagonal=True
                )

            self.set_state(
                next_position,
                state=1,
                add_new_walker=False
            )

            current_position = next_position

        plt.imshow(self.state, cmap='gray')
        plt.show()


if __name__ == "__main__":
    # ----------------------------------------------------------------------------------------------------------- #
    #                                      Logs Setup                                                             #
    # ----------------------------------------------------------------------------------------------------------- #
    logs_file_setup(__file__, logging.INFO)

    # ----------------------------------------------------------------------------------------------------------- #
    #                                       Constants                                                             #
    # ----------------------------------------------------------------------------------------------------------- #
    grid_size = 101
    center = int((grid_size - 1)/2)
    initial_walker_position = (center, center)

    logging.info(f"Initial position is {initial_walker_position}")

    # ----------------------------------------------------------------------------------------------------------- #
    #                                      Brownian Motion                                                        #
    # ----------------------------------------------------------------------------------------------------------- #
    brownian = BrownianMotion()
    brownian.random_walk(position=initial_walker_position, walk_length=1000)

