def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    #YOUR CODE HERE
    if k == 0:
        return False
    if k == 1:
        return True

    sum = 0
    for i in range(1,k):
        sum += i
        if sum == k:
            return True
    return False

print is_triangular(0)
print is_triangular(1)
print is_triangular(2)
print is_triangular(3)
print is_triangular(6)
print is_triangular(9)
print is_triangular(10)

def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    # Your code here
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    word = ''
    for letter in s:
        if letter not in vowels:
            word += letter
    print(word)

print_without_vowels("This is great!")
print_without_vowels("a")
print_without_vowels("aNd, nOW! I'm --so-- t35t1n@ those special chars!!")
print_without_vowels('Here is a simple sentence that makes sense. BYE.')

def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number
        of times in L. If no such element exists, returns None """
    # Your code here
    dicts = dict()
    for element in L:
        if element in dicts:
            dicts[element] += 1
        else:
            dicts[element] = 1
    choose = []
    for key in dicts:
        if dicts[key] %2 != 0:
            choose.append(key)
    if len(choose) == 0:
        return  None
    else:
        return max(choose)

print largest_odd_times([2,2,4,4])
print largest_odd_times([3,9,5,3,5,3])

def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    #YOUR CODE HERE
    dicts = dict()
    for key in d:
        if d[key] not in dicts:
            dicts[d[key]] = []
            dicts[d[key]].append(key)
        else:
            dicts[d[key]].append(key)
    for key in dicts:
        dicts[key] = sorted(dicts[key])
    return dicts

dict_invert({1:10, 2:20, 3:30}) #returns {10: [1], 20: [2], 30: [3]}
dict_invert({1:10, 2:20, 3:30, 4:30}) #returns {10: [1], 20: [2], 30: [3, 4]}
dict_invert({4:True, 2:True, 0:True}) #returns {True: [0, 2, 4]}
dict_invert({8: 6, 2: 6, 4: 6, 6: 6}) #returns {6: [2, 4, 6, 8]}

def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    #YOUR CODE HERE
    length = len(L)-1
    def degree(x):
        total = 0
        for index, coefficient in enumerate(L):
            total = total + coefficient*x**(length-index)
        return total
    return degree

print general_poly([1, 2, 3, 4])(10)


def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    # Your code here
    if len(L1) == 0 and len(L2) == 0:
        return (None, None, None)
    if len(L1) != len(L2):
        return False
    dictL1 = dict()
    for element in L1:
        if element not in dictL1:
            dictL1[element] = 1
        else:
            dictL1[element] += 1
    dictL2 = dict()
    for element in L2:
        if element not in dictL2:
            dictL2[element] = 1
        else:
            dictL2[element] += 1
    if dictL1 != dictL2:
        return False

    max_key = max(dictL1, key=lambda k: dictL1[k])
    return (max_key, dictL1[max_key], type(max_key))

L1 = ['a', 'a', 'b']
L2 = ['a', 'b']
is_list_permutation(L1,L2)
L1 = [1, 'b', 1, 'c', 'c', 1]
L2 = ['c', 1, 'b', 1, 1, 'c']
is_list_permutation(L1,L2)