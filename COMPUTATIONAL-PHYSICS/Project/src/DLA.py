# Stickiness factor
import logging
from typing import Tuple, List
import matplotlib.pyplot as plt

from walkers_grid import WalkersGrid
from src.tools import logs_file_setup, set_seed


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
            show_cluster_every_n_iterations: int,
            show_every_random_walk: bool = False
    ):
        """
        This function uses the DLA process to create fractal structures called Brownian trees as walkers aggregate into
        clusters during the diffusion process.

        Parameters
        ----------
        initial_position (Tuple[int, int]): The starting position (x, y).
        show_cluster_every_n_iterations (int): Display cluster formed by the walkers every n iterations.
        show_every_random_walk (bool): Display or not the figure of the random walk performed by each walkers added to
                                       the structure.

        Returns
        -------
        Fig and axes.
        """
        complete_cluster = False
        while not complete_cluster:
            current_position = initial_position
            complete_random_walk = False

            if show_every_random_walk:
                walker_grid = WalkersGrid(grid_size=self.grid_size)
                walker_grid.set_state(position=current_position, state=1, add_new_walker=True)

            while not complete_random_walk:
                adjacent_positions = self.get_adjacent_positions(position=current_position,
                                                                 filter_positions_outside_bounds=False
                                                                 )
                complete_random_walk = self.check_walk_terminate_conditions(adjacent_positions)

                next_position = self.get_random_adjacent_position(
                    adjacent_positions=adjacent_positions,
                    avoid_other_walkers=False,
                )

                if complete_random_walk:
                    pass
                else:
                    current_position = next_position

                if show_every_random_walk:
                    walker_grid.set_state(position=current_position, state=1, add_new_walker=False)

            if show_every_random_walk:
                # ---------------------------------------------------------------------
                # Will be replaced by the corresponding function of the animation class
                plt.imshow(walker_grid.state, cmap='gray')
                plt.show()
                # ---------------------------------------------------------------------

            self.set_state(
                position=current_position,
                state=1,
                add_new_walker=True
            )

            complete_cluster = self.check_dla_terminate_condition(
                initial_position=initial_position,
                final_position=current_position
            )

            if (self.walkers_count % show_cluster_every_n_iterations) == 0:
                logging.info(f"Current number of walkers: {self.walkers_count}")

                # ---------------------------------------------------------------------
                # Will be replaced by the corresponding function of the animation class
                plt.imshow(self.state, cmap='gray')
                plt.show()
                # ---------------------------------------------------------------------

        logging.info(f"Total number of walkers: {self.walkers_count}")
        # ---------------------------------------------------------------------
        # Will be replaced by the corresponding function of the animation class
        plt.imshow(self.state, cmap='gray')
        plt.show()
        # ---------------------------------------------------------------------

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

    SHOW_CLUSTER_EVERY_N_ITERATIONS = 300

    logging.info(f"Initial position is {initial_walker_position}.")
    # ----------------------------------------------------------------------------------------------------------- #
    #                                            DLA                                                              #
    # ----------------------------------------------------------------------------------------------------------- #
    dla = DLA(grid_size=grid_size)

    dla.dla_cluster(
        initial_position=initial_walker_position,
        show_cluster_every_n_iterations=SHOW_CLUSTER_EVERY_N_ITERATIONS,
        show_every_random_walk=False
    )
