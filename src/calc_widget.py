
import os
from PySide6.QtCore import Slot, Qt
from PySide6.QtGui import QIcon, QColor
from PySide6.QtWidgets import QWidget, QPushButton, QButtonGroup, QGridLayout, QLineEdit, QVBoxLayout, QHBoxLayout
from calc_logic import CalcLogic


class NumPad(QWidget):
    """
    A QWidget that represents the numeric keypad 
    and basic functions of the calculator.
    """
    def __init__(self):
        super().__init__()

        # Defines non-numeric buttons
        self.clear_button = QPushButton('AC')
        self.negative_button = QPushButton('-/+')
        self.percent_button = QPushButton('%')
        # Asign each a name to adjust style
        self.clear_button.setObjectName('top')
        self.negative_button.setObjectName('top')
        self.percent_button.setObjectName('top')

        # Define button group to manage signals for non-numeric buttons
        self.function_group = QButtonGroup()
        # Define button group to manage signals for numeric buttons
        self.nums_group = QButtonGroup()
        # Define array for numeric buttons 1-9
        self.num_buttons = []

        self.decimal_button = QPushButton('.')
        self.zero_button = QPushButton('0')
        # Asign name to adjust style 
        self.zero_button.setObjectName('zero')

        # Define buttons 1-9
        for i in range(1, 10):
            button = QPushButton(str(i), self)
            self.num_buttons.append(button)

        # Add buttons 1-9 to nums group
        for button in self.num_buttons:
            self.nums_group.addButton(button)
        # Add zero & decimal buttons to nums group
        self.nums_group.addButton(self.zero_button)
        self.nums_group.addButton(self.decimal_button)

        # Add non numeric buttons to  fuction group
        self.function_group.addButton(self.clear_button)
        self.function_group.addButton(self.negative_button)
        self.function_group.addButton(self.percent_button)

        # Define grid layout
        layout = QGridLayout(self)
        # Add non numeric buttons to first row in grid
        layout.addWidget(self.clear_button, 0, 0)
        layout.addWidget(self.negative_button, 0, 1)
        layout.addWidget(self.percent_button, 0, 2)

        # Add buttons 1-9 starting at 9
        n = 8
        # loops through each row
        for i in range(1, 4):
            # Loops through each column in reverse
            for j in range(2, -1, -1):
                layout.addWidget(self.num_buttons[n], i, j)
                n -= 1
        # Add 0 and decimal buttons to last row
        layout.addWidget(self.zero_button, 4, 0, 1, 2)
        layout.addWidget(self.decimal_button, 4, 2)

        self.setLayout(layout)


class OperationButtons(QWidget):
    """ A QWidget that represents the operation buttons of the calculator."""
    def __init__(self):
        super().__init__()
        # Define button group to manage signals for operation buttons
        self.operation_group = QButtonGroup()
        # Define array to store operation buttons
        self.math_buttons = []
        symbols = ['/', '*', '-', '+']
        # define and name equal buttons to style easily
        self.equal_button = QPushButton('=')
        self.equal_button.setObjectName('equal')

        # define each operator button and set name for styling
        for symbol in symbols:
            button = QPushButton(symbol, self)
            button.setObjectName('op')
            self.math_buttons.append(button)

        # Add each button to button group
        for button in self.math_buttons:
            self.operation_group.addButton(button)
        self.operation_group.addButton(self.equal_button)

        # Define vertical box layout
        layout = QVBoxLayout()
        # Add each button to layout
        for i in range(4):
            layout.addWidget(self.math_buttons[i])
        layout.addWidget(self.equal_button)
        
        self.setLayout(layout)


class DisplayOutput(QWidget):
    """A QWidget that represents the display output of the calculator."""
    def __init__(self):
        super().__init__()
        # Define a text box to display values
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        # Remove text box border to blend with background
        self.display.setFrame(False)
        # Display text from right to left
        self.display.setAlignment(Qt.AlignRight)

        # Define horizontal box layout and add display to it
        layout = QHBoxLayout()
        layout.addWidget(self.display)
        self.setLayout(layout)

# Define a parent widget to manage child widgets
class CalcUI(QWidget):
    """
    A QWidget that combines the display, numeric keypad, 
    and operation buttons to create the calculator's user interface.
    """
    def __init__(self):
        super().__init__()

        # Define icon for the window tilebar
        icon_path = os.path.join('src', 'static', 'icon.png')
        icon = QIcon(icon_path)

        # Define bool value to manage when to clear text from diplay
        self._operation_clicked = False

        # Call CalcLogic class from calc_logic.py
        self.calculate = CalcLogic()

        self.setWindowIcon(icon)

        # Call the child widgets
        self.display = DisplayOutput()
        self.operation_buttons = OperationButtons()
        self.num_pad = NumPad()

        # Define a grid layout then add the child widgets
        layout = QGridLayout()
        layout.addWidget(self.display, 0, 0, 1, -1)
        layout.addWidget(self.num_pad, 1, 0, 5, 3)
        layout.addWidget(self.operation_buttons, 1, 3, 5, 1)
        self.setLayout(layout)

        # Connect the button group signals to thier corresponding slots
        self.num_pad.nums_group.buttonClicked.connect(self.update_display)
        self.operation_buttons.operation_group.buttonClicked.connect(self.call_operation)
        self.num_pad.function_group.buttonClicked.connect(self.run_function)

    # Ensure values properly display as int or float
    def display_value(self, value: int | float):
        """
        Display the given value as an integer or float in the calculator's
        display output.

        :param value: The value to display, as an integer or float.
        """
        # Convert the value to float
        float_value = float(value)
        
        # ".is_integer()" will evaluate to true if all values after
        # decimal are 0
        if float_value.is_integer():
            self.display.display.setText(str(int(float_value)))
        else:
            self.display.display.setText(str(round(float_value, 8)))
    

    @Slot(QPushButton)
    def update_display(self, num):
        """
        Update the display output with the clicked number button's value.

        :param num: The clicked number button.
        """
        # If an oporator is selected clear the display before the 
        # value is inserted
        if self._operation_clicked:
            self.display.display.clear()
            self._operation_clicked = False

        # append the clicked value to the displayed text
        self.display.display.insert(str(num.text()))


    @Slot(QPushButton)
    def call_operation(self, operator):
        """
        Perform the selected operation on the current input values and update the display output.

        :param operator: The clicked operator button.
        """
        self._operation_clicked = True
        # Retrieve the currently displayed text
        text = self.display.display.text()

        # Send the value to calc logic
        self.calculate.set_value(text)

        # Send the clicked oportator to calc logic
        # returns none unless operator is '='
        result = self.calculate.get_operation(operator.text())
        # If result has value display result
        if result is not None:
            # if divide by zero display Error
            if hasattr(self.calculate, 'error_message'):
                self.display.display.setText(self.calculate.error_message)
                delattr(self.calculate, 'error_message')
            else:
                # Display the result and reset operation_clicked
                self.display_value(result)
                self._operation_clicked = False

    @Slot(QPushButton)
    def run_function(self, function):
        """
        Execute the selected function (AC, -/+, %) and update the display output.

        :param function: The clicked function button.
        """
        # Clear the display and update calc logic
        if function.text() == 'AC':
            self.calculate.reset_values()
            self.display.display.clear()
        # Make displayed value negative
        if function.text() == '-/+':
            value = self.display.display.text()
            if '-' not in value:
                value = '-' + value
            else:
                value = value.lstrip('-')
            self.display_value(value)
        # Convert value to a percentage
        if function.text() == '%':
            value = float(self.display.display.text())
            value = str(value / 100)
            self.display_value(value)
