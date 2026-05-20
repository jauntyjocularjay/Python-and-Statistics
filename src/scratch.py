from quantkit.stats import *
from quantkit.pytilities import *
from pprint import pprint

console.clear()

result = geoh(6,5,4,2)

print('geoh(6,5,4,2)')
print(f'    fraction: {result}')
print(f'    float: {float(result)}')

result = pois(1, 0.75)

print('pois(1, 0.75):')
print(f'    fraction: {result}')
print(f'    float: {float(result)}')