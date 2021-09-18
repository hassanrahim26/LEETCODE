# PROBLEM LINK:- https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

class Solution:
    def average(self, salary: List[int]) -> float:
        n = len(salary)
        salary.sort()
        sum = 0.00
        avg = 0.00
        for i in range(0,n):
            sum += salary[i];
        avg = sum - (salary[0] + salary[n-1]);
        return avg/(n-2);
