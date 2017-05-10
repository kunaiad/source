
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
'''
min_price = min(zip(prices.values(), prices.keys()))
# min_price is (10.75, 'FB')
max_price = max(zip(prices.values(), prices.keys()))
# max_price is (612.78, 'AAPL')

print(min_price)
print(max_price)

prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)
# prices_sorted is [(10.75, 'FB'), (37.2, 'HPQ'),
#                   (45.23, 'ACME'), (205.55, 'IBM'),
#                   (612.78, 'AAPL')]

'''
#prices_and_names = zip(prices.values(), prices.keys())
#print(min(prices_and_names))
#print(max(prices_and_names))

#print(min(prices)) # Returns 'AAPL'
#print(max(prices)) # Returns 'IBM'

#print(min(prices.values())) # Returns 10.75
#print(max(prices.values())) # Returns 612.78


#print(min(prices, key=lambda k: prices[k])) # Returns 'FB'
#print(max(prices, key=lambda k: prices[k])) # Returns 'AAPL'


#min_value = prices[min(prices, key=lambda k: prices[k])]
#print(min_value)

#prices = { 'AAA' : 45.23, 'ZZZ': 45.23 }
#print(min(zip(prices.values(), prices.keys())))
#print(max(zip(prices.values(), prices.keys())))
'''
a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}

b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}
'''
# Find keys in common
#print(a.keys() & b.keys()) # { 'x', 'y' }
# Find keys in a that are not in b
#print(a.keys() - b.keys()) # { 'z' }
# Find (key,value) pairs in common
#print(a.items() & b.items()) # { ('y', 2) }

# Make a new dictionary with certain keys removed
#c = {key:a[key] for key in a.keys() - {'z', 'w'}}
#print(c)
# c is {'x': 1, 'y': 2}

'''
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
        seen.add(item)

a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))

def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))


a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
list(dedupe(a, key=lambda d: (d['x'],d['y'])))
print(list(dedupe(a, key=lambda d: (d['x'],d['y']))))

'''

