

def get_full_binary(n):
    """ adds 0's to the beginning of the number so we have the full byte """
    n = str(n)
    if len(n) < 8:
        n = ("0" * (8 - len(n))) + n
    return n


# def full_binary_converter(n):
#    """ LONGER CODE converts full binary into a base 10 number """
#    n = str(n)
#    list_nums = [int(digit) for digit in n]
#    list_nums[0] = list_nums[0] * 128
#    list_nums[1] = list_nums[1] * 64
#    list_nums[2] = list_nums[2] * 32
#    list_nums[3] = list_nums[3] * 16
#    list_nums[4] = list_nums[4] * 8
#    list_nums[5] = list_nums[5] * 4
#    list_nums[6] = list_nums[6] * 2
#    list_nums[7] = list_nums[7] * 1
#    reg_number = sum(list_nums)
#    return reg_number

# print(full_binary_converter("00000101"))

def full_binary_converter(n):
   """ CONDENSED CODE converts full binary into a base 10 number """
   n = str(n)
   list_nums = [int(digit) for digit in n]
   for i in range(8):
       list_nums[i] = list_nums[i] * (2**(7 - i))
   reg_number = sum(list_nums)
   return reg_number


def all_binary_converter(n):
    """ coverts ANY binary number into a base 10 number using 2 functions"""
    n = str(n)
    if len(n) < 8: 
        binary_n = get_full_binary(n)
        return full_binary_converter(binary_n)
    else: 
        n = int(n)
        return full_binary_converter(n)

print(all_binary_converter(101))


        
    

