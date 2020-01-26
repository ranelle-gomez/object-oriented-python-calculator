import time
import sys


class RecursiveExponentiation:
    """
    A class with two different recursive methods of calculating 2-positive-integer exponentiation.
    """
    sys.setrecursionlimit(9999999)

    def tail_recursive_exponentiate(self, base, exponent):
        """"Returns the result of raising base to exponent, where base and exponent are integers.
        This method utilizes tail recursion, which closes the previous frame once the first recursive
        call is made.
        >>> tail_recursive_exponentiate([3, 2])
        24
        >>> tail_recursive_exponentiate([1, 0])
        1
        >>> tail_recursive_exponentiate([3, 99])
        35732755827665509164214129957981...
        """
        if not isinstance(base, int) or not isinstance(exponent, int):
            return 'Base and exponent must both be integers.'

        def exp_tail(base, exponent, result):
            if exponent == 0 or base == 1:
                return result
            else:
                return exp_tail(base, exponent - 1, result * base)
        return exp_tail(base, exponent, 1)

    def recursive_exponentiate(self, base, exponent):
        """"The same function signature as tail_recursive_exponentiate, using conventional recursion.
        >>> recursive_exponentiate([3, 2])
        24
        >>> recursive_exponentiate([1, 0])
        1
        >>> recursive_exponentiate([3, 850])
        35732755827665509164214129957981...
        """
        result = 1
        if not isinstance(base, int) or not isinstance(exponent, int):
            return 'Base and exponent must both be integers.'
        elif exponent == 0 or base == 1:
            return result
        else:
            return base * RecursiveExponentiation.recursive_exponentiate(self, base, exponent - 1)


if __name__ == '__main__':

    obj = RecursiveExponentiation()
    print(sys.getrecursionlimit(), 'is the recursion limit.')

    while True:
        choice = input("1) Tail-recursive 2) Conventional-recursive 3) Exit\n")
        if choice not in "123":
            print("Invalid input. Please choose from 1-3.")
        elif choice == '1':
            args = [int(i) for i in
                    input('Input the base and exponent, separated by a space. For example, for 3^2, input: "3 2".\n').split()]
            base, exponent = args[0], args[1]
            if len(args) != 2 or base < 0 or exponent < 0:
                print('Invalid input; takes only 2 positive-integer arguments.\n')
                continue
            start_time = time.time()
            print(obj.tail_recursive_exponentiate(base, exponent))
            print("--- %s second(s) ---" % (time.time() - start_time))
        elif choice == '2':
            args = [int(i) for i in
                    input('Input the base and exponent, separated by a space. For example, for 3^2, input: "3 2".\n').split()]
            base, exponent = args[0], args[1]
            if len(args) != 2 or base < 0 or exponent < 0:
                print('Invalid input; takes only 2 positive-integer arguments.\n')
                continue
            start_time = time.time()
            print(obj.recursive_exponentiate(base, exponent))
            print("--- %s second(s) ---" % (time.time() - start_time))
        else:
            print('Goodbye!')
            break
