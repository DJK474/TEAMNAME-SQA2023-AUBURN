
from ast import operator
import random 


#These methods make an simple interest calculator

def get_int(prompt, low):
    while True:
        anInteger = int(input(prompt))
        if anInteger > low:
            return anInteger
        else:
            print("Entry must be an integer greater than 0 Please try again.")
            
def get_float(prompt, low):
    while True:
        anInteger = float(input(prompt))
        if anInteger > low:
            return anInteger
        else:
            print("Entry must be an integer greater than 0.0 Please try again.")

def calculate_simple_interest(principle,interest,years=1):
    result = principle * (interest/100) * years
    return result

#Two new methods

def calucate_percentage(percent, number):
    if percent > 0:
        total = percent * number
        return total
    else:
        print("Incorrect entry!")
    
def calculate_total(interest, percent):
    total = interest + percent
    return total


def fuzz():
    #print("")
    #loan = get_int("Enter the loan: ", 0)
    #interest_rate = get_float("Enter the interest rate: ", 0)
    #year = get_int("Enter the number of years: ", 0)
    #result = calculate_simple_interest(loan,interest_rate,year)

    #calucate_percentage(rtry, 56)
    
    number_two_decimal = "{:.2f}".format(result)
    
    #print(result)
    print("")
    print("\tThe interest on a loan of $", loan, " at ", interest_rate, "% interest rate for ", year, " year", ('s' if year > 1 else ''), "\nis $", number_two_decimal, ".", sep='')





if __name__=='__main__':
    fuzz()
