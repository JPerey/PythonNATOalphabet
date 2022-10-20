import pandas


#TODO 1. Create a dictionary in this format:


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

alphabet_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {}
done = False


while not done:
    player_word = input("Please enter a word turn phonetic: ").upper()
    player_word_split = [letter for letter in player_word]
    player_word_length = len(player_word_split)
    phonetic_word = []
    i = 0
    print(player_word_split)

    for player_letter in player_word_split:
        for (index, row) in alphabet_dataframe.iterrows():
            if player_letter == row.letter:
                phonetic_word.append(row.code)
                if i < player_word_length:
                    i += 1

    print(phonetic_word)

    player_choice = input("would you like to try another word? yes or no: ").lower()

    if player_choice == "no":
        done = True




