from collections import deque


class Solution:
    MIN = -2**31
    MAX = 2**31 - 1

    def reverse(self, number: int) -> int:
        if number < self.MIN or number > self.MAX:
            return 0

        sign , unsign = self._unsign(number)
        result = sign * self._reverse(unsign)

        if result < self.MIN or result > self.MAX:
            return 0

        return result

    def _unsign(self, number: int):
        if number < 0:
            return -1, -number
        else:
            return 1, number

    def _reverse(self, unsign: int):
        reverse_digits = deque()
        factor = 10

        while unsign > 0:
            digit = unsign % factor
            reverse_digits.append(digit)
            unsign = int((unsign - digit) / 10)

        factor = 1
        result = 0
        while len(reverse_digits) > 0:
            digit = reverse_digits.pop()
            if digit > 0:
                result += digit * factor
            factor *= 10

        return result