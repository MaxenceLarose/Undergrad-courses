# Stickiness factor
import logging
from typing import Tuple, List

from walkers_grid import WalkersGrid
from src.tools import logs_file_setup, set_seed
import numpy as np
from random import random

from animation import Animation


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
            log_every_random_walk: bool = False
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

        r = 0
        state_frame = []
        complete_cluster = False
        spawn_position = initial_position
        self.set_state(
            position=initial_position,
            state=1,
            add_new_walker=True)
        position_list = []
        added_walker = True
        radius_bounds = False
        while not complete_cluster:

            if added_walker or radius_bounds:
                frame = self.state.copy()
                state_frame.append(frame)
                spawn_position, r = self.walker_spawn_coordinates(initial_position, frame)
            else:
                pass


            current_position = spawn_position
            complete_random_walk = False
            radius_bounds = False


            if log_every_random_walk:
                walker_grid = WalkersGrid(grid_size=self.grid_size)
                walker_grid.set_state(position=current_position, state=1, add_new_walker=True)

            while not complete_random_walk and not radius_bounds:
                adjacent_positions = self.get_adjacent_positions(position=current_position,
                                                                 filter_positions_outside_bounds=False
                                                                 )
                complete_random_walk, radius_bounds = self.check_walk_terminate_conditions(adjacent_positions, initial_position, r)


                next_position = self.get_random_adjacent_position(
                    adjacent_positions=adjacent_positions,
                    avoid_other_walkers=False,
                )

                if complete_random_walk:
                    self.set_state(
                        position=current_position,
                        state=1,
                        add_new_walker=True)
                    position_list.append(current_position)
                    added_walker = True
                else:
                    current_position = next_position
                    added_walker = False

                if log_every_random_walk:
                    walker_grid.set_state(position=current_position, state=1, add_new_walker=False)

            if log_every_random_walk:
                logging.info(f"Current number of walkers: {self.walkers_count}")



            complete_cluster = self.check_dla_terminate_condition(
                r = r
            )


            if (self.walkers_count % log_cluster_every_n_iterations) == 0:
                logging.info(f"Current number of walkers: {self.walkers_count}")
                print(f"Spawning circle radius = {r}")

        logging.info(f"Total number of walkers: {self.walkers_count}")
        print(f"Spawning circle radius = {r}")

        frame = self.state.copy()
        state_frame.append(frame)

        animate = Animation()
        animate.DLA_animation(state_frame, 30)


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
        if not all(list(map(lambda location: self.validate_position(location), adjacent_positions))):
            terminate = True
        elif any(list(map(lambda location: self.state[location] == 1, adjacent_positions))):
            terminate = True
        else:
            terminate = False

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
        if r == np.floor(self.grid_size/4):
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


        x,y = np.nonzero(np.asarray(frame))
        dist = ((x-initial_position[0])**2+(y-initial_position[1])**2)**(1/2)
        max_dist = np.floor(np.amax(dist))
        next_max_dist = max_dist + 1


        theta = random()*2*np.pi

        x = round(next_max_dist*np.cos(theta)) + initial_position[0]
        y = round(next_max_dist*np.sin(theta)) + initial_position[1]

        return (x,y), next_max_dist






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

    LOG_CLUSTER_EVERY_N_ITERATIONS = 100

    logging.info(f"Initial position is {initial_walker_position}.")
    # ----------------------------------------------------------------------------------------------------------- #
    #                                            DLA                                                              #
    # ----------------------------------------------------------------------------------------------------------- #
    dla = DLAOriginal(grid_size=grid_size)

    dla.dlaoriginal_cluster(
        initial_position=initial_walker_position,
        log_cluster_every_n_iterations=LOG_CLUSTER_EVERY_N_ITERATIONS,
        log_every_random_walk=False
    )
