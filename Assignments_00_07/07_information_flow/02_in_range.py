def in_range(n, low, high):
    """Returns True if n is between low and high, inclusive."""
    return low <= n <= high


print(in_range(7, 9, 60)) 
print(in_range(4, 1, 16)) 
print(in_range(7, 6, 1))  
