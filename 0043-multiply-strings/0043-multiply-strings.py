class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = int(num1)
        num2 = int(num2)
        num2 *= num1
        return str(num2)
        