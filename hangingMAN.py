'''
# 0
print("_________")
print("|       |")
print("|")
print("|")
print("|")
print("|")
print("|")
#1
print("_________")
print("|       |")
print("|       0")
print("|           ")
print("|")
print("|")
print("|")
#2
print("_________")
print("|       |")
print("|       0")
print("|       |   ")
print("|")
print("|")
print("|")
#3
print("_________")
print("|       |")
print("|       0")
print("|       | \ ")
print("|")
print("|")
print("|")
#4
print("_________")
print("|       |")
print("|       0")
print("|     / | \ ")
print("|")
print("|")
print("|")
#5
print("_________")
print("|       |")
print("|       0")
print("|     / | \ ")
print("|        \ ")
print("|")
print("|")
#6 game over!!
print("_________")
print("|       |")
print("|       0")
print("|     / | \ ")
print("|      / \ ")
print("|")
print("|")

'''



print("Welcome to the hanging man game")
#asking the user to choose a subject
print("In this game there are a few options of subjects you can choose from. press the number you want:")
print("for animal press 1")
print("for food press 2 ")
print("for Languages press 3 ")
choice_subject = int(input("your choice is: "))
choice_word = int(input("choose a number between 0-2: "))

# preparing the list of word
word_list_animal = ["lion", "bird", "pig"]
word_list_food = ["cheese", "cake", "apple"]
word_list_Languages = ["hebrew", "spanish", "english"]

#starting the game!!
#printing the hanging man
print("_________")
print("|       |")
print("|")
print("|")
print("|")
print("|")
print("|")
print()
print()
# to know when to move to the next letter in the word
right_letter = 0
# defining the variable letter
letter = ""
# to know when the game is over and the user loses
bad_points = 0

# checking what the user chose
if choice_subject == 1:
    word = word_list_animal[choice_word]
elif choice_subject == 2:
    word = word_list_food[choice_word]
else:
    word = word_list_Languages[choice_word]
guess = []
for i in range(len(word)):
        print("_", end=' ')
        guess.append('_')
word_completed = 0#indicates if the word completed if the nuber equals to the word length
right_letter = 0 #indicates how many letters were guessed correctly
already_chosen_letter = 0 #indicates if a correct letter was chosen more then once
while word_completed < len(word): #as long as the word wasn't completed
    right_letter = 0
    letter = input("\n press a letter: ") #asking the user to choose a letter
    for i in range(len(word)):
        if letter == guess[i]:
            print("You  have already chose this letter and you were correct. Now Please choose a different letter ")
            already_chosen_letter = 1
            break
        if letter == word[i]:
            guess[i] = letter #if it is correct we save it to the guess user list
            word_completed += 1 #changing the flag to know the answer was correct and we can move on to the next guess
            right_letter = 1
    for i in range(len(word)):
        print(guess[i], end=' ') #the end is to make sure the line won't drop  every time we perform the print
    if already_chosen_letter == 1:
        already_chosen_letter = 0
        continue
    if right_letter == 0:
        print("Wrong letter try again!")
        bad_points += 1
    if bad_points == 0:
        pass
    elif bad_points == 1:
        print("\n_________")
        print("|       |")
        print("|       0")
        print("|           ")
        print("|")
        print("|")
        print("|")
    elif bad_points == 2:
        print("\n_________")
        print("|       |")
        print("|       0")
        print("|       |   ")
        print("|")
        print("|")
        print("|")
    elif bad_points == 3:
        print("\n_________")
        print("|       |")
        print("|       0")
        print("|       | \ ")
        print("|")
        print("|")
        print("|")
    elif bad_points == 4:
        print("\n_________")
        print("|       |")
        print("|       0")
        print("|     / | \ ")
        print("|")
        print("|")
        print("|")
    elif bad_points == 5:
        print("\n_________")
        print("|       |")
        print("|       0")
        print("|     / | \ ")
        print("|        \ ")
        print("|")
        print("|")
    else:
        print("\nGAME OVER!!!")
        print("_________")
        print("|       |")
        print("|       0")
        print("|     / | \ ")
        print("|      / \ ")
        print("|")
        print("|")
        print("you lost!!")
        print("the word was: ", end='')
        print("GAME IS OVER!!!!")
        for m in range(len(word)):
            print(word[m], end='')
    if bad_points > 5:
        break
    if '_' in guess:
        print()
    else:
        print("\n You won!!!!")
        break
