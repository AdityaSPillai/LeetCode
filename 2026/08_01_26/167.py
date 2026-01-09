#solution 1
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num=set(numbers)
        for i in range(len(num)):
            find=target-numbers[i]
            if find in num:
                if i+1==numbers.index(find)+1:
                    continue
                return [i+1,numbers.index(find)+1]

#solution 2
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)-1
        while right>left:
            if numbers[right]+numbers[left]==target:
                return [left+1,right+1]
            elif numbers[right]+numbers[left]>target:
                right=right-1
            elif numbers[right]+numbers[left]<target:
                left=left+1