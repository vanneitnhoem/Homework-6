
#Exercise 1
replace_last = [1,2,3,4,5]
if replace_last == []:
    print(replace_last)
else:
    replace_last.insert(0, replace_last[-1])
    replace_last = replace_last[:-1]
    # del replace_last[-1]

    print(replace_last)