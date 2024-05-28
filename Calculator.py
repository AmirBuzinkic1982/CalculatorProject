class Calculator:
    final_result = 0.0

    class Operations:
        ADDITION_SYMBOL = '+'
        SUBTRACTION_SYMBOL = '-'
        MULTIPLICATION_SYMBOL = '*'
        DIVISION_SYMBOL = '/'

        @staticmethod
        def to_string():
            return "{}{}{}{}".format(Calculator.Operations.ADDITION_SYMBOL, 
                                     Calculator.Operations.MULTIPLICATION_SYMBOL, 
                                     Calculator.Operations.DIVISION_SYMBOL, 
                                     Calculator.Operations.SUBTRACTION_SYMBOL)

    @staticmethod
    def run(expression):
        return Calculator.evaluate_expression(expression)

    @staticmethod
    def evaluate_expression(expression):
        if expression[0] == Calculator.Operations.ADDITION_SYMBOL or expression[0] == Calculator.Operations.SUBTRACTION_SYMBOL:
            expression = '0' + expression

        numbers = expression.split("[" + Calculator.Operations.to_string() + "]")
        operations = [char for char in expression if char in Calculator.Operations.to_string()]

        number_list = []
        for number in numbers:
            if number == "-Infinity":
                number_list.append(float('-inf'))
            elif number == "Infinity":
                number_list.append(float('inf'))
            else:
                try:
                    number_list.append(float(number))
                except ValueError:
                    return "ERROR"

        Calculator.calculate(number_list, operations)
        return str(Calculator.final_result)

    @staticmethod
    def calculate(numbers, operations):
        if len(numbers) == 1:
            Calculator.final_result = numbers[0]
            return

        result = 0.0

        if Calculator.Operations.MULTIPLICATION_SYMBOL in operations and Calculator.Operations.DIVISION_SYMBOL in operations:
            index_multiply = operations.index(Calculator.Operations.MULTIPLICATION_SYMBOL)
            index_divide = operations.index(Calculator.Operations.DIVISION_SYMBOL)

            if index_multiply < index_divide:
                result = numbers[index_multiply] * numbers[index_multiply + 1]
                numbers[index_multiply] = result
                del numbers[index_multiply + 1]
                del operations[index_multiply]
            else:
                result = numbers[index_divide] / numbers[index_divide + 1]
                numbers[index_divide] = result
                del numbers[index_divide + 1]
                del operations[index_divide]
        elif Calculator.Operations.MULTIPLICATION_SYMBOL in operations:
            index_multiply = operations.index(Calculator.Operations.MULTIPLICATION_SYMBOL)
            result = numbers[index_multiply] * numbers[index_multiply + 1]
            numbers[index_multiply] = result
            del numbers[index_multiply + 1]
            del operations[index_multiply]
        elif Calculator.Operations.DIVISION_SYMBOL in operations:
            index_divide = operations.index(Calculator.Operations.DIVISION_SYMBOL)
            result = numbers[index_divide] / numbers[index_divide + 1]
            numbers[index_divide] = result
            del numbers[index_divide + 1]
            del operations[index_divide]

        if Calculator.Operations.ADDITION_SYMBOL in operations and Calculator.Operations.SUBTRACTION_SYMBOL in operations:
            index_plus = operations.index(Calculator.Operations.ADDITION_SYMBOL)
            index_minus = operations.index(Calculator.Operations.SUBTRACTION_SYMBOL)

            if index_plus < index_minus:
                result = numbers[index_plus] + numbers[index_plus + 1]
                numbers[index_plus] = result
                del numbers[index_plus + 1]
                del operations[index_plus]
            else:
                result = numbers[index_minus] - numbers[index_minus + 1]
                numbers[index_minus] = result
                del numbers[index_minus + 1]
                del operations[index_minus]
        elif Calculator.Operations.ADDITION_SYMBOL in operations:
            index_plus = operations.index(Calculator.Operations.ADDITION_SYMBOL)
            result = numbers[index_plus] + numbers[index_plus + 1]
            numbers[index_plus] = result
            del numbers[index_plus + 1]
            del operations[index_plus]
        elif Calculator.Operations.SUBTRACTION_SYMBOL in operations:
            index_minus = operations.index(Calculator.Operations.SUBTRACTION_SYMBOL)
            result = numbers[index_minus] - numbers[index_minus + 1]
            numbers[index_minus] = result
            del numbers[index_minus + 1]
            del operations[index_minus]

        Calculator.calculate(numbers, operations)

