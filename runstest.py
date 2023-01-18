import math
from random import random, randrange;
import statistics;

def runsTest(random_sequence):


    n = len(random_sequence)
    # numbers which are lesser than the median and greater than the median accordingly
    n1, n2 = 0, 0
    # The observed number of runs
    # Run is a consecutive positive or negative numbers
    # Positive number is the number which greater than the median of a sample
    # Negative number is the number which is lesser than the median of a sample
    R = 0
    # The expected number of runs
    R_exp = 0
    # median finding with the help of the statistics module of the Python
    median = statistics.median(random_sequence)
    # flags for comfort of counting runs
    isIncreasing = False
    isDecreasing = False

    for i in range(n):
        # if the sequence of positive numbers ends then increase number of runs and start a decreasing sequence
        # (a consecutive sequence of positive numbers) and also end the increasing sequence
        if (random_sequence[i] < median):
            if isIncreasing:
                R += 1
            isDecreasing = True
            isIncreasing = False
            n2 += 1
        # opposite to the first case but with the start of the increasing sequence and ending of the decreasing sequence
        else :
            if (isDecreasing):
                R += 1
            isIncreasing = True
            isDecreasing = False
            n1 += 1

    # expected number of runs if the sample were to be random
    R_exp = 2*n1*n2/(n1 + n2) + 1
    # the deviation of the sample
    S_R = math.sqrt(2*n1*n2*(2*n1*n2 - n1 - n2)/((n1 + n2)**2*(n1 + n2 - 1)))

    # the main value of the runs test
    Z = (R-R_exp)/S_R

    # the critical value to compare the main value of the test with
    Z_critical = 1.96
    # if the |Z| > Z_critical then the numbers are NOT random
    if abs(Z) > Z_critical:
        return(False, Z)
    # otherwise the numbers may be random
    else:
        return (True, Z)

# function to perform safe cast (without errors) of one type to another
def safe_cast(value, type, default=None):
    try:
        return type(value)
    except(ValueError, TypeError):
        return default

# a function to get the input from user with good interface and checks of the input

def get_input_from_user():

    random_sequence = []

    element_type = input("Which element do you wish to generate sequence with? Choose one of the following: number or letter")
    while element_type not in("number", "letter"):
        element_type = input("You did not enter one of the variants in the braces. Please enter either \"number\" or \"letter\". Which element do you wish to generate sequence with? Choose one of the following: number or letter")
    
    random_or_no = input("Do you wish to generate a random sequence or to input it yourself? (Y to generate a sequence with Python or N to input it yourself): ")
    while random_or_no not in "NY":
        random_or_no = input("Please enter either N or Y (uppercase only). Do you wish to generate a random sequence or to input it yourself? (Y to generate a sequence with Python or N to input it yourself): ")

    if random_or_no=="N":

        str_number = input("Input a number of elements in a random sequence")
        n = safe_cast(str_number, float)
        while (n == None or n <= 0 or n % 1 != 0):
            str_number = input("You entered invalid length of a random sequence. Input a number of elements in a random sequence")
            n = safe_cast(str_number, float)

        if (element_type == "letter"):

            for i in range(n):
            
                random_sequence.append(None)
                random_sequence[i] = input("Please, enter a character:")
                while (len(random_sequence[i]) != 1 or ord(random_sequence[i]) > 1_114_112):
                    random_sequence[i] = input("You entered no character or more than one character. Please, enter a character:")
                random_sequence[i] = ord(random_sequence[i])
        else:

            for i in range(n):
            
                random_sequence.append(None)
                random_sequence[i] = input("Please, enter a number:")
                while (safe_cast(random_sequence, float) == None):
                    random_sequence[i] = input("Please, enter a number:")
                random_sequence[i] = float(random_sequence[i])

    elif random_or_no=="Y":

        random_or_no = input("Do you wish to specify a length of a sequence to generate? (Y to generate a random length or N to input it yourself): ")
        while random_or_no not in "NY":
            random_or_no = input("Please enter either N or Y (uppercase only). Do you wish to specify a length of a sequence to generate? (Y to generate a random length or N to input it yourself): ")

        if (random_or_no == "Y"):
            n = int(randrange(1000, 10000))
        else :
            str_number = input("Input a number of elements in a random sequence")
            n = safe_cast(str_number, float)
            while (n == None or n <= 0 or n % 1 != 0):
                str_number = input("You entered invalid length of a random sequence. Input a number of elements in a random sequence")
                n = safe_cast(str_number, float)

        random_sequence = [random.random() for i in range(n)] if element_type == "number" else [randrange(1, 1_114_112) for i in range(n)]

    return random_sequence

# if we start this file directly - get input from the user
if __name__ == '__main__':

    random_sequence = get_input_from_user()

    print(runsTest(random_sequence)
    )
