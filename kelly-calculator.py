"""
Use Kelly criterion to calculate how many bets you need to place in a gambling game.
Specifically, losing this bet means losing all bets.
Please fill in the following question and click on 'Run'!

用凯利公式来计算你需要在一个赌局里下多少赌注。特别地，输掉这个赌局时输掉所有的赌注。
请填下面问题，然后点击运行吧！
"""

# What is the name of this random event?
# 这个随机事件的名字是？
note = "T1 在 S13 全球总决赛决赛上获胜"

# What is your estimate of the probability of this random event occurring?
# 你估计这个随机事件发生的概率是？
winrate_estimated_by_yourself = 0.8

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

winrate_dealer = 1 / pl / (1 / pl + 1 / pl_negative)
kelly_suggested_percentage = (winrate_estimated_by_yourself * pl - 1) / (pl - 1)
expected_income_percentage = winrate_estimated_by_yourself * (pl - 1) - (1 - winrate_estimated_by_yourself)

print(f"在 {note} 事件中，赔率为 {pl}，它的对立事件的赔率为 {pl_negative}：\n"
      f"也就是庄家预估该事件的概率为 {winrate_dealer:.2%}。\n"
      f"如果按照庄家预估胜率：\n"
      f"    本场你获得期望 {winrate_dealer * (pl - 1) - (1 - winrate_dealer):.2%} 赌注。\n"
      f"在你预估概率为 {winrate_estimated_by_yourself:.2%} 的情况下：\n"
      f"    凯利公式推荐赌注为 {kelly_suggested_percentage:.2%} 本金，"
      f"本场你获得期望 {expected_income_percentage:.2%} 赌注，也就是期望 "
      f"{expected_income_percentage * kelly_suggested_percentage:.2%} 本金。\n"
      f"    本金 {bj} 元的情况下，凯利公式推荐赌注为 {kelly_suggested_percentage * bj:.2f} 元，"
      f"本场如果胜利获得 {kelly_suggested_percentage * bj * (pl - 1):.2f} 元。"
      f"总期望为 {(winrate_estimated_by_yourself * (pl - 1) - (1 - winrate_estimated_by_yourself)) * kelly_suggested_percentage * bj:.2f} 元。\n"
      )
print(f"In the {note} event, the odds were {pl}, while the odds for its opposing event were {pl_negative}:\n"
      f"that is, the banker estimated the probability of this event to be {winrate_dealer:.2%}.\n"
      f"If you use the banker's estimated winning rate,\n"
      f"    you will receive an expected {winrate_dealer * (pl - 1) - (1 - winrate_dealer):.2%} stake in this game.\n"
      f"Under your estimated probability of {winrate_estimated_by_yourself:.2%}:\n"
      f"    Kelly criterion recommends a bet of {kelly_suggested_percentage:.2%} principal, "
      f"and in this game you receive the expected {expected_income_percentage:.2%} bet, "
      f"which is the expected {expected_income_percentage * kelly_suggested_percentage:.2%} principal.\n"
      f"    In the case of a principal of {bj} yuan, Kelly criterion recommends a bet of {kelly_suggested_percentage * bj:.2f} yuan.\n"
      f"    If you win, you will receive {kelly_suggested_percentage * bj * (pl - 1):.2f} yuan. "
      f"The total expected bet is {(winrate_estimated_by_yourself * (pl - 1) - (1 - winrate_estimated_by_yourself)) * kelly_suggested_percentage * bj:.2f} yuan.")
