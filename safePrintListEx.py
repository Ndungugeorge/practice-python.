"""def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        for j in my_list:
            if i >= x:
                break
            print(j,end=" ")
            i+=1
        print()
        return i
    except:
        return 0

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))"""
def safe_print_list(my_list=[], x=0):
    
        i = 0
        for k in range(x):
            try:
                print("{}[{}]".format(my_list[i]))
                i+=1
            except IndexError:
                    break
        print("")
        return i