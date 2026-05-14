class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0

        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five > 0:
                    five -= 1
                    ten += 1
                else:
                    return False
            else: # It's a 20
                # Priority: Give a 10 and a 5 (saves 5s for later)
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                # Fallback: Give three 5s
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True