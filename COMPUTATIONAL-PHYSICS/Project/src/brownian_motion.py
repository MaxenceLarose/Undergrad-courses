import logging
from typing import Tuple
import matplotlib.pyplot as plt
import numpy as np

from src.tools import logs_file_setup
from walkers_grid import WalkersGrid
from animation import Animation
from theoretical_tools import plot_distance_distribution, plot_2d_displacement


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
            show_animation: bool = False,
            show_last_frame: bool = False,
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
        # Create walker at initial position.
        self.set_state(position=initial_position, state=1, add_new_walker=True)

        current_position = initial_position

        # create lists to save different frames of the grid.
        state_frame = []
        position_frame = []
        position_sum = 0

        # random walk loop for the number of steps chosen.
        for step in range(number_of_steps):

            # Set a secondary grid to keep track of current position.
            position_grid = WalkersGrid(grid_size=self.grid_size)
            position_grid.set_state(position=current_position, state=1, add_new_walker=False)

            # Add current position and grid state for figure purposes.
            frame = self.state.copy()
            if show_animation:
                state_frame.append(frame)
                position_frame.append(position_grid.state)
            if show_last_frame:
                position_sum += position_grid.state

            # Get adjacent position of the walker
            adjacent_positions = self.get_adjacent_positions(
                position=current_position,
                filter_positions_outside_bounds=True,
                filter_diagonal=True
            )

            # Decide where the walker will go next in it's adjacent positions.
            next_position = self.get_random_adjacent_position(
                adjacent_positions=adjacent_positions,
                avoid_other_walkers=False,
                )

            # Set the state of the grid for the walkers new position.
            self.set_state(
                position=next_position,
                state=1,
                add_new_walker=False
            )

            current_position = next_position

        # Set a secondary grid to keep track of last position.
        position_grid = WalkersGrid(grid_size=self.grid_size)
        position_grid.set_state(position=current_position, state=1, add_new_walker=False)

        # Add current position and grid state for figure purposes and animate.
        animate = Animation()
        if show_animation:
            frame = self.state.copy()
            state_frame.append(frame)
            position_frame.append(position_grid.state)

            # Animation function.
            animate.brownian_motion_animation(state_frame, position_frame, 60)
            plt.close()

        if show_last_frame:
            position_sum += position_grid.state

            # Plot last frame.
            plt.imshow(self.state + position_sum, cmap=animate.colormap(reverse = False), vmin = 1,
                       vmax = np.amax(position_sum + self.state))

            cbar = plt.colorbar()
            cbar.set_label('Time spent on position [frame]', rotation=270, labelpad = 15)

            plt.savefig(f'BM_{self.grid_size}grid_{number_of_steps}step.pdf', dpi = 300, bbox_inches = 'tight')
            plt.show()
            plt.close()

        return current_position

    def show_traveled_distances(
            self,
            initial_position: Tuple[int, int],
            number_of_steps: int,
            number_of_walkers: int,
            size: int
    ):
        """
        This functions is used to perform multiple random walks to plot the distribution of the distance traveled by the
        walkers.

        Parameters
        ----------
        initial_position (Tuple[int, int]): The starting position (x, y).
        number_of_steps (int): The number of steps on the grid the walker must do.
        number_of_walkers (int): The total number of random walks performed.
        size (int): Square grid size.

        Returns
        -------
        Fig and axes.
        """
        distance = []
        last_positions = []
        for walker in range(number_of_walkers):
            if (walker % 10) == 0:
                print(walker)
            last_position = self.random_walk(
                initial_position=initial_position,
                number_of_steps=number_of_steps,
                show_animation=False
            )
            distance.append(np.linalg.norm(np.asarray(last_position) - np.asarray(initial_position)))
            last_positions.append(last_position)

        plot_distance_distribution(
            distance=distance,
            nb_steps=nb_steps,
            number_of_walkers=number_of_walkers
        )

        plot_2d_displacement(
            last_positions=last_positions,
            nb_steps=nb_steps,
            grid_size=size,
            number_of_walkers=number_of_walkers
        )


if __name__ == "__main__":
    # ----------------------------------------------------------------------------------------------------------- #
    #                                      Logs Setup                                                             #
    # ----------------------------------------------------------------------------------------------------------- #
    logs_file_setup(__file__, logging.INFO)

    # ----------------------------------------------------------------------------------------------------------- #
    #                                       Constants                                                             #
    # ----------------------------------------------------------------------------------------------------------- #
    grid_size = 201
    center = int((grid_size - 1)/2)
    initial_walker_position = (center, center)
    show_traveled_distances_distribution = False
    loop = False
    nb_steps = 1000

    logging.info(f"Initial position is {initial_walker_position}.")
    logging.info(f"The total number of steps is {nb_steps}.")
    # ----------------------------------------------------------------------------------------------------------- #
    #                                      Brownian Motion                                                        #
    # ----------------------------------------------------------------------------------------------------------- #
    brownian = BrownianMotion(grid_size=grid_size)

    brownian.random_walk(
        initial_position=initial_walker_position,
        number_of_steps=nb_steps,
        show_animation=True,
        show_last_frame=True
    )

    if show_traveled_distances_distribution:
        brownian.show_traveled_distances(
            initial_position=initial_walker_position,
            number_of_steps=nb_steps,
            number_of_walkers=10000,
            size=grid_size
        )

    if loop:
        steps = np.arange(100, 1100, 100)
        grid_size = np.arange(101, 505, 101)
        for size in grid_size:
            for step in steps:
                center = int((size - 1) / 2)
                initial_walker_position = (center, center)
