# Day 6: The Central Limit Theorem III
import math

# read inputs
sample = int(input())
mu = int(input())
std = int(input())
inte = float(input())
z = float(input())

# lower limit
print(round(mu - z*(std/math.sqrt(sample)), 2))

# higher limit
print(round(mu + z*(std/math.sqrt(sample)), 2))