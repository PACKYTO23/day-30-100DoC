# with open("a_file.txt") as file:  # File Not Found
#     file.read()

# a_dictionary = {"key": "value"}  # Key Error
# value = a_dictionary["non_existent_key"]

# fruit_list = ["Apple", "Banana", "Pear"]  # Index Error
# fruit = fruit_list[3]

# text = "abc"  # Type Error
# print(text + 5)

# try:  # File Not Found & Error Handlers
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something.")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error I made up.")

# height = float(input("Height: "))
# weight = int(input("Weight: "))

# if height > 3:
#     raise ValueError("Human height should not be over 3 meters.")

# bmi = weight / height ** 2
# print(bmi)

# fruits = eval(input())  # IndexError Handling


# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:  # ["Apple", "Pear", "Orange"]
#         print("Fruit pie.")
#     else:
#         print(fruit + " pie.")


# make_pie(4)


# facebook_posts = eval(input())  # KeyError Handling
# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3}
# ]
# total_likes = 0

# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post["Likes"]
#     except KeyError:
#         pass

# print(total_likes)
