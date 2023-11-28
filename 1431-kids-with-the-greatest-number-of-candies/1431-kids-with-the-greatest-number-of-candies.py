class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        max_element = max(candies)
        for i in candies:
            if i + extraCandies >= max_element:
                result.append(True)
                print(i+extraCandies)
            else:
                result.append(False)
                print("sd")
        print(result)
        return result
        