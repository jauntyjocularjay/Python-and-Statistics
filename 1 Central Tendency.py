import statistics as Statistics
import PyTils.console as console

def main():
    console.clear()
    # Measure of Central Tendency
    # A single value that attempts to describe a set of data. Three main tendencies.
    # Mean: the sum of observations divided by the number of observations

    print()
    print("# Measure of Central Tendency")
    print("A single value that attempts to describe a set of data. Three main tendencies:")
    print()


    data = [2,4,7,8,8]

    print( "1) Mean, aka Average: the sum of observations divided by the number of observations")
    print(f"  - the mean of {data} is {Statistics.mean(data)}")
    print()

    # Median: the middle value of the dataset

    # Odd set length
    data = [1, 3, 4]
    print("2) Median: the middle value of the dataset")
    print("  a. In a list of values with an odd number of data points, median is the value at the center of the list.")
    print(f"   - statistics.median({data}): {Statistics.median(data)}")

    #   Median Low: the lower of the two center values
    data = [2,4,6,8]

    print("  b. In a list of values with even data points, the median_low is the lower of two median values.")
    print(f"   - The statistics.median_low low among {data}: {Statistics.median_low(data)}")

    #   Median high: the higher of the two center values
    data = [2,4,6,8]
    print("  c. In a list of values with even data points, the median_high is the higher of two median values.")
    print(f"   - The statistics.median_high high among {data}: {Statistics.median_high(data)}")
    print()


    # Mode : The most common point in a set of data
    data = [3,3,3,10,10,11,15]

    print("3) Mode : The most common point in a set of data")
    print(f" - The mode of {data}: {Statistics.mode(data)}")


    # Measure of variability
    # The spread of data or how data is distributed.

    print()
    print()
    print("# Measure of variability")
    print(" - The spread of data or how data is distributed.")
    print()

    # Range
    # The difference between the largest and smallest data point in the set.
    # The range is directly proportional to the spread.
    # Calculated using statistics.max() and statistics.min()

    data = [1,2,5,9]

    print("1. Range")
    print( "   a. The difference between the largest and smallest data point in the set.")
    print( "   b. The range is directly proportional to the spread.")
    print( "   c. Calculated using statistics.max() and statistics.min()")
    print(f"   d. in the set {data}")
    print(f"     - the max is {max(data)}")
    print(f"     - the min is {min(data)}")
    print(f"     - the range is {max(data)} - {min(data)} = {max(data) - min(data)}")
    print()

    # Variance
    # defined as the average squared deviation from the mean:
    #   - find the difference between every data point and the mean (average)
    #   - square them
    #   - add all of them
    #   - divide by the number of data points
    # use the statistics.variance()

    print( "# Variance")
    print( "   a. defined as the average squared deviation from the mean:")
    print( "     1. find the difference between every data point and the mean (average)")
    print( "     2. square them")
    print( "     3. add all of them")
    print( "     4. divide by the number of data points")
    print( "   b. use the statistics.variance()")

    data = [1,2,4,5,6,7,9]
    print(f"   - The variance of {data} is {Statistics.variance(data)}")
    print()

    # Standard Deviation
    #   - square root of the variance
    #     1. find the variance
    #     2. take the square root
    #   - use statistics.stdev(data_list)

    print( "# Standard Deviation")
    print( "   a. square root of the variance")
    print( "     1. find the variance")
    print( "     2. take the square root")
    print( "   b. use statistics.stdev(data_list)") 
    print(f"   c. The standard deviation of {data} is {Statistics.stdev(data)}") 

    



main()