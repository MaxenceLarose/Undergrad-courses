# Stickiness factor
import logging
from typing import Tuple, List

from walkers_grid import WalkersGrid
from src.tools import logs_file_setup, set_seed
import numpy as np
from random import random
import matplotlib.pyplot as plt

from animation import Animation
from theoretical_tools import get_fractal_dimension


class DLAOriginal(WalkersGrid):
    def __init__(self, **kwargs):
        """
        Constructor of the class DLAOriginal.

        Parameters
        ----------
        kwargs: {
            grid_size (int): Square grid size. Default = 101.
        }
        """
        super().__init__(kwargs.get("grid_size", 101))

    def dlaoriginal_cluster(
            self,
            initial_position: Tuple[int, int],
            log_cluster_every_n_iterations: int,
            log_every_random_walk: bool = False,
            show_animation: bool = False,
            show_last_frame: bool = False,
    ):
        """
        This function uses the DLA original process to create fractal structures called Brownian trees as walkers
        aggregate into a central cluster during the diffusion process.

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

        # set initial spawning radius r to 0.
        r = 0

        state_frame = []
        complete_cluster = False

        # Spawning initial central walker.
        spawn_position = initial_position
        self.set_state(
            position=initial_position,
            state=1,
            add_new_walker=True)

        # create variable to save latest frame in.
        frame_sum  = self.state.copy()

        added_walker = True
        radius_bounds = False

        # DLA original loop.
        while not complete_cluster:

            #   Check if walker added to save grid state.
            frame = self.state.copy()
            if added_walker:
                if show_animation:
                    state_frame.append(frame)
                if show_last_frame:
                    frame_sum += frame

            #   Check if walker added to cluster or if walker broke radius boundaries to spawn walker on circle.
            if added_walker or radius_bounds:
                spawn_position, r = self.walker_spawn_coordinates(initial_position, frame)


            # reinstate loop criteria.
            current_position = spawn_position
            complete_random_walk = False
            radius_bounds = False


            if log_every_random_walk:
                walker_grid = WalkersGrid(grid_size=self.grid_size)
                walker_grid.set_state(position=current_position, state=1, add_new_walker=True)

            # random walk loop the latest added walker.
            while not complete_random_walk and not radius_bounds:

                # Get adjacent position of the walker.
                adjacent_positions = self.get_adjacent_positions(position=current_position,
                                                                 filter_positions_outside_bounds=False
                                                                 )
                # Check if random walk is completed.
                complete_random_walk, radius_bounds = self.check_walk_terminate_conditions(adjacent_positions, initial_position, r)

                # Decide where the walker will go next in it's adjacent positions.
                next_position = self.get_random_adjacent_position(
                    adjacent_positions=adjacent_positions,
                    avoid_other_walkers=False,
                )

                # Decide walker's current position according to criterion and add position to calculate radius.
                if complete_random_walk:
                    self.set_state(
                        position=current_position,
                        state=1,
                        add_new_walker=True)
                    added_walker = True
                else:
                    current_position = next_position
                    added_walker = False

                #
                if log_every_random_walk:
                    walker_grid.set_state(position=current_position, state=1, add_new_walker=False)

            #
            if log_every_random_walk:
                logging.info(f"Current number of walkers: {self.walkers_count}")


            # Check if the cluster is completed according to criterion.
            complete_cluster = self.check_dla_terminate_condition(
                r = r
            )

            # Log the number of added walkers at each chosen number of walkers added.
            if (self.walkers_count % log_cluster_every_n_iterations) == 0:
                logging.info(f"Current number of walkers: {self.walkers_count}")

        # Log total walkers added to complete cluster.
        logging.info(f"Total number of walkers: {self.walkers_count}")
        print(f"Spawning circle final radius = {r}")

        # Add current position and grid state for figure purposes and animate.
        frame = self.state.copy()
        animate = Animation()
        if show_animation:
            state_frame.append(frame)

            # Animation function.
            animate.DLA_animation(state_frame, 30, 'original')

        if show_last_frame:
            frame_sum += frame
            maximum = np.amax(frame_sum)

            # Plot last frame.
            plt.imshow(frame_sum, cmap=animate.colormap(), vmin = 1, vmax = maximum)
            cbar = plt.colorbar()
            cbar.set_label('Age of the walker [frame]', rotation=270, labelpad = 15)

            plt.savefig(f'DLAoriginal_{self.walkers_count}walkers_{self.grid_size}.pdf', dpi = 300, bbox_inches = 'tight')


            plt.show()



    def check_walk_terminate_conditions(
            self,
            adjacent_positions: List[tuple],
            initial_position: Tuple[int,int],
            r : int
    ) -> Tuple[bool,bool]:
        """
        Check if the random walk must be terminated. The random walk must be terminated if an adjacent position is
        occupied by a walker (state = 1) or if an adjacent position is outside the grid (walker reaches one of the
        sides of the grid).

        Parameters
        ----------
        adjacent_positions (List[tuple, ..., tuple]): List of all the adjacent positions.
        initial position (Tuple[int,int]): initial position of the first spawned walker.
        r (int): radius from the initial position at which the walkers are spawned.


        Returns
        -------
        (terminate,terminate_circle) Tuple[bool,bool]: Terminate random walk.
        """

        # Check if the walker is in a valid position or next to another walker.
        terminate = False
        if not all(list(map(lambda location: self.validate_position(location), adjacent_positions))):
            terminate_radius = True
        elif any(list(map(lambda location: self.state[location] == 1, adjacent_positions))):
            terminate = True

        # Check if the position of the walker is within a radius of approximately 2r of the center.
        for position in adjacent_positions:
            distance = np.linalg.norm([position[0]-initial_position[0],position[1]-initial_position[1]])
            if 2*r < round(distance):
                terminate_radius = True
            else:
                terminate_radius = False

        return (terminate, terminate_radius)

    def check_dla_terminate_condition(self,
            r: int
    ) -> bool:
        """
        Check if the DLA process must be terminated. The DLA process must be terminated if the radius of the circle
        spawning walkers is half the distance between the center of the grid to the side of the grid.

        Parameters
        ----------
        r (int): radius of the walker spawning circle.

        Returns
        -------
        terminate (bool): Terminate DLA process.
        """

        # Check if the walker spawning circle has a radius larger than a quarter of the grid's size.
        if np.floor(self.grid_size/4) <= r:
            terminate = True
        else:
            terminate = False

        return terminate

    def walker_spawn_coordinates(self,
                                 initial_position : Tuple[int,int],
                                 frame : np.ndarray
                                 ):
        """
        Calculates the valid coordinates at which the walkers can be spawned.

        Parameters
        ----------
        initial_position (Tuple[int, int]): The initial position of the first spawned walker(x, y).
        frame (np.ndarray): current state of the grid.

        Returns
        -------
        (x,y) (Tuple): Coordinates of the to be spawned walker
        next_max_dist: Approximate distance from the center at which the walker is spawned.
        """

        # Get the indices for which the current grid_state is not zero (occupied by walker).
        x,y = np.nonzero(np.asarray(frame))

        # Get distance to the initial position of the walkers.
        dist = ((x-initial_position[0])**2+(y-initial_position[1])**2)**(1/2)

        # Get maximal distance.
        max_dist = np.floor(np.amax(dist))

        # Decide next_maximal distance allowed (r).
        next_max_dist = max_dist + 1

        # Generate random angle at which to spawn walker.
        theta = random()*2*np.pi

        # Generate spawn coordinates for next walker.
        x = round(next_max_dist*np.cos(theta)) + initial_position[0]
        y = round(next_max_dist*np.sin(theta)) + initial_position[1]

        return (x,y), next_max_dist


def show_fractal_dimension(
        grid_size_list: list,
        log_cluster_every_n_iterations: int,
):
    """
    This function displays the figure of the mass of the cluster as a function of its radius. The curve fit on the data
    of this figure provides the average fractal dimension of the DLA original cluster.

    Parameters
    ----------
    grid_size_list (list): List of the grid sizes to use. The size of the grid determines the maximum radius of the
                           cluster.
    log_cluster_every_n_iterations (int): Display cluster formed by the walkers every n iterations.

    Returns
    -------
    Fig and axes.
    """
    radius: list = []
    walkers_count: list = []
    for size in grid_size_list:
        dla_cluster = DLAOriginal(grid_size=size)

        center_position = int((size - 1) / 2)
        initial_position = (center_position, center_position)

        dla_cluster.dlaoriginal_cluster(
            initial_position=initial_position,
            log_cluster_every_n_iterations=log_cluster_every_n_iterations
        )
        radius.append(size / 4)
        walkers_count.append(dla_cluster.walkers_count)

    get_fractal_dimension(radius=radius, mass=walkers_count)


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
    show_fractal_dimensionality = True
    LOG_CLUSTER_EVERY_N_ITERATIONS = 100

    logging.info(f"Initial position is {initial_walker_position}.")
    # ----------------------------------------------------------------------------------------------------------- #
    #                                            DLA                                                              #
    # ----------------------------------------------------------------------------------------------------------- #
    dla = DLAOriginal(grid_size=grid_size)
    dla.dlaoriginal_cluster(
        initial_position=initial_walker_position,
        log_cluster_every_n_iterations=LOG_CLUSTER_EVERY_N_ITERATIONS,
        log_every_random_walk=False,
        show_animation=True,
        show_last_frame=True
    )
    # ----------------------------------------------------------------------------------------------------------- #
    #                                  Fractal Dimensionality analysis                                            #
    # ----------------------------------------------------------------------------------------------------------- #
    if show_fractal_dimensionality:
        GRID_SIZE_LIST = np.arange(50, 300, 10)
        LOG_CLUSTER_EVERY_N_ITERATIONS = 1000

        show_fractal_dimension(
            grid_size_list=GRID_SIZE_LIST,
            log_cluster_every_n_iterations=LOG_CLUSTER_EVERY_N_ITERATIONS
        )
