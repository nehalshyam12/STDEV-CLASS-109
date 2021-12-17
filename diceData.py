import statistics

dice_result = []

for i in range (0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_result.append(dice1+dice2)   

mean = sum(dice_result)/len(dice_result)
std_deviation = statistics.stdev(dice_result)