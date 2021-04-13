import logging
from typing import Tuple
import matplotlib.pyplot as plt

from src.tools import logs_file_setup, set_seed
from walkers_grid import WalkersGrid
from animation import Animation


class BrownianMotion(WalkersGrid):
    def __init__(self, **kwargs):
        """
        Constructor of the class BrownianMotion.

        Parameters
        ----------
        kwargs: {
            grid_size (int): Square grid size. Default = 101.
        }
        """
        super().__init__(kwargs.get("grid_size", 101))

    def random_walk(
            self,
            initial_position: Tuple[int, int],
            number_of_steps: int
    ):
        """
        This function performs a random walk starting from a given position.

        Parameters
        ----------
        initial_position (Tuple[int, int]): The starting position (x, y).
        number_of_steps (int): The number of steps on the grid the walker must do.

        Returns
        -------
        None
        """
        self.set_state(position=initial_position, state=1, add_new_walker=True)

        # ---------------------------------------------------------------------
        # Will be replaced by the corresponding function of the animation class
        plt.imshow(self.state, cmap='gray')
        plt.show()
        # ---------------------------------------------------------------------

        current_position = initial_position

        for step in range(number_of_steps):
            adjacent_positions = self.get_adjacent_positions(
                position=current_position,
                filter_positions_outside_bounds=True,
                filter_diagonal=True
            )

            next_position = self.get_random_adjacent_position(
                adjacent_positions=adjacent_positions,
                avoid_other_walkers=False,
                )

            self.set_state(
                position=next_position,
                state=1,
                add_new_walker=False
            )

            current_position = next_position

        # ---------------------------------------------------------------------
        # Will be replaced by the corresponding function of the animation class
        plt.imshow(self.state, cmap='gray')
        plt.show()
        # ---------------------------------------------------------------------


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

    nb_steps = 1000

    logging.info(f"Initial position is {initial_walker_position}.")
    logging.info(f"The total number of steps is {nb_steps}.")
    # ----------------------------------------------------------------------------------------------------------- #
    #                                      Brownian Motion                                                        #
    # ----------------------------------------------------------------------------------------------------------- #
    brownian = BrownianMotion()
    brownian.random_walk(initial_position=initial_walker_position, number_of_steps=nb_steps)
