import random

def wordle():
    categories = { #just change this I can't think of stuff
        "Food": ["Salad"], #I added one just for testing purposes
        "English": [],
        "Fruits": []
    }
    
    for keys in categories.keys(): #this just loops the dictionary so that all the keys are printed
        print(keys)

    while True:
        user_input = input("What category would you like to try?\n(type Exit to exit)\n").strip()
        user_input = ''.join(user_input.split()).lower().capitalize()
                     # we can make it choose numbers instead
                     # strip removes any whitespaces, only before and after tho
                     #" ".join just joins the words back into a single string without any spaces.
                     #.lower is to lower all the characters and capitalize capitalizes only the 1st character
                     # I did this so that the code won't break unless integers and stuff were inputted, tho a fix for that can be added too
        print("User input:", user_input)
        print("Categories:", categories.keys())
        
        if user_input in categories:
            randomizer = random.choice(categories[user_input]) #randomizes the list of the chosen category
            print("\nYou have chosen the category:", user_input)
            print("\nStarting...")
            print("\nYou have 5 attempts to guess the word for this category. Good luck!") #just make these 3 lined more user-friendly
            break #breaks out
        elif user_input == "Exit": #well I thought it's a nice addition, remove if you want
            exit()
        elif user_input not in categories: #if the user inputted anything not in the category this runs and repeats back to user_input until the if one runs
            print("Hmm, I couldn't find that category...\nDouble-check your typing and try again!\n")  

    attempts = 5
    while attempts != 0:
        guess = input("Enter your guess = ").lower().capitalize() #only these two for now, you can add more like the user_input if you want
        
        if len(guess) != 5: #counts the length of the inputted gues and if not 5 then
            print("You need to input a 5 letter word")
            continue #continue is needed so that the loop will restart and not check the conditions below

        if attempts == 0:
            print("You have failed to guess the word")
            print(f"The correct word was {randomizer}")
            try_again = input("Do you wanna try again? (Y/N) = ").strip().lower() #asks if the user wanna do it again
            if try_again == "Y": #if yes then this just runs the code again
                wordle()
            elif try_again == "N": #if not then exits the code
                exit()

        feedback = "" #an empty string to store the feedbacks
        for i in range(5): #checks each letter of the inputted guess to see if it matches the word
            if guess[i] == randomizer[i]: #if the letter is in correct position
                feedback += f"[{guess[i]}]"  #adds [] for every letter in a correct position
            elif guess[i] in randomizer: #if the letter is correct but in wrong position
                feedback += f"({guess[i]})" #this adds a () if the word is correct but in wrong position
            else: #if the letter is incorrect
                feedback += f" {guess[i]} " #just normal

        if guess != randomizer: # if wrongly guessed. this is placed after feedback because there will be no response if not
            attempts -= 1
            print(feedback)
            print(f"You have {attempts} attempts left!")
        
        if guess == randomizer: # if guessed correctly then
            print(feedback)
            print("You have correctly guessed the word!\nCongratulations!") #change this to a better one lol
            try_again = input("Do you wanna try again? (Y/N) = ").strip().lower() #asks if the user wanna do it again
            if try_again == "Y": #if yes then this just runs the code again
                wordle()
            elif try_again == "N": #if not then exits the code
                exit()
            break 

wordle()

        