import logging
from typing import Tuple, List
import matplotlib.pyplot as plt
import numpy as np

from src.tools import logs_file_setup, set_seed
from walkers_grid import WalkersGrid
from animation import Animation
from theoretical_tools import plot_mean_displacement



import sys
np.set_printoptions(threshold=sys.maxsize)


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
            number_of_steps: int,
            show_animation: bool
    ) -> Tuple[int, int]:
        """
        This function performs a random walk starting from a given position.

        Parameters
        ----------
        initial_position (Tuple[int, int]): The starting position (x, y).
        number_of_steps (int): The number of steps on the grid the walker must do.
        show_animation (bool): Display animation

        Returns
        -------
        current_position (Tuple[int, int]): The final position (x, y).
        """
        self.set_state(position=initial_position, state=1, add_new_walker=True)

        # ---------------------------------------------------------------------
        # Will be replaced by the corresponding function of the animation class
        # plt.imshow(self.state, cmap='CMRmap')
        # plt.show()
        # ---------------------------------------------------------------------

        current_position = initial_position
        state_frame = []
        position_frame =[]

        for step in range(number_of_steps):

            frame = self.state.copy()
            state_frame.append(frame)

            position_grid = WalkersGrid(grid_size=self.grid_size)
            position_grid.set_state(position=current_position, state=1, add_new_walker=False)
            position_frame.append(position_grid.state)

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

        frame = self.state.copy()
        state_frame.append(frame)

        position_grid = WalkersGrid(grid_size=self.grid_size)
        position_grid.set_state(position=current_position, state=1, add_new_walker=False)
        position_frame.append(position_grid.state)



        # ---------------------------------------------------------------------
        # Will be replaced by the corresponding function of the animation class
        if show_animation:
            animate = Animation()
            animate.brownian_motion_animation(state_frame, position_frame, 30)
        # ---------------------------------------------------------------------

        return current_position

    def show_final_distances(
            self,
            initial_position: Tuple[int, int],
            number_of_steps: int,
            number_of_walkers: int
    ):
        distance = []
        for walker in range(number_of_walkers):
            last_position = self.random_walk(
                initial_position=initial_position,
                number_of_steps=number_of_steps,
                show_animation=False
            )
            distance.append(np.linalg.norm(np.asarray(last_position) - np.asarray(initial_position)))
        print(np.mean(distance))
        print(np.sqrt(np.mean(np.asarray(distance)**2)))

        plot_mean_displacement(distance=np.asarray(distance))




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

    nb_steps = 100

    logging.info(f"Initial position is {initial_walker_position}.")
    logging.info(f"The total number of steps is {nb_steps}.")
    # ----------------------------------------------------------------------------------------------------------- #
    #                                      Brownian Motion                                                        #
    # ----------------------------------------------------------------------------------------------------------- #
    brownian = BrownianMotion(grid_size=grid_size)
    brownian.random_walk(initial_position=initial_walker_position, number_of_steps=nb_steps, show_animation=True)
    brownian.show_final_distances(initial_position=initial_walker_position, number_of_steps=nb_steps, number_of_walkers=1000)
