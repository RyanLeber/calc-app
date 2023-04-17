
class CalcLogic:
    def __init__(self):

        self.operator_dict = {
            '/': 'divide',
            '*': 'multiply',
            '-': 'subtract',
            '+': 'add'
        }

        self._stored_value = None
        self._current_value = 0
        self._operation = None

    # clear the calculator memory
    def reset_values(self):
        self._stored_value = None
        self._current_value = 0
        self._operation = None

    # Stores the currently displayed value
    def set_value(self, value):
        self._current_value = value

    # Execute the operation then store the selected operation
    def get_operation(self, operator):
        self._execute_operation()

        if operator in self.operator_dict:
            self._operation = self.operator_dict[operator]

        # if operation is '=', clear _operation and return answer
        if operator == '=':
            self._operation = None
            return self._current_value

    def _execute_operation(self):
        # If no operation selected or no value previously stored,
        # store the value
        if not self._operation or not self._stored_value:
            self._stored_value = self._current_value
        
        else:
            if self._operation == 'add':
                self._stored_value += self._current_value
            elif self._operation == 'subtract':
                self._stored_value -= self._current_value
            elif self._operation == 'multiply':
                self._stored_value *= self._current_value
            elif self._operation == 'divide':
                self._stored_value /= self._current_value
            self._current_value = self._stored_value

