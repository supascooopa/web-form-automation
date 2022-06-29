import os
import random
from timeit import default_timer


# computer_choice = random.randint(0, 9)
# print(computer_choice)
# flag = True
# while flag:
#     choice = int(input("please enter a number: "))
#     if choice == computer_choice:
#         print("you win!")
#         flag = False

# list_of_pokemon = [file for file in os.listdir() if file.endswith(".jpg")]
# path_to_pokemon = [os.getcwd()+"\\"+file+" " for file in list_of_pokemon]
# # path_to_pokemon.append(os.getcwd()+"\\"+list_of_pokemon[len(list_of_pokemon)-1])
# combine = "\n".join(path_to_pokemon)
# print(repr(combine))
# for pokemon in os.listdir("CE"):
#     print(pokemon)
# print(os.path.abspath("CE"))
# print(os.listdir("XL")[0])
# pdf_file = os.listdir("invoice")[0]
# print(pdf_file)
# print(os.path.abspath("invoice") + "\\CI -Total 20210913.pdf")
#
#
# starting_time = default_timer()
# ending_time = default_timer()
# time_taken = str(ending_time - starting_time)
# with open("time taken.txt", "w") as timer_file:
#     timer_file.write(time_taken)
#
# a_dict= {}
# a_dict["a"] = 10
# a_dict["f"] = 20
# a_dict["d"] = 30
# sorted_dictino = sorted(a_dict.items(), key=lambda k: k[0])
# print(a_dict)
# print(sorted_dictino)
n = 3
s = ""
for i in range(1,n +1):
    s += str(i)
print(s)

