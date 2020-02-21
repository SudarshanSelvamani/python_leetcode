def middle_character(sts):
    if s % 2 == 0:
        return sts[(int(len(sts)/2) - 1):int((len(sts)/2)+1)]
    else:
        return sts[(len(sts) // 2 )]   
middle_character(str(input()))
