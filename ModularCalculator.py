import time
import RecursiveExponentCalculator


class ModularCalculator:
    """
    This class contains methods of different utilities used in everyday calculations, using object-oriented design.
    """

    def add(self, numbers):
        """"Return the product of the number(s) in numbers.
        >>> add([6, 4])
        25
        >>> add([1, 0])
        1
        """""
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
        """""
        return numbers[0] - ModularCalculator.add(numbers[1:])

    def multiply(self, numbers):
        """"Return the product of the number(s) in numbers.
        >>> multiply([6, 4])
        24
        >>> multiply([1, 0])
        0
        """
        init = 1
        result = numbers[0]
        rest = [elem for elem in numbers[1:]]
        if 0 in numbers:
            return 0
        for rest_elem in rest:
            init = init * rest_elem
        result = result * init
        return result

    def divide(self, numbers):
        """"A higher-order function that return the quotient of the number(s) in numbers.
        >>> divide([6, 4])
        24
        >>> divide([8, 4, 2]) # 8 * 1/4 * 1/2
        1
        >>> divide([1, 0])
        Whoops. Can't divide by zero. 😭
        """
        try:
            return numbers[0] / ModularCalculator.multiply(self, numbers[1:])
        except ZeroDivisionError:
            return 'Whoops. Cannot divide by zero. 😭'

    def two_integer_exponentiate(self, base, exponent):
        """"Returns the result of raising base to exponent, where base and exponent are integers.
        >>> two_integer_exponentiate([3, 2])
        24
        >>> two_integer_exponentiate([1, 0])
        1
        >>> two_integer_exponentiate([3, 999999])
        5992367055585812... ≈ 5.99 x 10^477120
        """
        result = 1
        i = 0
        if not isinstance(base, int) or not isinstance(exponent, int):  # imposed in case another main() not imposing integer-only.
            return 'Base and exponent must both be integers.'
        if exponent == 0 or base == 1:
            return 1
        elif base == 0:
            return base
        while i < abs(exponent):  # accounts for case of a negative exponent.
            if exponent < 0:
                result = ModularCalculator.multiply(self, [result, ModularCalculator.divide(self, [1, base])])
            elif exponent > 0:
                result = ModularCalculator.multiply(self, [result, base])
            i = ModularCalculator.add(self, [i, 1])
        return result


if __name__ == '__main__':

    obj = ModularCalculator()
    print('Welcome to Modular Calculator! 🙂')

    while True:
        choice = input('Choose your operation. 🤓\n'
                       '1) Add 2) Subtract 3) Multiply 4) Divide 5) Two-integer Exponentiate 6) Exit\n')
        if choice not in "123456":
            print("Invalid input. Please choose from 1-6.")
            continue
        elif choice == '1':
            summands = [float(i) for i in
                        input('Input the numbers you would like to add, separated by spaces.\n').split()]
            if len(summands) < 2:
                print('Invalid number of input; takes at least two summands.\n')
                continue
            start_time = time.time()
            print(obj.add(summands))
            print('--- Calculated in %s second(s)! ---' % (time.time() - start_time))
        elif choice == '2':
            args = [float(i) for i in
                        input('Input the numbers you would like to subtract from the first, separated by spaces.\n'
                              'For 8 - 4 - 4: "8 4 4"\n'
                              'Note: All numbers following the first one will be subtracted from the first.\n').split()]
            if len(args) < 2:
                print('Invalid number of input; takes at least two summands.\n')
                continue
            start_time = time.time()
            print(obj.add(args))
            print('--- Calculated in %s second(s)! 😮 ---' % (time.time() - start_time))

        elif choice == '3':
            multicands = [float(i) for i in
                          input('Input the numbers you would like to multiply, separated by spaces.\n').split()]
            if len(multicands) < 2:
                print('Invalid number of input; takes at least two multicands.\n')
                continue
            start_time = time.time()
            (print(obj.multiply(multicands)))
            print('--- Calculated in %s second(s)! 😮 ---' % (time.time() - start_time))
        elif choice == '4':
            args = [int(i) for i in
                    input('Input the dividend and divisor(s). For 6 ÷ 4 ÷ 2: "6 4 2"\n').split()]
            if len(args) < 2:
                print('Invalid number of input; takes 1 dividend and 1 or more divisors.\n')
                continue
            start_time = time.time()
            print(obj.divide(args))
            print('--- Calculated in %s second(s)! 😮---' % (time.time() - start_time))
        elif choice == '5':
            try:
                args = [int(i) for i in
                    input('Input the base and exponent, separated by a space. For 3^2: "3 2".\n').split()]
                base, exponent = args[0], args[1]
            except ValueError:
                print('The base and exponent must both be integers. Please try again.')
                continue
            if len(args) != 2:
                print('Invalid number of input; takes only 2 arguments: 1 base and 1 exponent.\n')
                continue
            start_time = time.time()
            print(obj.two_integer_exponentiate(base, exponent))
            print('--- Calculated in %s second(s)! 😮 ---' % (time.time() - start_time))
        else:
            print('Goodbye! I hope your problem is solved. 😏')
            break
