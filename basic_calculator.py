class AdvancedCalculator:
    def __init__(self):
        print("**** Advanced Calculator ****")

    def get_numbers(self):
        while True:
            try:
                self.num1 = float(input("Enter the First Number: "))
                self.num2 = float(input("Enter the Second Number: "))
                break
            except ValueError:
                print("Error: Invalid input! Please enter valid numbers.")

    def addition(self):
        return self.num1 + self.num2

    def subtraction(self):
        return self.num1 - self.num2

    def division(self):
        if self.num2 == 0:
            return "Error: Cannot divide by zero!"
        else:
            return self.num1 / self.num2

    def multiplication(self):
        return self.num1 * self.num2

    def calculate(self):
        while True:
            try:
                print("1. Addition\n2. Subtraction\n3. Division\n4. Multiplication\n5. Exit")
                choice = int(input("Enter your choice: "))

                if choice == 1:
                    print("Result:", self.addition())
                elif choice == 2:
                    print("Result:", self.subtraction())
                elif choice == 3:
                    print("Result:", self.division())
                elif choice == 4:
                    print("Result:", self.multiplication())
                elif choice == 5:
                    print("Exiting...")
                    return
                else:
                    print("Invalid choice! Please enter a number between 1 and 5.")

                cont = input("Do you want to continue (yes/no): ").lower()
                if cont != "yes":
                    print("Exiting...")
                    return
                else:
                    self.get_numbers()
            except ValueError:
                print("Error: Invalid input! Please enter valid numbers.")
            except Exception as e:
                print("An error occurred:", str(e))


# Create an instance of the AdvancedCalculator class and start the calculator
calculator = AdvancedCalculator()
calculator.get_numbers()
calculator.calculate()
