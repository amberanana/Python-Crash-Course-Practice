# 8.2 Practice

# 8-3 T-shirts
def make_shirt(size, pattern):
    print("\nI need a " + size + " size shirt.")
    print("I would like to print " + pattern + " on my shirt.")

make_shirt('medium','Hello')

# 8-4 Large T-shirt
def make_shirt(size, pattern='I love Python'):
    print("\nI need a " + size + " size shirt.")
    print("I would like to print " + pattern + " on my shirt.")
make_shirt('large')
make_shirt('medium')
make_shirt('small',pattern='whatever')

# 8-5 City
def describe_city(city, country='China'):
    print("\n" + city + " is in " + country + ".")

describe_city('Reykjavik', country='Iceland')
describe_city('Hangzhou')
describe_city('Shanghai')
