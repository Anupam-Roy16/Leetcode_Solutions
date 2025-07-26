class Solution:
    def minimumSum(self, num: int) -> int:
        array_of_digit = []
        while num:
            array_of_digit.append(num%10)
            num //=10
        array_of_digit.sort()
        num1 = array_of_digit[0]*10 + array_of_digit[3]
        num2 = array_of_digit[1]*10 + array_of_digit[2]
        return num1 +num2

        