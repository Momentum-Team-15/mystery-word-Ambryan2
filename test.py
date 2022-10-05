from cgi import test
import string

example = "How long, an an an how long it's must we sing this song? How long? test test test chocolate"
STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    # this lowercases letters in file
    file = file.lower()
    # this removes punctuation
    remove_punctuation = file.translate(str.maketrans('', '', string.punctuation))
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
    # print(result)
    word = list(result.keys()) 
    values = list(result.values())
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

print_word_freq(example)