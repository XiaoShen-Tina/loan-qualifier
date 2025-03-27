# Get three test scores and calculate the total and average with proper message
score1 = 1
score2 = 2
score3 = 3
# Calculate the amount of 3 scores
total_scores = score1 + score2 + score3
# Calculate the average number of 3 scores
average_scores = (score1 + score2 + score3) / 3

score1 = float(input("Enter the first test score: ")) #浮点数（float） 是 带小数点的数值，比如 3.14、2.0、-7.5，它可以表示小数或分数。在 Python 里，整数（int）和浮点数（float）是不同的数据类型
score2 = float(input("Enter the second test score: "))
score3 = float(input("Enter the third test score: "))
total_scores = score1 + score2 + score3
Average_scores = total_scores/3
print(total_scores)
print(Average_scores)