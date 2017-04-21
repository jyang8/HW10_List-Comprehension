# returns list of uppercase letters
def getUpper(s):
    l = [x for x in s]
    return [x for x in l if x.isupper()]

# returns list of lowercase letters
def getLower(s):
    l = [x for x in s]
    return [x for x in l if x.islower()]

# returns list of numbers
def getNums(s):
    l = [x for x in s]
    return [x for x in l if x.isdigit()]

# returns list of non-alphanumeric chars
def getNon(s):
    l = [x for x in s]
    upper = getUpper(s)
    lower = getLower(s)
    nums = getNums(s)
    return [x for x in l if not (x in upper or x in lower or x in nums)]

# if password has at least 1 uppercase, 1 lowercase, and 1 num, return true
# else return false
def check(pw):
    upper = getUpper(pw)
    lower = getLower(pw)
    nums = getNums(pw)
    return len(upper) > 0 and len(lower) > 0 and len(nums) > 0
'''
# returns password strength rating from scale of 1-10
def strength(pw):
    if not check(pw):
        return 1
    l = [x for x in pw]
    numUpper = len(getUpper(pw)) 
    numLower = len(getLower(pw)) 
    numNums = len(getNums(pw)) 
    numNon = len(getNon(pw))
    tLen = numUpper + numLower + numNums + numNon
    scale = 0
    if tLen > 3:
        scale = (2 * numUpper + numLower + 2 * numNums +  5 * numNon)/5
    rating = tLen/2 + scale
    if rating > 10:
        return 10
    return rating
'''
