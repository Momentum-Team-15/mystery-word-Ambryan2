import string


example = "How long, how long it's must we sing this song? How long? test test test"

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    file = file.lower()
    remove_punctuation = file.translate(str.maketrans('', '', string.punctuation))
    string_file = remove_punctuation.split()
    result = {}
    for item in string_file:
        amount = 0
        amount = string_file.count(item) 
        if item not in result:
            result[item] = amount
    print(result)
    # Need to remove keys and values from words that I do not want to count 
    word = list(result.keys()) 
    values = list(result.values())
    # need to use list to create a display like the one in the directions
    print(values)

print_word_freq(example)