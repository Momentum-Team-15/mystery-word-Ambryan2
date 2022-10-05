import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    with open(file, 'r') as f:
        file_string = f.read()
            # this lowercases letters in file
        text = file_string.lower()
        # this removes punctuation
        remove_punctuation = text.translate(str.maketrans('', '', string.punctuation))
        # this makes every word its own item in array
        string_file = remove_punctuation.split()
        result = {}
        for item in string_file:
            # amount = 0
            amount = string_file.count(item) 
            # this if removes any words that match the stop words
            if item not in STOP_WORDS:
                # this if adds new key in result dictionary with amount as the number of times word appears
                if item not in result:
                    result[item] = amount
        # Puts everything in descending order note it is now an array
        result = sorted(result.items(), key=lambda seq: seq[1], reverse=True)
        # this separates word from number and puts them in separate strings
        word = []
        values = []
        for content in result:
            word.append(content[0])
            values.append(content[1])
        # this looks for longest word
        longest_word = 0
        for word_length in word:
            if longest_word<len(word_length):
                longest_word = len(word_length)
        # this checks the length of word string and then adds spaces so the length of all of them is the same
        final_display_word = []
        for same_length in word:
            spaces = ' '
            if len(same_length) != longest_word:
                difference = longest_word - len(same_length)
                final_display_word.append((spaces * difference) + same_length)
                difference = 0
            else: 
                final_display_word.append(same_length)
        # everything below creates the display in the terminal
        count = 0
        for number in range(len(final_display_word)):
            stars = "*" * values[count]
            print( f"{final_display_word[count]}  |  {values[count]}  {stars}")
            count +=1

print_word_freq('praise_song_for_the_day.txt')

# if __name__ == "__main__":
#     import argparse
#     from pathlib import Path

#     parser = argparse.ArgumentParser(
#         description='Get the word frequency in a text file.')
#     parser.add_argument('file', help='file to read')
#     args = parser.parse_args()

#     file = Path(args.file)
#     if file.is_file():
#         print_word_freq(file)
#     else:
#         print(f"{file} does not exist!")
#         exit(1)
