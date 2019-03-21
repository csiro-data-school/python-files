from collections import Counter, OrderedDict
import operator
import sys

def read_file(filename):
    """Returns the contents of a text file as a single string, with newlines
    converted to spaces.
    """

    with open(filename, "r", encoding="utf-8") as input_file:
        # Read the entire file, replacing newlines with spaces
        text = input_file.read().replace('\n', ' ')
        return text

def word_count(text, characters_to_ignore=",.?", ignore_case=True):
    """Returns the sorted count of words in a string"""

    # replace all ignored characters with spaces.
    # This assumes that punctuation delimits words.
    # Mid-word punctuation will not give the correct results.
    for c in characters_to_ignore:
        text = text.replace(c, " ")

    # Convert to lower-case if required
    if ignore_case:
        text = text.lower()

    # Calculate word frequencies with Counter
    word_frequencies = Counter(text.split())

    # Sort into descending order and store in an order-preserving OrderedDict
    return OrderedDict(
            sorted(word_frequencies.items(),
                key=operator.itemgetter(1),
                reverse=True))


if __name__ == "__main__":

    # If we have less than two arguments, print the usage message and exit
    if len(sys.argv) < 2:
        print("{0} usage: {0} input_file <'punctuation to ignore'>".format(
            sys.argv[0]))
        exit()

    # First argument (and second in argv) is the input file.
    input_file = sys.argv[1]

    # Second argument (if it exists) is the punctuation to ignore.  Since it is
    # optional, we use the Python ternary operator to assign a default value if
    # the argument was not supplied
    characters_to_ignore = sys.argv[2] if len(sys.argv) > 2 else ",.?"

    counts = word_count(
            read_file(input_file),
            characters_to_ignore=characters_to_ignore)

    for word, count in counts.items():
        print("{0}: {1}".format(word, count))
