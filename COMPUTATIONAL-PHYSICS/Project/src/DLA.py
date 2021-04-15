# Stickiness factor
import logging
from typing import Tuple, List
import matplotlib.pyplot as plt
import numpy as np

from walkers_grid import WalkersGrid
from src.tools import logs_file_setup, set_seed
from animation import Animation


class DLA(WalkersGrid):
    def __init__(self, **kwargs):
        """
        Constructor of the class DLA.

        Parameters
        ----------
        kwargs: {
            grid_size (int): Square grid size. Default = 101.
        }
        """
        super().__init__(kwargs.get("grid_size", 101))

    def dla_cluster(
            self,
            initial_position: Tuple[int, int],
            log_cluster_every_n_iterations: int,
            log_every_random_walk: bool = False,
            show_animation: bool = False,
            show_last_frame: bool = False,
    ):
        """
        This function uses the DLA process to create fractal structures called Brownian trees as walkers aggregate into
        clusters during the diffusion process.

        Parameters
        ----------
        initial_position (Tuple[int, int]): The starting position (x, y).
        log_cluster_every_n_iterations (int): Display cluster formed by the walkers every n iterations.
        log_every_random_walk (bool): Display or not the figure of the random walk performed by each walkers added to
                                       the structure.

        Returns
        -------
        Fig and axes.
        """
        # create lists to save different frames of the grid.
        state_frame = []
        frame_sum = 0

        # DLA loop.
        complete_cluster = False
        while not complete_cluster:
            current_position = initial_position
            complete_random_walk = False

            # Add grid state for figure purposes.
            frame = self.state.copy()
            if show_animation:
                state_frame.append(frame)
            if show_last_frame:
                frame_sum += frame

            if log_every_random_walk:
                walker_grid = WalkersGrid(grid_size=self.grid_size)
                walker_grid.set_state(position=current_position, state=1, add_new_walker=True)

            # random walk loop the latest added walker.
            while not complete_random_walk:

                # Get adjacent position of the walker
                adjacent_positions = self.get_adjacent_positions(position=current_position,
                                                                 filter_positions_outside_bounds=False
                                                              )
                # Check if random walk is completed
                complete_random_walk = self.check_walk_terminate_conditions(adjacent_positions)

                # Decide where the walker will go next in it's adjacent positions.
                next_position = self.get_random_adjacent_position(
                    adjacent_positions=adjacent_positions,
                    avoid_other_walkers=False,
                )

                # Decide walker's current position according to criteria.
                if complete_random_walk:
                    pass
                else:
                    current_position = next_position

                #
                if log_every_random_walk:
                    walker_grid.set_state(position=current_position, state=1, add_new_walker=False)

            #
            if log_every_random_walk:
                logging.info(f"Current number of walkers: {self.walkers_count}")

            # Set grid state for walker last position.
            self.set_state(
                position=current_position,
                state=1,
                add_new_walker=True
            )

            # Check if the cluster is completed according to criteria.
            complete_cluster = self.check_dla_terminate_condition(
                initial_position=initial_position,
                final_position=current_position
            )

            # Log the number of added walkers at each chosen number of walkers added.
            if (self.walkers_count % log_cluster_every_n_iterations) == 0:
                logging.info(f"Current number of walkers: {self.walkers_count}")

        # Log total walkers added to complete cluster.
        logging.info(f"Total number of walkers: {self.walkers_count}")

        # Add current position and grid state for figure purposes and animate.
        frame = self.state.copy()
        if show_animation:
            state_frame.append(frame)

            # Animation function.
            animate = Animation()
            animate.DLA_animation(state_frame, 30)

        if show_last_frame:
            frame_sum += frame
            nonzero = np.nonzero(frame_sum)
            maximum = np.amax(frame_sum)
            for (x, y) in zip(*nonzero):
                frame_sum[x, y] = -1 * (frame_sum[x, y] - maximum)

            # Plot last frame.
            plt.imshow(frame_sum, cmap='CMRmap', vmin = 0, vmax = maximum)
            plt.show()




    def check_walk_terminate_conditions(
            self,
            adjacent_positions: List[tuple],
    ) -> bool:
        """
        Check if the random walk must be terminated. The random walk must be terminated if an adjacent position is
        occupied by a walker (state = 1) or if an adjacent position is outside the grid (walker reaches one of the
        sides of the grid).

        Parameters
        ----------
        adjacent_positions (List[tuple, ..., tuple]): List of all the adjacent positions.

        Returns
        -------
        terminate (bool): Terminate random walk.
        """

        # Check if walker is in a valid position (grid edge) or adjacent to other walker to complete random walk.
        if not all(list(map(lambda location: self.validate_position(location), adjacent_positions))):
            terminate = True
        elif any(list(map(lambda location: self.state[location] == 1, adjacent_positions))):
            terminate = True
        else:
            terminate = False

        return terminate

    @staticmethod
    def check_dla_terminate_condition(
            initial_position: Tuple[int, int],
            final_position: Tuple[int, int]
    ) -> bool:
        """
        Check if the DLA process must be terminated. The DLA process must be terminated if a walker reaches the initial
        position after its random walk.

        Parameters
        ----------
        initial_position (Tuple[int, int]): The starting position (x, y).
        final_position (Tuple[int, int]): The final position (x, y).

        Returns
        -------
        terminate (bool): Terminate DLA process.
        """

        # Check if the last position of the latest added walker is the initial position (center of the grid).
        if final_position == initial_position:
            terminate = True
        else:
            terminate = False

        return terminate


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

    LOG_CLUSTER_EVERY_N_ITERATIONS = 300

    logging.info(f"Initial position is {initial_walker_position}.")
    # ----------------------------------------------------------------------------------------------------------- #
    #                                            DLA                                                              #
    # ----------------------------------------------------------------------------------------------------------- #
    dla = DLA(grid_size=grid_size)

    dla.dla_cluster(
        initial_position=initial_walker_position,
        log_cluster_every_n_iterations=LOG_CLUSTER_EVERY_N_ITERATIONS,
        log_every_random_walk=False,
        show_animation = True,
        show_last_frame = True,
    )
