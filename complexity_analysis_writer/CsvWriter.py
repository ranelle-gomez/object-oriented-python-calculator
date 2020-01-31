import csv
import ModularCalculator
import RecursiveExponentCalculator
import time


class WriteCSV:
    def csv_writer_recursive(self, base_range, exponent_range):
        with open('recursive.csv', 'w') as csvfile:
            filewriter = csv.writer(csvfile,
                                    delimiter=',',
                                    quotechar='|',
                                    quoting=csv.QUOTE_MINIMAL)
            for p in range(exponent_range):
                start_time = time.time()
                result = RecursiveExponentCalculator.RecursiveExponentiation.recursive_exponentiate(
                    self, base_range, p)
                end_time = time.time() - start_time
                filewriter.writerow([base_range, p, end_time])
                print("recursive. base: ", base_range, "power: ", p, "time: ",
                      end_time, "result: ", result)

    def csv_writer_recursive_range(self, base_range, exponent_range):
        with open('recursive_1.csv', 'w') as csvfile:
            filewriter = csv.writer(csvfile,
                                    delimiter=',',
                                    quotechar='|',
                                    quoting=csv.QUOTE_MINIMAL)
            for b in range(base_range):
                for p in range(exponent_range):
                    start_time = time.time()
                    result = RecursiveExponentCalculator.RecursiveExponentiation.recursive_exponentiate(
                        self, b, p)
                    end_time = time.time() - start_time
                    filewriter.writerow([b, p, end_time])
                    print("recursive. base: ", b, "power: ", p, "time: ",
                          end_time, "result: ", result)

    def csv_writer_tail_recursive(self, base_range, exponent_range):
        with open('tail_recursive.csv', 'w') as csvfile:
            filewriter = csv.writer(csvfile,
                                    delimiter=',',
                                    quotechar='|',
                                    quoting=csv.QUOTE_MINIMAL)
            for p in range(exponent_range):
                start_time = time.time()
                result = RecursiveExponentCalculator.RecursiveExponentiation.tail_recursive_exponentiate(
                    self, base_range, p)
                end_time = time.time() - start_time
                filewriter.writerow([base_range, p, end_time])
                print("tail_recursive. base: ", base_range, "power: ", p,
                      "time: ", end_time, "result: ", result)

    def csv_writer_tail_recursive_range(self, base_range, exponent_range):
        with open('tail_recursive.csv', 'w') as csvfile:
            filewriter = csv.writer(csvfile,
                                    delimiter=',',
                                    quotechar='|',
                                    quoting=csv.QUOTE_MINIMAL)
            for b in range(base_range):
                for p in range(exponent_range):
                    start_time = time.time()
                    result = RecursiveExponentCalculator.RecursiveExponentiation.tail_recursive_exponentiate(
                        self, b, p)
                    end_time = time.time() - start_time
                    filewriter.writerow([b, p, end_time])
                    print("tail_recursive. base: ", b, "power: ", p, "time: ",
                          end_time, "result: ", result)

    def csv_writer_iterative(self, base_range, exponent_range):

        with open('iterative.csv', 'w') as csvfile:
            filewriter = csv.writer(csvfile,
                                    delimiter=',',
                                    quotechar='|',
                                    quoting=csv.QUOTE_MINIMAL)
            for p in range(exponent_range):
                start_time = time.time()
                result = ModularCalculator.ModularCalculator.two_integer_exponentiate(
                    self, base_range, p)
                end_time = time.time() - start_time
                filewriter.writerow([base_range, p, end_time])
                print("iterative. base: ", base_range, "power: ", p, "time: ",
                      end_time, "result: ", result)

    def csv_writer_iterative_range(self, base_range, exponent_range):
        with open('iterative.csv', 'w') as csvfile:
            filewriter = csv.writer(csvfile,
                                    delimiter=',',
                                    quotechar='|',
                                    quoting=csv.QUOTE_MINIMAL)
            for b in range(base_range):
                for p in range(exponent_range):
                    start_time = time.time()
                    result = ModularCalculator.ModularCalculator.two_integer_exponentiate(
                        self, b, p)
                    end_time = time.time() - start_time
                    filewriter.writerow([b, p, end_time])
                    print("iterative. base: ", b, "power: ", p, "time: ",
                          end_time, "result: ", result)


if __name__ == '__main__':

    obj = WriteCSV()

    while True:
        base_and_exp = [
            int(i) for i in input(
                "Choose a base and exponent, separated by a space.\n").split()
        ]
        if len(base_and_exp
               ) != 2 or base_and_exp[0] < 1 or base_and_exp[1] < 1:
            print("Invalid input. 2 positive integers")
            continue
        base = base_and_exp[0] + 1
        exp = base_and_exp[1] + 1
        choice = input(
            "What do you want to export for measurements? 1) Recursive 2) Tail-recursive 3) Iterative "
            "4) Everything with fixed base and up to exponent 5) Everything for base and exponent 6) Exit\n"
        )
        if choice not in "123456":
            print('Invalid. Must choice 1-6. Try again.')
            continue
        elif choice == '1':
            obj.csv_writer_recursive(base, exp)
        elif choice == '2':
            obj.csv_writer_tail_recursive(base, exp)
        elif choice == '3':
            obj.csv_writer_iterative(base, exp)
        elif choice == '4':
            obj.csv_writer_recursive(base, exp)
            obj.csv_writer_tail_recursive(base, exp)
            obj.csv_writer_iterative(base, exp)
        elif choice == '5':
            obj.csv_writer_recursive_range(base, exp)
            obj.csv_writer_tail_recursive_range(base, exp)
            obj.csv_writer_iterative_range(base, exp)
        else:
            print('Goodbye!')
            continue
