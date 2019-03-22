---
title: "Getting arguments from the command-line"
teaching: 15
exercises: 25
questions:
- "Why are command-line arguments useful?"
- "How can I add command-line arguments to my programs?"
objectives:
- "Gain experience reading and modifying code written by someone else."
- "Be able to write simple command-line arguments using `sys.argv`."
- "Write more complex command-line arguments with `argparse`."
- "Become more comfortable with text file processing."
keypoints:
- "Using command-line arguments can make your programs easier to use and reuse."
- "`sys.argv` is the oldest and simplest method for reading command-line
  arguments in Python. It just returns a list of strings."
- "The simplicity of `sys.argv` brings limitations, and may lead to more complex
  code."

---

> ## Before proceeding
>
> Make sure you have followed the [setup instructions][setup-instructions] to
> download and unzip the [intermediate_python_data.zip][intermediate_python_data]
> file.
{: .callout}


# TODO

- argparse
  - define args
  - arg types
  - optional args, default values
  - help strings
  - filters and constraints (eg: files must exist)
- click

## Command-line Arguments Make Your Programs Easier to Use and Reuse

Have you ever written a short program, and then a few months
later discovered that you that you can't remember exactly how to use it? While
good comments and docstrings help, command-line arguments with usage messages
can also help.

For many single-use programming tasks and small programs, hard-coding values
into the program can be sufficient. However, to make programs reusable it is
helpful to supply arguments to the program from the command-line.

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

In the exercises that follow, pay attention to how arguments to the primary
function directly influence the command-line arguments.

## Introducing Word Count

Have a look now at the file [wordcount1.py][wordcount1]. It contains two
functions. The first, 

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
> >
> > - The input file is hard-coded (`"text.txt"`).
> > - The punctuation characters to be ignored are defined as a function argument
> >   with a default value, so the function is easily reused.
> > - The program does not allow the user to override the ignored punctuation.
> > - The `ignore_case` argument cannot be modified when calling the program.
> {: .solution}
{: .discussion}


## What command-line arguments do we need?

The previous exercise identified some limitations of the word count program. Now
we will improve the program by adding command-line arguments with the following
goals:

- The first argument should specify the input file name.
- The optional second argument specifies a string of punctuation characters
  that should be ignored in the input text.
- If no arguments are supplied, the program should print a usage message.

## Method 1: `sys.argv`

The oldest method that Python provides for passing arguments to your programs is
[`sys.argv`][python-sys-argv]. It does nothing more than return a list
containing the whitespace delimited strings from the command-line that executed
your program. For example, the command "python3 my_file.py option1 option2"
would return `["my_file.py", "option1", "option2"]` from `sys.argv`.
If you have programmed in C, then this will be familiar, as `sys.argv` was
modelled on the C approach.

> ## Echo command-line arguments
> Write a short program that uses `sys.argv` to echo the command-line arguments
> back to the user. Each argument should print on a separate line along with the
> argument index.
>
> Once you have a working program, spend a few minutes exploring different
> arguments and their effect.
> > ## Solution
> >
> > ~~~
> > import sys
> > for index, arg in enumerate(sys.argv):
> >     print("{0}: {1}".format(index, arg))
> > ~~~
> > {: .language-python}
> > This is also provided as [argv-echo.py][argv-echo].
> {: .solution}
{: .challenge}

The first value in the list is always the name of your script, and so it should
be ignored in "wordcount2.py".

> ## Write wordcount2.py
>
> Your challenge is to modify wordcount1.py to use `sys.argv` to implement these
> features:
>
> - The first argument should specify the input file name.
> - The optional second argument specifies a string of punctuation characters
>   that should be ignored in the input text.
> - If no arguments are supplied, the program should print a usage message.
>
> > ## Solution
> >
> > Without reproducing the whole program, here is the important new code.
> > [Download the solution][wordcount2] if required. Note that my usage message
> > is not great. Writing good usage messages is hard.
> >
> > ~~~
> > ...
> >
> > if __name__ == "__main__":
> >
> >     # If we have less than two arguments, print the usage message and exit
> >     if len(sys.argv) < 2:
> >         print("{0} usage: {0} input_file <'punctuation to ignore'>".format(
> >             sys.argv[0]))
> >         exit()
> >
> >     # First argument (and second in argv) is the input file.
> >     input_file = sys.argv[1]
> >
> >     # Second argument (if it exists) is the punctuation to ignore.  Since it is
> >     # optional, we use the Python ternary operator to assign a default value if
> >     # the argument was not supplied
> >     characters_to_ignore = sys.argv[2] if len(sys.argv) > 2 else ",.?"
> >
> >     counts = word_count(
> >             read_file(input_file),
> >             characters_to_ignore=characters_to_ignore)
> >
> >     ...
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}

> ## What do you think of `sys.argv` as a method?
>
> Spend a few minutes to discuss this with the class. What are some advantages
> and disadvantages to using `sys.argv`?
>
> > ## Some thoughts
> >
> > - The method is simple, so for simple programs `sys.argv` may be all you
> >   need.
> > - For complex programs, you can end up doing a lot of low-level work that
> >   could be done by a library.
> > - Tends to produce inflexible interfaces. For example, specifying arguments
> >   in a different order requires a lot more code.
> > - `sys.argv` just returns strings. If you need other data types (eg: `bool`,
> >   `int`) then extra work is needed.
> > - Common features of modern interfaces are tedious to implement:
> >   - optional arguments.
> >   - standardised help text, including descriptions of all arguments.
> >   - short and long form arguments (eg: `-f` and `--file`).
> >   - Validation for specific arguments (eg: files must exist).
> {: .solution}
{: .discussion}

## Method 2: `argparse`

In addition to `sys.argv`, the Python Standard Library provides another method
for managing command-line arguments: `argparse`. It is not my goal to reproduce
the [argparse documentation][argparse] here, but to summarise, `argparse`
provides a consistent approach to:

- Positional arguments (specified by position in the argument list).
- Optional arguments with default values.
- Named arguments (either optional or required), with both long and short
  variations.
- Validation.
- Standardised help and usage messages.

The simplest example ([argparse1.py][argparse1]) shows how to initialise `argparse` in your code:
~~~
import argparse
parser = argparse.ArgumentParser()
parser.parse_args()
~~~
{: .language-python}

FIXME: Should I spoon feed the exercise and solution? Provide a partial
implementation of wordcount3.py and get users to complete/fix it?

> ## Write wordcount3.py
>
> Your challenge is to modify wordcount2.py to use `argparse` to implement these
> features:
> - The input file name is required, and can be specified with either short-form
>   (`-f`) or long-form arguments (`--file`).
> - An optional argument (`-p`, `--punctuation`) specifies the punctuation
>   characters to be ignored. It should have a default value of `".,?"`.
> - If no arguments are supplied, the program should print a usage message. The
>   usage message should describe the program purpose, the arguments (including
>   short and long-form) and whether a value is required or optional.
>
> > ## Solution
> > FIXME
> {: .solution}
{: .challenge}

{% include links.md %}

[setup-instructions]: {{page.root}}/setup.html
[intermediate_python_data]: {{page.root}}/files/intermediate_python_data.zip
[python-sorted]: https://docs.python.org/3/library/functions.html#sorted
[python-counter]: https://docs.python.org/3/library/collections.html#counter-objects
[python-ordereddict]: https://docs.python.org/3/library/collections.html#ordereddict-objects
[wordcount1]: {{page.root}}/files/wordcount1.py
[wordcount2]: {{page.root}}/files/wordcount2.py
[argv-echo]: {{page.root}}/files/argv-echo.py
[sample-text]: {{page.root}}/files/sample-text.txt
[python-sys-argv]: https://docs.python.org/3/library/sys.html#sys.argv
[argparse]: https://docs.python.org/3/library/argparse.html
[argparse1]: {{page.root}}/files/argparse1.py
