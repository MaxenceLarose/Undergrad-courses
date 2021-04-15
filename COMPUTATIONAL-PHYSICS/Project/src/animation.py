import matplotlib.pyplot as plt
import matplotlib.animation as anim
from matplotlib.animation import PillowWriter
import numpy as np
from typing import List
from walkers_grid import WalkersGrid

class Animation():
    def __init__(self, **kwargs):
        """
        Constructor of the class BrownianMotion.

        Parameters
        ----------
        kwargs: {
            grid_size (int): Square grid size. Default = 101.
        }
        """

    def brownian_motion_animation(
            self,
            state_frames : List[np.ndarray],
            position_frames : List[np.ndarray],
            fps : int
    ):
        """
        This function animates the state_frames from the brownian_motion.

        Parameters
        ----------
        state_frames (list[np.ndarray]): List of the saved state_frames from the brownian_motion.
        position_frames_frames (list[np.ndarray]): List of the saved position_frames from the brownian_motion.
        fps (int): frames per second for rendering the animation.

        Returns
        -------
        None
        """

        # Number of frames to animate
        nframes = len(state_frames)

        # Sum frames for heat map of the walker's positions
        frame = []
        position_prec = 0

        for i in range(len(state_frames)):
            position_sum = position_frames[i] + position_prec
            frame.append(state_frames[i] + position_sum)
            position_prec = position_sum

        # Take maximum pixel magnitude to set cmap in order for the last walker's position to be highlighted.
        maximum = np.amax(frame[-1])

        frame = np.asarray(frame)

        # Create figure and animation
        fig = plt.figure()
        im_state = plt.imshow(frame[0] + (maximum+1)*position_frames[0], cmap='winter', vmin = 1, vmax = maximum+1)

        def init():
            im_state.set_data(frame[0]+(maximum+1)*position_frames[0])
            return [im_state]

        def animate_func(i):
            im_state.set_data(frame[i]+(maximum+1)*position_frames[i])
            return [im_state]

        animated = anim.FuncAnimation(fig,animate_func, init_func = init, frames = nframes, interval = 1000/fps)

        animated.save(f'BM_{np.shape(frame[-1])[0]}grid_{nframes}steps.gif', writer=PillowWriter(fps=30))

        plt.show()


    def DLA_animation(
            self,
            state_frames : List[np.ndarray],
            fps : int,
            DLA_type : str = ''
    ):
        """
        This function animates the state_frames from the DLA and the DLA original.

        Parameters
        ----------
        state_frames (list[np.ndarray]): List of the saved state_frames from the DLA.
        fps (int): frames per second for rendering the animation.

        Returns
        -------
        None
        """

        # Number of frames to animate
        nframes = len(state_frames)

        # Sum frames for heat map of the walker's positions
        frame = []
        frame_prec = 0
        for i in range(len(state_frames)):
            frame_sum = state_frames[i] + frame_prec
            frame.append(frame_sum)
            frame_prec = frame_sum

        # Take maximum pixel magnitude to set cmap.
        maximum = np.amax(frame[-1])

        frame = np.asarray(frame)

        # Reverse pixel magnitudes to have younger additions to the cluster be lighter for visibility and for the
        # background to remain a dark color.
        nonzero = np.nonzero(frame)
        for (x,y,z) in zip(*nonzero):
            frame[x,y,z] = -1*(frame[x,y,z] - (maximum+1))

        # Create figure and animation
        fig = plt.figure()
        im_state = plt.imshow(frame[0], cmap='winter', vmin = 1, vmax = maximum+1)

        def init():
            im_state.set_data(frame[0])
            return [im_state]

        def animate_func(i):
            im_state.set_data(frame[i])
            return [im_state]

        animated = anim.FuncAnimation(fig,animate_func, init_func = init, frames = nframes, interval = 1000/fps)
        animated.save(f'DLA{DLA_type}_{nframes}walkers_{np.shape(frame[-1])[0]}.gif', writer=PillowWriter(fps=30))
        plt.show()




