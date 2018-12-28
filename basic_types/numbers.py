sum_of_5_and_6 = 5 + 6
print(sum_of_5_and_6)
print(type(sum_of_5_and_6))

concat_5_and_6 = '5' + '6'
print(concat_5_and_6)
print(type(concat_5_and_6))

sum_type_cast = int('5') + int('6')
print(sum_type_cast)
print(type(sum_type_cast))

sum_float_numbers = 3.1 + 3.2
print(sum_float_numbers)
print(type(sum_float_numbers))

# this raise a error : ValueError
#int('Hello')

cast_down = int(sum_float_numbers)
print(cast_down)
print(type(cast_down))