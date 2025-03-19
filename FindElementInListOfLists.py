TableList = ['tableA','tableB','tableG']
A = [['abc',['tableA'],['colmn1','column2']], ['cde',['tableD'],['colmn3','column4']], ['def',['tableG'],['colmn7','column8']]]

# Check for the presence of 'tableA'
# table_present = any(TableList in sublist[1] for sublist in A if isinstance(sublist[1], list))
# # table_present = any(table in sublist[1] for sublist in A if isinstance(sublist[1], list))
# print(table_present)



# for i in range(0,len(TableList)):
#     if (any(TableList[i] in sublist[1] for sublist in A if isinstance(sublist[1], list))):
#         print(TableList[i], "Present")
#     else:
#         print(TableList[i],"Not Present")

# print(table_present)

# List of numbers
numbers = [-5, -3, 5, -2, -1]

# Check if any number in the list is positive
item = numbers[0]
has_positive = any(item > 0 for num in numbers)

# Print the result
if has_positive:
    print("There is at least one positive number.")
else:
    print("There are no positive numbers.")



