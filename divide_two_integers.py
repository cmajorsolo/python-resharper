class Solution():
    def divide(self, dividend, divisor):

        if divisor == 0:
            return -1

        if dividend < divisor and ((dividend < 0 and divisor < 0) or (dividend > 0 and divisor > 0)):
            return 0
        elif dividend == divisor:
            return 1

        positive = (dividend < 0 and divisor < 0) or (dividend > 0 and divisor > 0)

        dividend = abs(dividend)
        divisor = abs(divisor)
        result = 0

        while dividend >= divisor:
            b = divisor
            a = dividend
            counter = 1
            while b + b <= a:
                b += b
                counter += counter
            dividend = dividend - b
            result += counter

        if not positive:
            result = -result

        return min(max(-2147483648, result), 2147483647)

