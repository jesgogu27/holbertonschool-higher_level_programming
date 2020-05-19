#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for x in range(list_length):
        try:
            res = my_list_1[x] / my_list_2[x]
        except (TypeError, ValueError):
            res = 0
            print("wrong type")
        except ZeroDivisionError:
            res = 0
            print("division by 0")
        except IndexError:
            res = 0
            print("out of range")
        finally:
            result.append(res)
    return result
