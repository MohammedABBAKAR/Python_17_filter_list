# Filter Strings from Array

# Create a function that takes a list of strings and integers, 
# and filters out the list so that it returns a list of integers only.
# Examples

# filter_list([1, 2, 3, "a", "b", 4]) ➞ [1, 2, 3, 4]

# filter_list(["A", 0, "Edabit", 1729, "Python", "1729"]) ➞ [0, 1729]

# filter_list(["Nothing", "here"]) ➞ []


def filter_list(l):

    strlis=[]
    for i in l:
        if isinstance(i,int):
            strlis.append(i)
    return strlis
print(filter_list([1, 2, 3, "a", "b", 4]))
print(filter_list(["A", 0, "Edabit", 1729, "Python", "1729"]))



def filter_list(lst):
    result = [i for i in lst if isinstance(i, int)]
    return result

# Test cases
print(filter_list([1, 2, 3, "a", "b", 4]))  # ➞ [1, 2, 3, 4]
print(filter_list(["A", 0, "Edabit", 1729, "Python", "1729"]))  # ➞ [0, 1729]
print(filter_list(["Nothing", "here"]))  # ➞ []
