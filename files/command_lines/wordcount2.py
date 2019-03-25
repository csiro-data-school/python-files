import Argparse     # Required to use the argparse module
from wordcount import read_file, word_count, print_counts


def get_program_args():
    """Defines command-line arguments and returns them to caller."""

    # Create an argument parser
    parser = argparse.ArgumentParser()

    # Define the input file name argument
    parser.add_argument(
            help="The input text file")

    # Define the optional punctuation argument
    parser.add_argument(
            "-p",
            "--punctuation",
            default=",.?",      # Default value to use when argument is not supplied
            required=True,
            help="Punctuation to ignore when counting words.")

    # Optional boolean argument indicating whether to ignore word case
    # When the "store_true" action is given, argparse stores True in the
    # argument variable if the argument is present, and False otherwise.
    parser.add_argument(
            "-c",
            "--case-sensitive",
            action="store_true",  # This action tells argparse to store True when the flag is specified.
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
            default=2,
            help="The minimum word count threshold for display.")

    # parse_args first checks for errors, and if there are none, it returns
    # a Namespace object containing your named arguments. argument names
    # correspond to the long-form argument names.
    return parser.parse_args()


if __name__ == "__main__":

    counts = word_count(
            read_file(args.file),
            characters_to_ignore=args.punctuation,
            case_sensitive=args.case-sensitive)

    print_counts(counts, min_count=args.min_count)
