a = (23, 456, 123, 12, 1345)
print(len([x for x in a if x > 100]))

# WAP to add a given value to a tuple
a = a + (2,)
print(a)

# WAP to find the years in which sachin scored higest and lowest runs
sachin = [(2012, 1200), (2013, 987), (2014, 1345), (2015, 876)]
runs = [x[1] for x in sachin]
year = [x[0] for x in sachin]
print(year[runs.index(max(runs))])
print(year[runs.index(min(runs))])
