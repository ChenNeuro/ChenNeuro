def polynomial_long_division(dividend, divisor):
    """
    Performs polynomial long division and returns the quotient and remainder.
    Assumes that the input polynomials are represented as lists of coefficients,
    where the index of the coefficient corresponds to the power of x.

    Args:
        dividend (list): Coefficients of the dividend polynomial.
        divisor (list): Coefficients of the divisor polynomial.

    Returns:
        tuple: (quotient, remainder)
    """
    quotient = [0] * (len(dividend) - len(divisor) + 1)
    remainder = dividend.copy()

    while len(remainder) >= len(divisor):
        # Calculate the next term of the quotient
        coef = remainder[0] / divisor[0]
        quotient[len(remainder) - len(divisor)] = coef

        # Subtract the term from the remainder
        for i in range(len(divisor)):
            remainder[i] -= coef * divisor[i]

        # Remove leading zeros from the remainder
        while len(remainder) > 0 and remainder[0] == 0:
            remainder.pop(0)

    return quotient, remainder

# Example usage
dividend = [3, 2, -5, 1]  # Coefficients of P(x) = 3x^3 + 2x^2 - 5x + 1
divisor = [1, -2]         # Coefficients of Q(x) = x - 2

quotient, remainder = polynomial_long_division(dividend, divisor)
print(f"Quotient: {quotient}")
print(f"Remainder: {remainder}")
 