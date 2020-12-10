import random
import aciiarts
import hangman_words


word_list=hangman_words.word_list

print(aciiarts.logo)

hangman_word = random.choice(word_list)
list(hangman_word)
display=[]
for i in range(1,len(hangman_word)+1):
    display+="_"

end_of_game=False

lives=6
while not end_of_game:
    user_input=input("Guess a letter: ").lower()

    #displaydaki "_"ile girilen harfin yer değiştirmesi
    for position in range(len(hangman_word)):
        letter=hangman_word[position]
        if letter==user_input:
            display[position]=letter

    if user_input not in hangman_word:
        lives-=1
        if lives==0:
            print("you lose")
            end_of_game=True
    print(aciiarts.stages[lives])
    if "_" not in display:
        end_of_game=True
        print("you won")

    print(display)



