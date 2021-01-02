class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num1 = nums
        num2 = {}
        for i in range(len(num1)):
            current = target - num1[i]
            if current not in num2.keys():
                num2[current] = set()
            num2[current].add(i)
        #print(num2)
        for i in range(len(num1)):
            if num1[i] in num2.keys():
                if i not in num2[num1[i]]:
                    index_1 = i
                    index_2 = num2[num1[i]].pop()
                    break
                elif len(num2[num1[i]])>1:
                    num2[num1[i]].remove(i)
                    print(num2)
                    index_1 = i
                    index_2 = num2[num1[i]].pop()
                    break
                else:
                    continue
        return [index_1,index_2]
