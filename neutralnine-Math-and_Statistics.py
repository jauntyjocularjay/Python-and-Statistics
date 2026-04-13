# Title: Statistics Fundamentals in Python
# Author: NeuralNine
# url: https://www.youtube.com/watch?v=cECVvmFOKFc

import math as Math
import statistics as Statistics
import PyTils.console as console

console.clear()

numbers_odd = [10, 10, 10, 50, 60, 1000, 2000]
print(f"numbers_odd: {numbers_odd}")
numbers_even = [10, 10, 50, 60, 1000, 2000]
print(f"numbers_even: {numbers_even}\n")

# Mean (Average)
print(f"mean(numbers_odd):\n    {sum(numbers_odd) / len(numbers_odd)}")
print(f"Statistics.mean(numbers_odd):\n    {Statistics.mean(numbers_odd)}\n")

# Median

def median(sample: list): # concept demo
    if len(sample) == 0:
        print("cannot provide a median of an empty list")

    sample = sorted(sample)
    index = None
    if len(sample) % 2 == 1:
        index = (len(sample) + 1) // 2
        return sample[index - 1]
    else:
        index = len(sample) // 2
        return Statistics.mean([sample[index - 1], sample[index]]) * 1.0

print(f"my function median(numbers_odd):\n    {median(numbers_odd)}")
print(f"statistics.median(numbers_odd):\n    {Statistics.median(numbers_odd)}")
print(f"my function median(numbers_even):\n    {median(numbers_even)}")
print(f"statistics.median(numbers_even):\n    {Statistics.median(numbers_even)}\n")


# Mode

def mode(sample: list): # concept demo
    mode = sample[0]
    highest_occurences = 0
    current_occurences = 0

    for x in set(sample):
        current_occurences = sample.count(x)

        if(highest_occurences < current_occurences):
            highest_occurences = current_occurences
            mode = x
    
    return mode

print(f"my mode(numbers_odd):\n    {mode(numbers_odd)}")
print(f"statistics.mode(numbers_odd):\n    {Statistics.mode(numbers_odd)}\n")

numbers = [10, 10, 10, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100000, 200000]

# Standard Deviation & Variance










