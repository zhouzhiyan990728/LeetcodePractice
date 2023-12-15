# 1716.Calculate Money in Leetcode Bank

## Question
Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.

### Example
```
Input: n = 4
Output: 10
Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.
```

## Solution
* Calculate the week and day number using the given days.
* There are two rules in the bank:
1. On every subsequent Monday, 1 more dollar will be put in more than the previous Monday.
2. Every day from Tuesday to Sunday, it will put in 1 more than the day before.

## Code
```python3
class Solution:
    def totalMoney(self, n: int) -> int:
        week = int(n/7);
        day = n%7;
        money = 0;
        if week>0:
            for i in range(week):
                money += 7*(4+i);
        
        for i in range(day):
            money += i+week+1;
        
        return money;
```
