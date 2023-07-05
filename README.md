# TUI-Menu

This is a Python Module for Menu driven TUI scripts

It helps developers to write menu-driven scripts (or apps) in a simple way.

## Installation

You have two wayes to install and use this module:
* Use pip to install it

```bash
pip install tui-menu
```
* Copy the `tui-menu/Menu.py` to your project 

### Usage

An example of using this module.

```python
from tui_menu.Menu import Menu

# Create main menu
main_menu = Menu()

# Creating sub-menu
sub_menu = Menu()

# Setting up the title and menu level
main_manu.title("My Application main menu")
main_menu.level(0)

sub_menu.title("My Application sub menu")
sub_menu.level(1)

sub_menu.add_item(key="1", name="running option 2", data=op_func2)

main_menu.add_item(key="1", name="running option 1", data=op_func1)
main_menu.add_item(key="2", name="sub menu 1", data=sub_menu)

# Create functions for menu operations
def op_func1():
    # do something

def op_func2():
    # do something

# running the application
main_menu.run()
```
You can create as many as you want of sub-menus, each sub menu is a Menu object.

Every Menu item can be a Menu object (sub-menu) or a Function which can be call and 
execute some operation.

The menu key is **one letter** key, you cannot use **'x'** or **'r'** which use for
* 'x' - exit the script / app
* 'r' - use in sub menu to return one level up

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

This Module is distributing under the [GPLv3+](https://www.gnu.org/licenses/gpl-3.0.html)
 Licensing
