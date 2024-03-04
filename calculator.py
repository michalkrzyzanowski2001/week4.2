import sys
import logging
logging.basicConfig(level=logging.DEBUG)

def calc(operation, num1, num2):
    result = 0
    if operation == "Addition":
        result = num1 + num2
        logging.info(f'I am adding {num1} and {num2} to get {result}')
    if operation == "Subtraction":
        result = num1 - num2
        logging.info(f'I am subtracting {num2} from {num1} to get {result}')
    if operation == "Division":
        result = num1 / num2
        logging.info(f'I am dividing {num1} by {num2} to get {result}')
    if operation == "Multiplication":
        result = num1*num2
        logging.info(f'I am multiplying {num1} and {num2} to get {result}')
    else:
        logging.error("Your operation input is incorrect")            

if __name__ == "__main__":
    operation = input("Please choose one of the following operations(Addition, Subtraction, Division, Multiplication): ")
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    calc(operation, num1, num2)