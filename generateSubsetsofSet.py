def generate_all_subsets(s):
    res = ['']
    for i in s:
        res += [c+i for c in res]
    return res
        
