def check_elements_before(lst):
    for index in range(len(lst)):
        print(index)
        if index > 0:  # Check if there are elements before the current index
            print(f"There are elements before index {index}.")
        else:
            print(f"No elements before index {index}.")

# Example usage
my_list = [1]
check_elements_before(my_list)
