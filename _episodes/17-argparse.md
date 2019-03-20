---
title: "Getting arguments from the command-line"
teaching: 0
exercises: 0
questions:
- "Key question (FIXME)"
objectives:
- "First learning objective. (FIXME)"
keypoints:
- "Using command-line arguments can make your programs easier to use and reuse."
---

**TODO**
- sys.argv
- argparse
    - define args
    - arg types
    - optional args, default values
    - help strings
    - filters and constraints (eg: files must exist)
- click

## Why Bother with Command-line Arguments?

### They can make your programs easier to use

Have you ever written a short program, and then gone to reuse it a few months
later, only to find that you can't remember exactly how to make it work? While
good comments and docstrings clearly help, command-line arguments can also help.
The recommended approaches for implementing command-line arguments in Python all
support the creation of command-line help messages with very little extra
effort.

### They can make your programs easier to reuse

For many single-use programming tasks and small programs, hard-coding values
into the program can be sufficient. However, to make programs reusable it is
common to supply arguments to the program from the command-line.

For example, command-line arguments that specify the input data file to use will
make a data analysis program much easier to reuse compared to the same program
with a hard-coded input file.

In the [Functions episode]({{ page.root }}/15-functions/), we explored using
function arguments to customise the behaviour of a function. Function arguments
can supply data, specify options, and generally allow us to modify the function
behaviour within the limits allowed by the function design. Good function
arguments allow our functions to be reused in different situations or programs.

Command-line arguments to a program are exactly the same. They just operate for
the program as a whole rather than a single function. The goals are the same:
specify the allowable variations to behaviour for a program.

## Exploring the Options

While there are many libraries and approaches to managing command-line arguments
in Python, here we are going to limit our exploration to two options available
in the Python Standard Libraries. While these may not be the best options, they
don't require installation of additional code, and understanding their use and
limitations is invaluable when evaluating other approaches.

First, a scenario. You have written a function that reads a text file and
calculates the frequency count of words in the text. Punctuation and case are
ignored. While there are many ways to do this, here is one version that makes
use of some string processing functions, the [`sorted`][python-sorted] function
and two classes from the collections module: [`Counter`][python-counter] and
[`OrderedDict`][python-ordereddict].

~~~
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
    counts = word_count(read_file("sample-text.txt"))
    for word, count in counts.items():
        print("{0}: {1}".format(word, count))
~~~
{: .language-python}

> ## What factors might limit reusability of that program?
>
> Glossing over the details of how the program works, what features can you see
> that influence the reusability of this program?
> > ## Solution
> > - The input file is hard-coded (`"text.txt"`).
> > - The punctuation characters to be ignored are defined as a function argument
> >   with a default value, so the function is easily reused.
> > - The program does not allow the user to override the ignored punctuation.
> > - The `ignore_case` argument cannot be modified when calling the program.
> {: .solution}
{: .challenge}

> ## Before proceeding
>
> Download the [wordcount1.py][wordcount1] and [sample-text.txt][sample-text]
> files now, as they will be used for the rest of the episode.
{: .callout}

## What command-line arguments do we need?

The previous exercise identified some limitations of the word count program. Now
we will improve the program by adding command-line arguments with the following
goals:
- The required first argument should specify the input file name.
- The optional second argument specifies a string of punctuation characters
  that should be ignored in the input text.
- If no arguments are supplied, the program should print a usage message.

{% include links.md %}

[python-sorted]: https://docs.python.org/3/library/functions.html#sorted
[python-counter]: https://docs.python.org/3/library/collections.html#counter-objects
[python-ordereddict]: https://docs.python.org/3/library/collections.html#ordereddict-objects
[wordcount1]: {{page.root}}/files/wordcount1.py
[sample-text]: {{page.root}}/files/sample-text.txt
