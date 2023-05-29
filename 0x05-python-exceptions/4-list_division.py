def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    result = 0
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
            new_list.append(result)
        except (ZeroDivisionError, TypeError, IndexError) as err:
            print(err)
            new_list.append(0)
        finally:
            pass
    return new_list
