# Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

# You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

 

# Example 1:

# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
# Output: ["Shogun"]
# Explanation: The only restaurant they both like is "Shogun".
# Example 2:

# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
# Output: ["Shogun"]
# Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).

def rest(list1, list2):

    shared = []
    dict_r_i = {}
    output = []

    for a in list1:
        for d in list2:
            if a == d:
                shared.append(a)
                list1.index(a)
                dict_r_i[a] = list1.index(a) + list2.index(a)
                print(dict_r_i)
            else:
                continue     
    x = dict_r_i.values()
    l_v = min(x)
    for  k , v in dict_r_i.items():
        if v == l_v:
            output.append(k)

    return output

print(rest(["Shogun","KFC","Burger King"], ["KFC","Shogun","Burger King"]))