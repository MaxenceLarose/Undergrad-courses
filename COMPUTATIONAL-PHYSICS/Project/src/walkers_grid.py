import logging
from typing import Tuple, List
import numpy as np
from itertools import starmap, product

from src.tools import logs_file_setup


class WalkersGrid(object):
    def __init__(
            self,
            grid_size: int = 101
    ):
        """
        Constructor of the class WalkersGrid.

        Parameters
        ----------
        grid_size (int): Square grid size. Default = 101.
        """
        self.grid_size = grid_size
        self._state: np.ndarray = np.zeros((self.grid_size, self.grid_size), dtype=int)
        self._walkers_count: int = 0

    @property
    def walkers_count(self):
        """
        Walkers count property.

        Returns
        -------
        self._walkers_count (int): Number of walkers added to the matrix.
        """
        return self._walkers_count

    @property
    def state(self):
        """
        State property.

        Returns
        -------
        self._state (np.ndarray): Current state of the grid matrix. The state of a specific position is generally 1 if a
                                  walker is currently at this position and 0 if there is not any walker at this
                                  position. However, the user can set the state of a specific position to a value of 0
                                  or 1 without adding a new walker to the grid, so this interpretation may differ
                                  depending on how it is used. For example, this can be used to follow the path of a
                                  single walker, note the final position of several walkers after their random walks,
                                  etc...
        """
        return self._state

    def validate_position(
            self,
            position: Tuple[int, int]
            ) -> bool:
        """
        This function allows you to check whether the position of a walker is valid or not. It is valid if the position
        is in the grid.

        Parameters
        ----------
        position (Tuple[int, int]): The position (x, y) to validate.

        Returns
        -------
        valid (bool): Validity of the position.
        """
        x, y = position

        valid = -1 < x < self.grid_size and -1 < y < self.grid_size

        return valid

    def set_state(
            self,
            position: Tuple[int, int],
            state: int,
            add_new_walker: bool
    ):
        """
        This function updates the state matrix at the given position with the given state.

        Parameters
        ----------
        position (Tuple[int, int]): The position (x, y) to update.
        state (int): State to use for the update. The allowed values are 0 or 1.
        add_as_new_walker (bool): Whether or not the update involves adding a new walker to the grid environment.

        Returns
        -------
        None
        """
        if not self.validate_position(position=position):
            raise ValueError("The position chosen for this walker is outside the grid bounds. Please select a position "
                             f"between (0, 0) and ({self.grid_size - 1}, {self.grid_size - 1}) inclusive.")

        if state == 0 or state == 1:
            pass
        else:
            raise ValueError("The state value you entered is not allowed. The allowed state values are 0 and 1.")

        if state == 0 and add_new_walker:
            raise PermissionError("A new walker must be paired with a state value of 1.")

        self._state[position] = state

        if add_new_walker:
            self._walkers_count += 1

    def get_adjacent_positions(
            self,
            position: Tuple[int, int],
            filter_positions_outside_bounds: bool = True,
            filter_diagonal: bool = True
    ) -> List[tuple]:
        """
        This function returns the adjacent positions given a specific position in the grid.

        Parameters
        ----------
        position (Tuple[int, int]): The position (x, y) to get the adjacent positions from.
        filter_positions_outside_bounds (bool): Whether or not to remove adjacent positions that are outside the grid
                                                bounds from the list of adjacent positions. Default = True.
        filter_diagonal (bool): Whether or not to remove diagonal adjacent positions from the list of adjacent
                                positions.
                                If True:
                                         |A|
                                        A|X|A
                                         |A|
                                If False:
                                        A|A|A
                                        A|X|A
                                        A|A|A

                                Default = True.

        Returns
        -------
        adjacent_positions (List[tuple, ..., tuple]): List of all the adjacent positions.
        """
        x, y = position

        if filter_diagonal:
            _displacements = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]
        else:
            _displacements = product((0, -1, +1), (0, -1, +1))

        adjacent_positions = starmap(lambda a, b: (x + a, y + b), _displacements)

        if filter_positions_outside_bounds:
            adjacent_positions = filter(
                lambda location: self.validate_position(location),
                adjacent_positions
            )

        return list(adjacent_positions)[1:]

    def get_random_adjacent_position(
            self,
            position: Tuple[int, int],
            avoid_other_walkers: bool = True,
            **kwargs
    ) -> Tuple[int, int]:
        """
        This function returns a random position adjacent to the given position.

        Parameters
        __________
        position (Tuple[int, int]): The position (x, y) to get the adjacent positions from.
        avoid_other_walkers (bool): Whether or not to avoid other walkers. If this is true, the walker's next position
                                    cannot be a position where a walker is already present. Default = True.
        kwargs: {
            filter_positions_outside_bounds (bool): Whether or not to remove adjacent positions that are outside the
                                                    grid bounds from the list of adjacent positions. Default = True.
            filter_diagonal (bool): Whether or not to remove diagonal adjacent positions from the list of adjacent
                                    positions. Default = True.
        }

        Returns
        _______
        random_adjacent_position (Tuple[int, int]): Random adjacent position (x, y).
        """
        adjacent_positions = self.get_adjacent_positions(
            position=position,
            filter_positions_outside_bounds=kwargs.get("filter_positions_outside_bounds", True),
            filter_diagonal=kwargs.get("filter_diagonal", True)
        )

        if avoid_other_walkers:
            adjacent_positions = list(
                filter(
                    lambda location: self._state[location] == 0,
                    adjacent_positions
                )
            )

        random_position_idx = np.random.randint(len(adjacent_positions))
        random_adjacent_position = adjacent_positions[random_position_idx]

        return random_adjacent_position

    def get_state_surface_area(self) -> int:
        """
        This function returns the surface area of the current state matrix.

        Returns
        -------
        area (int): Surface area of the current state matrix.
        """
        area = np.count_nonzero(self._state)

        return area

    def get_ratio_of_occupied_area(self) -> float:
        """
        This function returns the ratio between the surface area of the current state matrix and the total surface area
        of the grid.

        Returns
        -------
        ratio (float): Ratio between the surface area of the current state matrix and the total surface area of the
                       grid.
        """
        state_area = self.get_state_surface_area()
        grid_area = self._state.size

        ratio = state_area/grid_area

        return ratio

    def get_neighbors_count(self) -> float:
        """
        This function returns the total number of neighbors. For each position with state 1, it counts the number of
        adjacent positions with state 1 and returns the sum of all these numbers.

        Returns
        -------
        neighbors_count (float): Total number of neighbors.
        """
        neighbors_count: int = 0

        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if self.state[i, j] == 1:
                    neighbors = self.get_adjacent_positions(position=(i, j))
                    neighbors = list(
                        filter(
                            lambda position: self.state[position] == 1,
                            neighbors
                        )
                    )

                    neighbors_count += len(neighbors)

        return neighbors_count

    def get_average_neighbors_count(self) -> float:
        """
        This function returns the average number of neighbors.

        Returns
        -------
        average_neighbors_count (float): Average number of neighbors.
        """
        neighbors_count = self.get_neighbors_count()
        average_neighbors_count = neighbors_count/self._walkers_count

        return average_neighbors_count


if __name__ == "__main__":
    # ----------------------------------------------------------------------------------------------------------- #
    #                                      Logs Setup                                                             #
    # ----------------------------------------------------------------------------------------------------------- #
    logs_file_setup(__file__, logging.INFO)

    # ----------------------------------------------------------------------------------------------------------- #
    #                                       Constants                                                             #
    # ----------------------------------------------------------------------------------------------------------- #
    initial_walker_position = (100, 100)

    # ----------------------------------------------------------------------------------------------------------- #
    #                                  Grid Environment Setup                                                     #
    # ----------------------------------------------------------------------------------------------------------- #
    grid = WalkersGrid()
    grid_state = grid.state
    grid.set_state(position=initial_walker_position, state=1, add_new_walker=True)
    print(grid.walkers_count)
    print(grid.get_adjacent_positions((0, 0)))
    grid.set_state(position=(99, 99), state=1, add_new_walker=False)
    print(grid.get_random_adjacent_position((100, 100), avoid_other_walkers=True))
    print(grid.get_state_surface_area())
    print(grid.get_ratio_of_occupied_area())
    grid.set_state(position=(99, 98), state=1, add_new_walker=True)
    print(grid.get_neighbors_count())
    print(grid.get_average_neighbors_count())
