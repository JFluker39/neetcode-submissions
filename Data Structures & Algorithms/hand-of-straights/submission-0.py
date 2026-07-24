class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        my_dict = {}
        for h in hand:
            my_dict[h] = 1 + my_dict.get(h, 0)
        max_val = max(hand)
        
        while my_dict:
            count = 0
            min_val = min(my_dict)
            val = min_val
            while count != groupSize:
                if val not in my_dict:
                    return False
                my_dict[val] -= 1
                if my_dict[val] == 0:
                    del my_dict[val]
                val += 1
                count += 1
            
        return True