import numpy as np;
from scipy.stats import chi2;


# manual chi square function to check on randomness on our own
def chi_square(random_sequence):

    # length of the sequence
    n = len(random_sequence)

    # calculate expected Value with which to fill the sequence for the chi square formula
    expectedValue = random_sequence.sum()/n
    # the sequence for the chi square formula
    expected = np.full((1, n), expectedValue)
    # the chi square formula operands
    Xi_square_vect = (random_sequence - expected)**2/expected
    # the chi square final sum
    Xi_square = Xi_square_vect.sum()
    print("Xi_square: ", Xi_square)

    # the chi square critical value for the null hypothesis to be true (numbers are indeed random)
    Xi_critical = chi2.ppf(q = 0.95, df=n - 1)
    print("Xi_critical: ", Xi_critical)

    # the chi square p value (probability of the null hypothesis)
    p_value = 1 - chi2.cdf(x=Xi_square, df=n - 1)
    print("p_value: ", p_value)

    # return all three values for the fullness of the answer
    return (True if p_value > 0.5 else False, Xi_square, p_value)