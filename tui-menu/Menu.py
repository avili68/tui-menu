#!/usr/bin/env python
"""
Created on 30, Jun 2023

@author: Avi Liani
"""

# Python modules
import os
import sys

# 3ed party modules
from console import fg, fx
from console.utils import cls, pause, wait_key
from console.screen import sc


# Getting the Terminal dimensions (rows x cols)
terminal_size = os.get_terminal_size()


def print_in_line(row, col, data):
    """
    Print string message in a specific location on the screen

    Args:
        row (int) : the row of the screen (staring with 1)
        col (int) : the column of the screen
        data (str) : the string to display

    Returns:
        int : the next row to for the cursor
    """
    with sc.location(row, col):
        print(data)
    return row + 1


def goto_row(row):
    """
    go down to a specific row, relative to current row, starting from row number 1

    Args:
        row (int) : how much row to go foreword

    """
    for _ in range(row):
        print()


def clear_screen():
    """
    Clear the screen and move the cursor to the last line of the screen
    """
    cls()
    goto_row(terminal_size.lines - 1)


class MenuItem:
    """
    This is a Menu item class.
    menu item can be a 'Menu' or a 'Function', Function represent as OP

    """

    def __init__(self, key, value, data):
        """
        Setting up the menu item object

        Args:
             key (char): the menu selection key
             value (str): the key description
             data (Menu / Func name) : the sub-menu object or function name
               to be executed.

        """
        if isinstance(data, Menu):
            menu = "Menu"
        else:
            menu = "OP"
        self._key = key
        self._value = value
        self._data = data
        self._menu = menu

    def key(self, name=""):
        """Set / Get the 'name' variable"""
        if name != "":
            self._key = name
        return self._key

    def value(self, name=""):
        """Set / Get the 'value' variable"""
        if name != "":
            self._value = name
        return self._value

    def menu(self, name=""):
        """Set / Get the 'menu' variable"""
        if name != "" and name in ["OP", "Menu"]:
            self._menu = name
        return self._menu

    def data(self, name=""):
        """Set / Get the 'data' variable"""
        if name != "":
            self._data = name
        return self._data


class Menu:
    """
    Menu class to build and run menu-driven application
    """

    def __init__(self):
        """Initialize a menu object"""
        self._title = None
        self._level = None
        self._items = {}
        return

    def title(self, header=None):
        """
        Setting / Getting the menu title
        """
        if header is not None:
            self._title = header
        return self._title

    def level(self, level=None):
        """
        Setting / Getting the menu level.

        Args:
            level (int) : the menu level, 0 - main menu / 1 - sub-menu

        """
        if level is not None:
            self._level = level
        return self._level

    def add_item(self, key, name, data):
        """
        Adding new item to the menu (Function or sub-menu)

        """
        self._items[key] = MenuItem(key, name, data)

    def item(self, key):
        """
        Return menu item by its key

        Args:
            key (char) : the menu key option

        Returns:
            MenuItem / Function  : the submenu object or the function name to execute
        """
        return self._items[key]

    def display(self):
        """
        Display the menu on the screen

        Returns:
            int : the line where the courser need to be
        """
        row = 1
        clear_screen()
        # display the menu title with underline of '='
        row = print_in_line(row, 6, fx.italic + self.title() + fx.end)
        row = print_in_line(row, 5, "=" * (len(self.title()) + 2))
        row += 1

        # generate sorted list of menu options
        keys_list = list(self._items)
        keys_list.sort()

        for key in keys_list:
            string_line = f"{key} ) {self._items[key].value()}"
            if self._items[key].menu() == "Menu":
                # if menu option is a sub-menu add '->' to indicate it
                string_line += " -->"
            row = print_in_line(row, 6, string_line)

        if self.level() != 0:
            # if sub-menu, add the 'return' option
            row = print_in_line(row + 1, 6, "r ) Return to previous menu") + 1
            # row += 2

        # add the 'exit' option
        row = print_in_line(row + 1, 6, "x ) Exit") + 1
        # row += 2

        return row

    def get_option(self):
        """
        get the menu selected option from the user.
        make sure only valid option  was pressed

        Returns:
            char : the menu option that was selected
        """
        # build list of valid options
        keys_list = list(self._items)
        keys_list.sort()
        # adding exit option to valid options
        keys_list.append("x")
        if self.level() != 0:
            # if sub-menu, adding the return option to valid options
            keys_list.append("r")

        row = self.display()

        results = None
        while not results:
            print_in_line(row + 1, 6, "Select an option : [_]")
            with sc.location(row + 1, 26):
                results = wait_key()
            if results in keys_list:
                return results
            else:
                print_in_line(
                    row + 3, 6, fg.red + f"Invalid option : {results}" + fg.default
                )
                print_in_line(
                    row + 5,
                    6,
                    fg.green + f"Valid options are : {keys_list}" + fg.default,
                )
                results = None

    def run(self):
        """
        Run the application via the Menu
        """
        results = None
        while results != "x":
            results = self.get_option()

            if results == "x":  # exit the application immediately
                sys.exit()
            if results == "r":  # return to the previous menu
                return
            if self.item(results).menu() == "Menu":
                # run the sub-menu
                self.item(results).data().run()
            else:
                # run the menu option (function)
                self.item(results).data()()
                print()
                pause()
        return


def main():
    # This is a testing function for this module

    def testing_op_1():
        _ = input("Enter value for option 1 : ")

    def testing_op_2():
        _ = input("Enter value for option 2 : ")

    main_menu = Menu()
    main_menu.title("Testing Main Menu")
    main_menu.level(level=0)
    main_menu.add_item(key="a", name="testing option 1", data=testing_op_1)

    sub_menu_1 = Menu()
    sub_menu_1.title("Sub-Menu 1")
    sub_menu_1.level(level=1)
    sub_menu_1.add_item(key="1", name="testing option 2", data=testing_op_2)

    main_menu.add_item(key="1", name="sub menu 1", data=sub_menu_1)

    main_menu.run()


if __name__ == "__main__":
    main()
