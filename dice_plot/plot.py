from dice_tools import DICEObject
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import lz4
from tempfile import NamedTemporaryFile
import mmap
from dice_tools.helpers.xview import View
from dice_tools import *


class Plot(View):

    def __init__(self, size_x=1, size_y=1, figure=None, **kwargs):
        super().__init__(**kwargs)
        if figure is None:
            self.__figure = plt.figure()
        else:
            self.__figure = figure
        self.__figure.set_dpi(100)
        self.__size_x = size_x
        self.__size_y = size_y

    @property
    def figure(self):
        return self.__figure

    @figure.setter
    def figure(self, value):
        self.__figure = value
        self.draw()

    def draw(self):
        if self.__figure is None or \
                self.__size_x == 0 or self.__size_y == 0:
            return
        dpi = float(self.__figure.get_dpi())
        width = self.__size_x/dpi
        height = self.__size_y/dpi
        self.__figure.set_size_inches((width, height))
        self.__figure.canvas.draw()
        data, size = self.__figure.canvas.print_to_buffer()

        # assert size == (int(self.__size_x), int(self.__size_y)), '{} {} {}'.format(size, self.__size_x, self.__size_y)
        # assert len(data) == self.__size_x*self.__size_y*4

        self.update(size[0], size[1], False, data)

    def size_changed(self, size_x, size_y):
        """
        Size changed event handler.

        :param size_x: New size x dimension.
        :param size_y: New size y dimension.
        """
        self.__size_x = size_x
        self.__size_y = size_y
        self.draw()

    '''
    Mouse Events
    ============
    '''
    def mouse_press(self, btn, x, y, modifiers):
        """
        Mouse button press event handler.

        :param btn: Mouse button code.
        :param x: X coordinate of position where mouse pressed.
        :param y: Y coordinate of position where mouse pressed.
        :param modifiers: Keyboard modifiers, i.e. 'Alt', 'Control', 'Shift'.
        """

    def mouse_release(self, btn, x, y, modifiers):
        """
        Mouse button release event handler.

        :param btn: Mouse button code.
        :param x: X coordinate of position where mouse pressed.
        :param y: Y coordinate of position where mouse pressed.
        :param modifiers: Keyboard modifiers, i.e. 'Alt', 'Control', 'Shift'.
        """

    def mouse_move(self, x, y, modifiers):
        """
        Mouse move event handler.

        :param x: X coordinate of position mouse moved to.
        :param y: Y coordinate of position mouse moved to.
        :param modifiers: Keyboard modifiers, i.e. 'Alt', 'Control', 'Shift'.
        """

    def mouse_wheel(self, delta_x, delta_y, x, y, modifiers):
        """
        Mouse wheel event handler.

        :param delta_x: Unused.
        :param delta_y: Mouse wheel turn offset.
        :param x: X coordinate of position where mouse wheel was turned.
        :param y: Y coordinate of position where mouse wheel was turned.
        :param modifiers: Keyboard modifiers, i.e. 'Alt', 'Control', 'Shift'.
        """
