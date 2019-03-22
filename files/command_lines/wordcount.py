from collections import Counter, OrderedDict
import operator


def read_file(filename):
    """Returns the contents of a text file as a single string, with newlines
    converted to spaces.
    """

    with open(filename, "r", encoding="utf-8") as input_file:
        # Read the entire file, replacing newlines with spaces
        text = input_file.read().replace('\n', ' ')
        return text

def word_count(text, characters_to_ignore=",.?", case_sensitive=False):
    """Returns an ordered dictionary containing the sorted count of words in
    a string, with the word as dictionary key.
    """

    # replace all ignored characters with spaces.
    # This assumes that punctuation delimits words.
    # Mid-word punctuation will not give the correct results.
    for c in characters_to_ignore:
        text = text.replace(c, " ")

    # Convert to lower-case if required
    if not case_sensitive:
        text = text.lower()

    # Calculate word frequencies with Counter
    word_frequencies = Counter(text.split())

    # Sort into descending order and store in an order-preserving OrderedDict
    return OrderedDict(
            sorted(word_frequencies.items(),
                key=operator.itemgetter(1),
                reverse=True))

def print_counts(counts, min_count=2):
    """Prints the word counts. Only words with a count greater than or equal to
    `min_count` are displayed.
    """
    for word, count in counts.items():
        if count >= 2:
            print("{0}: {1}".format(word, count))
