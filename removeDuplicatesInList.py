def remove_duplicates(lst):
    nlst = []
    for l in lst:
        if l not in nlst:
            nlst.append(l)
        
    return nlst