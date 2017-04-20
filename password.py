# upper- and lowercase letters, and at least one number
def check(pw):
    l = [x for x in pw] #l = list(pw)
    upper = [x for x in l if x.isupper()]
    lower = [x for x in l if x.islower()]
    nums = [x for x in l if x.isdigit()]
    return len(upper) > 0 and len(lower) > 0 and len(nums) > 0
