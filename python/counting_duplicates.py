dict_0 = {}
def counting_duplicates(str):
    count = 0
    total = 0
    str = str.lower()
    st = list(str)
    print(st)
    for letter in st: 
        for let in st:
            if let == letter:
                count += 1
        st.remove(letter)
        print(st)
        if count > 1:
            total += 1
        count = 0
    print(total)        


        


counting_duplicates('aAA11A123')    