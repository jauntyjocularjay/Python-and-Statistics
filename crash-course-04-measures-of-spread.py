import math
import statistics as Statistics
import pytilities.console as console

console.clear()

def iqr(data_list: list = [0]):
    if(len(data_list) == 0):
        return None

    data_list.sort()

    if(len(data_list) % 2 == 1):
        data = data_list[:Statistics.median(data_list)-1] + data_list[Statistics.median(data_list):]

    lower_bound = Statistics.median_low(data)-1
    higher_bound = Statistics.median_high(data)

    return data_list[lower_bound:higher_bound]

def main():

    data = [1,2,3,4,5,6,7]
    print(f'IQR of {data}:\n    {iqr(data)}')

    quantiles = Statistics.quantiles(data, n=4)

    for i, x in enumerate(quantiles):
        quantiles[i] = int(x)

    quantiles = [int(x) for x in quantiles]

    print(f'quantiles are:\n    {quantiles}')


main()
