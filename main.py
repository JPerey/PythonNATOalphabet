import pandas

# TODO 1. Create a dictionary in this format:


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

alphabet_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter: row.code for (index, row) in alphabet_dataframe.iterrows()}
done = False

while not done:
    player_word = input("Please enter a word turn phonetic: ").upper()
    player_word_split = [letter for letter in player_word]
    try:
        phonetic_word = [alphabet_dict[letter] for letter in player_word_split]
    except KeyError as e:
        print(f"{player_word} contains values that are not letters. Please only use letters.")
        player_choice = input("would you like to enter a correct word? yes or no: ").lower()
    else:
        print(phonetic_word)
        player_choice = input("would you like to try another word? yes or no: ").lower()

    if player_choice == "no":
        done = True
