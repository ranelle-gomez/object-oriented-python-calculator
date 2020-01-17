import time


class oopCalculator:
    """
    This class contains methods of different utilities used in everyday calculations, demonstrating different algorithms
    of designing a calculator using object-oriented programming and recursion. Built-in arithmetic (e.g., +, *)
    operators are implemented to combine arguments. However, the purpose of this class is not to supplant conventional
    python operators; rather, to demonstrate object-oriented programming and the positive effects of tail recursion on
    efficiency (or lack of in an interpreted language like python).
    """

    def add(self, numbers):
        """"Return the product of the number(s) in numbers.
        >>> add([6, 4])
        25
        >>> add([1, 0])
        1
        """ ""
        result = 0
        for number in numbers:
            result += number
        return result

    def subtract(self, numbers):
        """"Returns the difference between the first inputted number and the rest of the inputted numbers.
        >>> subtract([6, 4])
        2
        >>> subtract([10, 5, 5]) # 10 - 5 - 5
        0
        """ ""
        return numbers[0] - oopCalculator.add(numbers[1:])

    def multiply(self, numbers):
        """"Return the product of the number(s) in numbers.
        >>> multiply([6, 4])
        24
        >>> multiply([1, 0])
        0
        """
        init = 1
        final = numbers[0]
        rest = [elem for elem in numbers[1:]]
        if 0 in numbers:
            return 0
        for rest_elem in rest:
            init = init * rest_elem
        final = final * init
        return final

    def divide(self, numbers):
        """"A higher-order function that return the quotient of the number(s) in numbers.
        >>> divide([6, 4])
        24
        >>> divide([8, 4, 2]) # 8 * 1/4 * 1/2
        1
        >>> divide([1, 0])
       Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        ZeroDivisionError: division by zero
        """
        try:
            return numbers[0] * 1 / oopCalculator.multiply(self, numbers[1:])
        except ZeroDivisionError:
            return "Whoops. Can't divide by zero."

    def iterativeExponentiate(self, base, exponent):
        """"Returns the result of raising base to exponent, where base and exponent are integers.
        This method utilizes tail recursion, which closes the previous frame once the first recursive
        call is made.
        >>> iterativeExponentiate([3, 2])
        24
        >>> iterativeExponentiate([1, 0])
        1
        >>> iterativeExponentiate([3, 999999])
        5992367055585812793466172140059850585142228456957040238771...
        """
        result = 1
        i = 0
        if not isinstance(base, int) or not isinstance(exponent, int):
            return 'Base and exponent must both be integers.'
        elif exponent == 0:
            return 1
        while i < abs(
                exponent
        ):  # abs accounts for the case if the exponent is negative.
            if exponent < 0:
                result = oopCalculator.multiply(
                    self,
                    [result, oopCalculator.divide(self, [1, base])
                     ])  # no if i < 0 leads to 3 -1 -> 1
            elif i > 0:  # need this so its not ran after if statement.
                result = oopCalculator.multiply(self, [result, base])
            i = oopCalculator.add(self, [i, 1])
        return result


if __name__ == '__main__':

    test_calculator = oopCalculator()

    while True:
        choice = input(
            "1) Add 2) Multiply 3) Iteratively Exponentiate 4) Recursive Exponentiate "
            "5) Tail-recursively Exponentiate 6) Exit\n").upper()
        if choice not in "1234":
            print("Invalid input. Try again.")
            continue
        if choice == '1':
            summands = [
                float(i)
                for i in input(
                    'Input the numbers you would like to add, separated by spaces.\n'
                ).split()
            ]
            start_time = time.time()
            print(test_calculator.add(summands))
            print("--- %s seconds ---" % (time.time() - start_time))
        if choice == '2':
            multicands = [
                float(i)
                for i in input(
                    'Input the numbers you would like to multiply, separated by spaces.\n'
                ).split()
            ]
            start_time = time.time()
            (print(test_calculator.multiply(multicands)))
            print("--- %s seconds ---" % (time.time() - start_time))
        if choice == '3':
            args = [
                int(i)
                for i in input(
                    'Input the base and exponent, separated by a space. For example, for 3^2 input: "3 2".\n'
                ).split()
            ]
            base, exponent = args[0], args[1]
            if len(args) != 2:
                print('Invalid number of input; takes only 2 arguments.\n')
                continue
            start_time = time.time()
            print(test_calculator.iterativeExponentiate(base, exponent))
            print("--- %s seconds ---" % (time.time() - start_time))
        if choice == '4':
            args = [
                int(i)
                for i in input(
                    'Input the base and exponent, separated by a space. '
                    'For example, for 3^2, input: "3 2".\n').split()
            ]
            if len(args) != 2:
                print('Invalid number of input; takes only 2 arguments.\n')
                continue
            start_time = time.time()
            base, exponent = args[0], args[1]
            print(test_calculator.slowExponentiate(base, exponent))
            print("--- %s seconds ---" % (time.time() - start_time))
        if choice == '5':
            break
