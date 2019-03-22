from collections import Counter, OrderedDict
import operator

# Required to use the argparse module
import argparse

def read_file(filename):
    """Returns the contents of a text file as a single string, with newlines
    converted to spaces.
    """

    with open(filename, "r", encoding="utf-8") as input_file:
        # Read the entire file, replacing newlines with spaces
        text = input_file.read().replace('\n', ' ')
        return text

def word_count(text, characters_to_ignore=",.?", case_sensitive=False):
    """Returns the sorted count of words in a string"""

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


def get_program_args():
    """Defines command-line arguments and returns them to caller."""

    # Create an argument parser
    parser = argparse.ArgumentParser()

    # Define the input file name argument
    parser.add_argument(
            "-f",           # short-form argument
            "--file",       # long-form argument
            required=True,  # This argument is required
            help="The input text file")

    # Define the optional punctuation argument
    parser.add_argument(
            "-p",
            "--punctuation",
            default=",.?",      # Default value to use when argument is not supplied
            required=False,
            help="Punctuation to ignore when counting words.")

    # Optional boolean argument indicating whether to ignore word case
    # When the "store_true" action is given, argparse stores True in the
    # argument variable if the argument is present, and False otherwise.
    parser.add_argument(
            "-c",
            "--case-sensitive",
            required=False,
            action="store_true",
            help="Force a case-sensitive count. By default, case is ignored.")

    # Optional integer argument indicating the minimum word count threshold for
    # display.
    # The new feature here is the type argument. By default, argparse treats
    # everything as a string. If you want arguments to be other types, you need
    # to tell argparse which type you require.
    # This has several benefits:
    # - argparse will do error handling for you.
    # - the value will already be the correct type in the arguments object.
    # - it helps make your code self-documenting.
    parser.add_argument(
            "-m",
            "--min-count",
            required=False,
            type=int,
            default=1,
            help="The minimum word count threshold for display.")

    # parse_args first checks for errors, and if there are none, it returns
    # a Namespace object containing your named arguments. argument names
    # correspond to the long-form argument names.
    return parser.parse_args()


if __name__ == "__main__":

    # Initialise the argument parser
    args = get_program_args()

    # Now that we have our arguments, we can just use them :)
    counts = word_count(
            read_file(args.file),
            characters_to_ignore=args.punctuation,
            # Small gotcha here. The argument was called "case-sensitive" which
            # is not a valid identifier. Argparse knows this and replaces "-"
            # with "_".
            case_sensitive=args.case_sensitive)

    for word, count in counts.items():
        if count >= args.min_count:
            print("{0}: {1}".format(word, count))
