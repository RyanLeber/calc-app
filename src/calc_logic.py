
class CalcLogic:
    """A class that represents a basic calculators logic"""
    def __init__(self):

        self.operator_dict = {
            '/': 'divide',
            '*': 'multiply',
            '-': 'subtract',
            '+': 'add'
        }

        self.reset_values()

    def reset_values(self):
        """Clear the calculator memory""" 
        self._stored_value = None
        self._current_value = 0
        self._operation = None

    def set_value(self, value: str):
        """Store the currently displayed value."""
        # Cast the value to float or int
        if '.' in value:
            cast_value = float(value)
        else:
            cast_value = int(value)

        self._current_value = cast_value

    def get_current_value(self) -> int | float:
        """Get the _current_value."""
        return self._current_value

    def get_operation(self, operator: str):
        """Execute the operation, then store the selected operation"""
        self._execute_operation()

        # set _operation to the selected operator
        if operator in self.operator_dict:
            self._operation = self.operator_dict[operator]

        # if operator is '=', clear _operation and return answer
        if operator == '=':
            self._operation = None
            return self.get_current_value()

    def _execute_operation(self):
        """Execute the currently selected operation."""
        # If no operation selected or no value previously stored,
        # store the value
        if not self._operation or self._stored_value == None:
            self._stored_value = self._current_value
        
        else:
            if self._operation == 'add':
                self._stored_value += self._current_value
            elif self._operation == 'subtract':
                self._stored_value -= self._current_value
            elif self._operation == 'multiply':
                self._stored_value *= self._current_value
            elif self._operation == 'divide':
                # Handle divide by zero error
                try:
                    self._stored_value /= self._current_value
                except ZeroDivisionError:
                    self.error_message = "Error"
                    self._current_value = 0
                    return

            self._current_value = self._stored_value
