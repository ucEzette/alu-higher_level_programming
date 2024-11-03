#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for i in range(list_length):
        try:
            # Attempt to get the i-th elements from both lists and divide
            num1 = my_list_1[i]
            num2 = my_list_2[i]
            result = num1 / num2  # Attempt division
        except TypeError:
            print("wrong type")  # Error if an element is not a number
            result = 0
        except ZeroDivisionError:
            print("division by 0")  # Error if dividing by zero
            result = 0
        except IndexError:
            print("out of range")  # Error if the index is beyond list length
            result = 0
        finally:
            result_list.append(result)  # Append result (either division or 0) to result_list
    return result_list  # Return the list of results
