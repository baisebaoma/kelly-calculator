# kelly-calculator
Use Kelly criterion to calculate how many bets you need to place in a gambling game. Specifically, losing this bet means losing all bets.

## Usage

Fill in the blanks and run the code!

```python
# What is the name of this random event?
# 这个随机事件的名字是？
note = "T1 在 S13 全球总决赛决赛上获胜"

# What is your estimate of the probability of this random event occurring?
# 你估计这个随机事件发生的概率是？
winrate_estimated_by_yourself = 1

# What are the odds of this random event (including principal)?
# 这个随机事件的赔率是（包含本金）？
pl = 1.375

# What are the odds that this random event will not occur?
# 这个随机事件不发生的赔率是？
pl_negative = 3.180

# What is all your principal used for gambling?
# 你的所有用于赌博的本金是？
bj = 10000

# Press Run!
# 按下运行吧！
```

## Sample Output
```
在 T1 在 S13 全球总决赛决赛上获胜 事件中，赔率为 1.375，它的对立事件的赔率为 3.18：
也就是庄家预估该事件的概率为 69.81%。
    如果按照庄家预估胜率，本场你获得期望 -4.01% 赌注，也就是期望 -4.01% 本金。
在你预估概率为 100.00% 的情况下：
    凯利公式推荐赌注为 100.00% 本金，本场你获得期望 37.50% 赌注，也就是期望 37.50% 本金。
    本金 10000 元的情况下，凯利公式推荐赌注为 10000.00 元，本场如果胜利获得 3750.00 元。总期望为 3750.00 元

In the T1 在 S13 全球总决赛决赛上获胜 event, the odds were 1.375, while the odds for its opposing event were 3.18:
That is, the banker estimated the probability of this event to be 69.81%.
If you use the banker's estimated winning rate, you will receive an expected -4.01% stake in this game, which means an expected -4.01% principal.
Under your estimated probability of 100.00%:
Kelly criterion recommends a bet of 100.00% principal, and in this game you receive the expected 37.50% bet, which is the expected 37.50% principal.
In the case of a principal of 10000 yuan, Kelly criterion recommends a bet of 10000.00 yuan.
If you win, you will receive 3750.00 yuan. The total expected bet is 3750.00 yuan.
```
