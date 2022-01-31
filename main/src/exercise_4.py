from typing import List

# method should have the append(5) as a parameter
# or it's name should be changed
# it's also misleading
def give_me_list(list_var: List = [], appanded_value = 5) -> List:
    list_var.append(appanded_value)
    return list_var # name of returned variable should be changed

# working on list by value is dangerous because of possible duplicates in values
# also mutable approach is dangerous
def return_every_third_element_from_list(l: List[str]) -> List[str]:
    # """Takes a list and return every 3-rd element."""
    # for i, val in enumerate(l):
    # if (i % 3) != 0:
    # del l[l.index(val)]
    # return l
    return [val for i, val in enumerate(l) if (i+1) % 3 == 0]
