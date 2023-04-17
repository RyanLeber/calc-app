
class CalcLogic:
    def __init__(self):

        self._stored_value = None
        self._current_value = 0
        self._operation = None

    # 
    def reset_values(self):
        self._stored_value = None
        self._current_value = 0
        self._operation = None

    # Stores the currently displayed value
    def set_value(self, value):
        self._current_value = value

    def get_operation(self, operation):
        if operation == '/':
            self.divide()
        if operation == '*':
            self.multiply()
        if operation == '-':
            self.subtract()
        if operation == '+':
            self.add()
        if operation == '=':
            self.equals()
            return self._current_value

    def add(self):
        self._execute_operation()
        self._operation = 'add'

    def subtract(self):
        self._execute_operation()
        self._operation = 'subtract'

    def multiply(self):
        self._execute_operation()
        self._operation = 'multiply'

    def divide(self):
        self._execute_operation()
        self._operation = 'divide'

    def equals(self):
        self._execute_operation()
        self._operation = None

    def _execute_operation(self):
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

