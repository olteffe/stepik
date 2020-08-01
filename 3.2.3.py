dict_base, list_out = {}, []
for i in range(int(input())):
    x = int(input())
    if x not in dict_base:
        dict_base.update({x:f(x)})
        list_out.append(int(dict_base[x]))
    else:
        list_out.append(int(dict_base[x]))
for i in list_out:
    print(i)






