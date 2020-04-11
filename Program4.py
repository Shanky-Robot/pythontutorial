# lists

example_lists_1 = [5, 4, 3, 2, 1]
example_list_2 = ["Yolo", "LMFAO", "ROFL", "LOL"]
print(example_lists_1)
print(list(example_list_2))
print(list(example_lists_1))
print(list("Blah"))

# in or not in operators

check_list = [1, 2, 3, 4]
print(1 in check_list)
print(8 in check_list)

not_in_example = 8 not in check_list
print(not_in_example)

# indexes and slicing
# indexing

index_example = ["carpet", "yolo", "dayum"]
print(index_example[1])
print(example_lists_1[2])
index_example_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(index_example_2[2][0])
print(index_example[2][0])

#negaive index

neg = [1, 2, 3, 4, 5]
print(neg[-1])
print(neg[-2])
print(neg[-3])
print(neg[-4])
print(neg[-5])

# index in expressions
mix= [False, 365, 4.24, "lol this is fun"]
print(mix[2] + 1.24)
print("I have \"" + mix[-1] + "\" as an example")

# list slicing

print(neg[:4])
print(neg[0:2])
print(neg[3:])

# reassigning a list's items

print(neg)
neg[3] = 10
print(neg)
neg[1:4] = [7, 8, 21]
print(neg)
neg[1:7] = [21, 5, 71, 23, 2]  # assigning new index values in list
print(neg)

# del ands list methods - only for list datatypes only

del example_list_2[0]
print(example_list_2)

# .remove()

example_list_2.remove("LOL")
print(example_list_2)

# append()
example_list_2.append("OMG")
print(example_list_2)

# .insert()
example_list_2.insert(1, "SMH")
print(example_list_2)

# sorting
neg.sort()
print(neg)

example_list_2.sort()
print(example_list_2)

# reverse=TRUE

example_list_2.sort(reverse=True)
print(example_list_2)
neg.sort(reverse=True)
print(neg)

# sort cannot be used on mixed data types
# boolean values is treated as 1 or 0 so sort can be done on bool and int

new = [False, -32, 532]
new.sort()
print(new)

#ASCIIbetical order

Word = ["Sand", "rand", "mand", "Dand"]
Word.sort()
print(Word)
Word.sort(key=str.lower)
print(Word)

# .index() index no. in passing
print(Word.index("Sand"))

# .pop() adds or removes items

end = Word.pop()
bend = Word.pop(1)
print(end)
print(Word)
bend = Word.pop(1)
print(bend)






