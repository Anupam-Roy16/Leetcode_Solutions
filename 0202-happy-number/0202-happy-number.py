class Solution:
#      def isHappy(self, n: int) -> bool:
#         # Create a set named 'hashmap' to keep track of encountered numbers
#         hashmap = set()

#         # Loop will continue until we find a number twice which is not equal to 1
#         while n not in hashmap:
#             # Add the current number 'n' to the set
#             hashmap.add(n)

#             # Calculate the sum of the squares of its digits
#             n = sum(int(digit) ** 2 for digit in str(n))

#             # If the current number is 1, return True as it is a happy number
#             if n == 1:
#                 return True

#         # If the loop completes, it means 'n' entered a cycle without reaching 1, so return #False
#         return False
        
        
        
        
        #another method
        
        def isHappy(self, n: int) -> bool:
        # This can also be solved using the cycle detection algorithm
            slow, fast = self.digitSquareSum(n), self.digitSquareSum(self.digitSquareSum(n))
            while slow != fast:
                slow = self.digitSquareSum(slow)
                fast = self.digitSquareSum(self.digitSquareSum(fast))
            return fast == 1

        def digitSquareSum(self, n):
            # Function to calculate the sum of the squares of digits in a number
            return sum(int(digit) ** 2 for digit in str(n))