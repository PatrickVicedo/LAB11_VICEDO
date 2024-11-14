words = []
for i in range(10):
    word = input(f"Enter word {i + 1}: ")
    words.append(word)

while True:
    user_input = input("Enter the word length you want to search for in the list: ")
    if user_input.isdigit():
        user_input = int(user_input)
        break
    else:
        print("Invalid input. Please enter a numeric value.")

matching_words = []
for word in words:
    if len(word) == user_input:
        matching_words.append(word)

if len(matching_words) > 0:
    print("Words with the specified length:")
    for word in matching_words:
        print(word)
else:
    print(f"There are no words with {user_input} characters.")