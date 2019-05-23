def insert_sort(list_of_numbers):
    """
    Takes in an unsorted list of numbers
    returns a sorted list (small to big) (using insertion method)
    hint: use wishful thinking
    """
    l = []
    for i in list_of_numbers:
        l=insert_num(l,i)
    return l

def insert_num(l, num):
    """
    takes in a sorted_list and a num
    and inserts the num into the correct position in the sorted_list.
    """
    hl = []
    for i in l.copy():
        if i < num:
            hl.append(l.pop(0))
    hl.append(num)
    for i in l:
        hl.append(i)
    return hl




# from random import sample
# mylist = sample(range(100), 10)
# mylistcheck = mylist.copy()
# mylistcheck.sort(reverse=True)
# print(mylist)
#
# print("=== BEGIN INSERTION ===")
# print("Ans:", insert_sort(mylist))
# print("=== END INSERTION ===")
#
# print(mylistcheck)

print(insert_num([0,1,3,4,5,6], 2))
print(insert_num([1,2,3,4,5,6,8,9], 7))
# print(insert_num([1,2,3,4,5,6,8,9], 7) == [1,2,3,4,5,6,7,8,9])
