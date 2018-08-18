number_list = [3, 14, 15, 9, 50, 2, 7, 46, 28, 30, 100, 4, 7]

over30 = sorted(number for number in number_list if number > 30)
print over30
under40 = sorted((number**2 for number in number_list if number<40),
                 reverse=True)
print under40