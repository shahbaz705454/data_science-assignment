'1.'
# print("\n1. Write a Python program which accepts the user's first and last name and prints them in reverse order with a space between them.")
# first_name = input("First name: ")
# last_name = input("Last name: ")
# print(last_name,first_name)

'2.'
# print('\n2.  Write a Python program which accepts a sequence of comma-separated numbers from the user and generates a list and a tuple with those numbers.')
# user_data = input("Enter sequence of comma-separated numbers: ")
# user_data = user_data.split(', ')
# user_list = list(user_data)
# user_tuple = tuple(user_data)
# print('List : ',user_list)
# print('Tuple : ',user_tuple)






'3.'
# print('\n3. Write a Python program to display the first and last colours from the following list.')
# color_list = ["Red", "Green", "White", "Black"]
# print(color_list)
# print('First color :',color_list[1],'\n' 'Last color :',color_list[-1])







'5.'
# print('\n5. Write a Python program to print the calendar of a given month and year.')
# import calendar
# year = int(input("Input the year : "))
# month = int(input("Input the month : "))
# print(calendar.month(year, month))

'4.' 
# import builtins 
# print("\n4. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).")
''' print(abs(-34))
    print(abs.__doc__)   '''
# help(builtins.abs)

# print(builtins.abs(-34))


'6.'
# print('\n6. Write a Python program to calculate number of days between two dates.')
# from datetime import date

# ay_1 = input("Enter first date in (yyyy, m, d): ")
# ay_2 = input("Enter second date in (yyyy, m, d): ")

# ay_1_value = ay_1.split(', ')
# ay_2_value = ay_2.split(', ')
# ay_1_list = list(ay_1_value)
# ay_2_list = list(ay_2_value)

# for ate in range(0, len(ay_1_list)):
    # ay_1_list[ate] = int(ay_1_list[ate])

# for ate in range(0, len(ay_2_list)):
    # ay_2_list[ate] = int(ay_2_list[ate])
    

''' y_1 = day_1_list[0]
    m_1 = day_1_list[1]
    d_1 = day_1_list[2] '''

'from datetime import date'
# day_1 = date(ay_1_list[0], ay_1_list[1], ay_1_list[2])
# day_2 = date(ay_2_list[0], ay_2_list[1], ay_2_list[2])

# day = day_2 - day_1

# print("The number of days are: ",day.days)

'7.'
# print('\n7. Write a Python program to check whether a specified value is contained in a group of values.')
# l = [1,5,8,3]
# value = int(input('Enter a value to check: '))
# if value in l:
    # print('True')
# else :
    # print('False')
# value = int(input('Enter a value to check: '))
# if value in l:
    # print('True')
# else :
    # print('False')

'8.'
# print('\n8. Write a Python program to create a histogram from a given list of integers.')
# l = input('List: ')
# l = l.split(',')
# list = list(l)
# for l in range(0,len(list)):
    # list[l] = int(list[l])

# print('_' * max(list) + '_______')
# for l in range(0,len(list)):
    # print('|'+'=' * list[l] + ']', list[l])
# print('|')

'9.'
# print('\n9. Write a Python program to concatenate all elements in a list into a string and return it.')
# list_u = list(input('List: ').split(','))
# for l in range(0,len(list_u)):
#     list_u[l] = str(list_u[l])

# print('List in string: ',list_u)

'10.'
# print('\n10. Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.')

# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])

# print('color_list_1: ',color_list_1,'\n' 'color_list_2: ',color_list_2)
# print("\nDifferenct of color_list_1 and color_list_2:")
# print('By color_list_1.difference(color_list_2)',color_list_1.difference(color_list_2))

# print("\nDifferenct of color_list_1 and color_list_2:")
# print('By color_list_1 - color_list_2',color_list_1 - color_list_2)

'11.'
# print('\n11. Write a Python program to check whether a file exists.')
# import os.path
# file_path = input('File path: ')
# file_exists = os.path.exists(file_path)

# print(file_exists)

'12.'
# print('\n12. Write a python program to call an external command in Python.')
# import os
# commond = input('Write your external commond: ')
# print(os.system(commond))

'13.'
# print('\n13. Write a Python program to find out the number of CPUs using.')
# import multiprocessing
# print('import multiprocessing \nprint(multiprocessing.cpu_count()):', multiprocessing.cpu_count())

'14.'
# print('\n14. Write a Python program to list all files in a directory in Python.')
# from os import listdir
# print("from os import listdir \nprint (listdir('File path name'))")
# print (listdir('E:\Shubham\Desktop\AI-ML\Coffeee Data Science Bootcamp - 0001'))

'15.'
# print('\n15. Write a python program to access environment variables.')
# import os
# for data in os.environ:
#    print(data)
#    print('-'*10)
#    print(os.environ[data])
#    print('='*20+'>')

'16.'
# print('16. Write a Python program to get the current username')
# print('''import os
# print(os.environ.get('USERNAME'))''')
# import os
# print(os.environ.get('USERNAME'))

'17.'
# print('\n17. Write a program to get execution time for a Python method.')
# import time
# start_time = time.time()
# t = 0
# for i in range(1,10):
    # t = t + i
    # print(t)
# end_time = time.time()

# print('Exicution time:{:.5f}'.format(end_time-start_time) )
# print('Exicution time:',end_time-start_time, 'seconds')

'18.'
# print('\n18. Write a Python program to get an absolute file path.')
# print('''import os
# absolute_file_path = os.path.abspath('.gitattributes')        
# print("Absolute file path: ",absolute_file_path)''')
# import os
# absolute_file_path = os.path.abspath('.gitattributes')        
# print("Absolute file path: ",absolute_file_path)

'19.'
# print('\n19. Write a Python program to get file creation and modification date/times.')
# import os.path, time
# file_name = '.gitattributes'
# print("File name:", file_name)
# print("Last modified:", time.ctime(os.path.getmtime(file_name)))
# print("Created:", time.ctime(os.path.getctime(file_name)))

'20.'
# print('\n20. Write a Python program to sort three integers without using conditional statements and loops.')
# int_list = input('Enter 3 integers(n,n,n): ')
# int_list = int_list.split(',')
# for l in range(0,len(int_list)):
    # int_list[l] = int(int_list[l])
# int_list.sort()
# print('Sorted list:',int_list)

'21.'


'22.'
# print('\n22. Write a Python program to get the command-line arguments (name of the script, the number of arguments, arguments) passed to a script.')
# import sys
# print("This is the name/path of the script:"),sys.argv[0]
# print("Number of arguments:",len(sys.argv))
# print("Argument List:",str(sys.argv))

'23.'
# print('\n23. Write a Python program to find the available built-in modules.')
# import sys
# module_name = ', '.join(sys.builtin_module_names)
# print(module_name)

'24.'
# print('\n24. Write a Python program to get the size of an object in bytes.')
# import sys
# obj = 7
# size = sys.getsizeof(obj)
# print('object: ', obj)
# print('Size of the object is:', size)

'25.'
# print('\n25. Write a Python program to get the current value of the recursion limit.')
# import sys
# print("Current value of the recursion limit:", sys.getrecursionlimit())

'26.'
# print('\n26. Write a Python program to count the number occurrence of a specific character in a string.')
# string = "Write a Python program to count the number occurrence of a specific character in a string."
# print("String:", string)
# char = input('Enter the character to count the number occurrence of it in the given above string: ')
# print(f"The number of '{char}' in the above string is:",string.count(char))

'27.'
# print('\n27. Write a Python program to get the system time.')
# import datetime
# print("The systen time is:", datetime.datetime.now().time())

'28.'
# print('\n28. Write a Python program to clear the screen or terminal.')
# import os
"os.system('cls')"
# print('''import os
# os.system('cls')''')

'29.'
# print('\n29. Write a Python program to get the name of the host on which the routine is running.')
# print('''import socket
# host_name = socket.gethostname()
# print("Host name:", host_name)''')
# import socket
# host_name = socket.gethostname()
# print("Host name:", host_name)

'30.'
# print("\n30. Write a Python program to access and print a URL's content to the console.")
# import requests
# data = requests.get('https://example.com')
# print(data.text)
