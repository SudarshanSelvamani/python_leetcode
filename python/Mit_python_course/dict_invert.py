def dict_invert(d):    
    inverse = {}
    for elm in d.keys():
        if d[elm] in inverse:
            inverse[d[elm]].append(elm)
            print('lopo',inverse)
        else:
            inverse[d[elm]] = [elm]
            print('lopy',inverse)
    for val in inverse.values():
        val.sort()
    return inverse
print(dict_invert({1:10, 2:20, 3:30, 4:30}))    
