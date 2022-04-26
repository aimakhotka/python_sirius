def insta(names):
    count_names = len(names)
    if count_names < 1:
        return None 
    elif count_names == 1:
        return '%s likes it'%(names[0])
    elif count_names == 2:
        return '%s and %s likes it'%(names[0], names[1])
    elif count_names == 3:
        return '%s, %s and %s likes it'%(names[0], names[1], names[2])
    else:
        return '%s and %d people likes it'%(names[0], count_names - 1)