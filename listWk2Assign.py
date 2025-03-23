my_list = []  # Creating the list

my_list.append(10)  # Appending
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list.insert(1, 15)  # Inserting

my_list.extend([50, 60, 70])  # Extending

my_list.pop()  # Removing

my_list.sort()  # Sorting

index_of_30 = my_list.index(30)  # Finding index

print(f"Index of 30: {index_of_30}")
print("Final List:", my_list)
