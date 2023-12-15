class Solution:
    def totalMoney(self, n: int) -> int:
        week = int(n / 7);
        day = n % 7;
        money = 0;
        if week > 0:
            for i in range(week):
                money += 7 * (4 + i);

        for i in range(day):
            money += i + week + 1;

        return money;