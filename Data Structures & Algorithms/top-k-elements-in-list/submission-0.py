class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        for i in range(len(nums)):
            if nums[i] in my_dict:
                my_dict[nums[i]] += 1
            else:
                my_dict[nums[i]] = 1
        print(my_dict)
                
        amount = k
        my_list = []

        while amount > 0:
            my_num = 0
            count = 0
            for key, value in my_dict.items():
                if value > count:
                    my_num = key
                    count = value
            my_list.append(my_num)
            amount -= 1
            del my_dict[my_num]
        return my_list


        