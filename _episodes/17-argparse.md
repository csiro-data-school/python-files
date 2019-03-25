---
title: "Getting arguments from the command-line"
teaching: 30
exercises: 40
questions:
- "Why are command-line arguments useful?"
- "How can I add command-line arguments to my programs?"
objectives:
- "Gain experience reading and modifying code written by someone else."
- "Implement command-line arguments with `argparse`."
keypoints:
- "Using command-line arguments can make your programs easier to use and reuse."

---

> ## Before proceeding
>
> Make sure you have followed the [setup instructions][setup-instructions] to
> download and unzip the [intermediate_python_data.zip][intermediate_python_data]
> file.
{: .callout}

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

Have a look at the file [wordcount.py][wordcount]. It contains three
functions. The first, `read_file`, returns the entire contents of a file as
a single string. The second, `word_count` returns a dictionary containing the
count of words found in a string. The third, `print_counts` displays the
results. The function signatures are:

~~~
def read_file(filename):
    """Returns the contents of a text file as a single string, with newlines
    converted to spaces.
    """

def word_count(text, characters_to_ignore=",.?", case_sensitive=False):
    """Returns an ordered dictionary containing the sorted count of words in
    a string, with the word as dictionary key.
    """

def print_counts(counts, min_count=2):
    """Prints the word counts. Only words with a count greater than or equal to
    `min_count` are displayed.
    """
~~~
{: .language-python}

Don't worry about how these functions work. The important thing for this
episode is knowing what the inputs and outputs are.

> ## Run wordcount.py
>
> Try running the `wordcount.py` file from the command-line:
>
> ~~~
> $ python3 wordcount.py
> ~~~
> {: .language-bash}
> What happens?
> > ## Solution
> >
> > Nothing. The file defines the functions, but does not call them.
> {: .solution}
{: .challenge}

## Running `word_count` in the simplest possible way

We need a new program to use the three provided functions. Our program will
read from a file, count the words, and display the results.
The data inputs we have to work with are:

1. The input file name.
2. The punctuation characters to ignore in the file.
3. Whether the comparisons are case-sensitive.
4. The minimum count threshold to display.

Items 2, 3, and 4 all have default values in the functions, so let's just use
those for now. All that is left is the input file.

> ## The simplest possible program to call `word_count`
>
> Having looked at the possible inputs, the simplest thing is
> to hard-code the file name, relying on default function arguments for everything
> else. The ["sample-text.txt"][sample-text] file contains some text designed to
> test the word count functions, so we will use that.
>
> Here is a program fragment that is missing some essential parts. Your
> challenge is to complete the program and run it.
>
> Save your program as "wordcount1.py".
> ~~~
> from wordcount import read_file, word_count, print_counts
>
> data = read_file("")      # add the filename
> counts = word_count(...)  # add appropriate function arguments
> print_counts(...)         # add appropriate function arguments
> ~~~
> {: .language-python}
>
> The expected output is:
> ~~~
> line: 7
> this: 4
> is: 2
> a: 2
> does: 2
> ~~~
> {: .source}
>
> > ## Solution
> > ~~~
> > from wordcount import read_file, word_count, print_counts
> >
> > data = read_file("sample-text.txt")
> > counts = word_count(data)
> > print_counts(counts)
> > ~~~
> > {: .language-python}
> The solution is available [here][wordcount1].
> {: .solution}
{: .challenge}

## Introducing `argparse`

Being able to run the code at all is great progress. However, wordcount1.py is
quite limited. The file name is hard-coded, and all the other parameters just
use the default values. Without modifying the program, we can't run it on
different files, or display all words regardless of their frequency. And if our
text has different punctuation characters, we can't handle them.

It would be great if we could pass all these things in when running our program.

It would be even greater if our program could also display a helpful message
when we supply the wrong arguments, or just when we ask for help.

`argparse` is a module in the Python Standard Library that does all of this for
us. We just need to tell it what our arguments are and it handles the rest.
It is not my goal to reproduce the [argparse documentation][argparse] here, but
to summarise, `argparse` provides a consistent approach to:

- Positional arguments (specified by position in the argument list).
- Optional arguments with default values.
- Named arguments (either optional or required), with both long and short
  variations.
- Argument validation.
- Standardised help and usage messages.

To illustrate what `argparse` code looks like, here is an example from the
[official argparse tutorial][argparse-tutorial]. The example specifies a single
positional argument and then prints the supplied text.
~~~
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo")
args = parser.parse_args()
print(args.echo)
~~~
{: .language-python}

Calling the program without any arguments prints an automatically generated
error message:
~~~
$ python3 prog.py
usage: prog.py [-h] echo
prog.py: error: the following arguments are required: echo
~~~
{: .source}

Calling the program with the `-h` (or `--help`) flags prints an automatically
generated help message:
~~~
$ python3 prog.py --help
usage: prog.py [-h] echo

positional arguments:
  echo

optional arguments:
  -h, --help  show this help message and exit
~~~
{: .source}

And calling the program with any other values echoes the supplied text:
~~~
$ python3 prog.py foo
foo
~~~
{: .source}

## Designing our User Interface

Even for simple user interfaces, it is helpful to think about what we want
first.

Here, we would like to specify the following:

- The input text.
    - Required.
    - Positional argument named "file".
    - Argument data type: `str`
- An optional set of punctuation characters that will be ignored in the text.
    - Optional.
    - Default value: ",.?"
    - Short-form name: `-p`
    - Long-form argument name: `--punctuation`
    - Argument data type: `str`
- An optional flag indicating whether comparisons are case-sensitive.
    - Optional.
    - Default value: `False`
    - Short-form name: `-c`
    - Long-form argument name: `--case-sensitive`
    - Argument data type: `bool`
- An optional integer specifying the minimum word frequency required for the
  word to be displayed.
    - Optional.
    - Default value: 2
    - Short-form name: `-m`
    - Long-form argument name: `--min-count`
    - Argument data type: `int`

> ## Write wordcount2.py
>
> Your challenge is to implement the arguments in our design by completing
> [wordcount2.py][wordcount2]. This program has the basic elements in place,
> however it contains some missing sections and a couple of errors. To fix it,
> you will need to pay attention to the error messages that come from running
> wordcount2.py. You may also need to refer to [the argparse
> documentation][argparse].
>
> The following test cases show the test command line and the expected output
> for some combinations of inputs. Make sure you try other combinations as well
> to see if the outputs look OK.
>
> ### No arguments
> ~~~
> $ python3 wordcount2.py
> usage: wordcount2.py [-h] [-p PUNCTUATION] [-c] [-m MIN_COUNT] file
> wordcount2.py: error: the following arguments are required: file
> ~~~
> {: .language-source}
> 
> ### Help
> ~~~
> $ python3 wordcount2.py --help
> usage: wordcount2.py [-h] [-p PUNCTUATION] [-c] [-m MIN_COUNT] file
> 
> positional arguments:
>   file                  The input text file
> 
> optional arguments:
>   -h, --help            show this help message and exit
>   -p PUNCTUATION, --punctuation PUNCTUATION
>                         Punctuation to ignore when counting words.
>   -c, --case-sensitive  Force a case-sensitive count. By default, case is
>                         ignored.
>   -m MIN_COUNT, --min-count MIN_COUNT
>                         The minimum word count threshold for display.
> ~~~
> {: .language-source}
> 
> ### File argument
> ~~~
> $ python3 wordcount2.py sample-text.txt 
> line: 7
> this: 4
> a: 3
> is: 2
> why: 2
> does: 2
> or: 2
> two;;: 2
> ~~~
> {: .language-source}
> 
> ### Semi-colon in punctuation
> 
> ~~~
> $ python3 wordcount2.py sample-text.txt --punctuation ",.?;"
> line: 7
> this: 4
> a: 3
> two: 3
> is: 2
> why: 2
> does: 2
> or: 2
> ~~~
> {: .language-source}
> 
> ### Case-sensitive comparisons
> 
> Note that the count for some words has changed. Try setting the `-min-count`
> flag to 1 to see the full set of words.
> ~~~
> $ python3 wordcount2.py sample-text.txt --case-sensitive
> line: 6
> this: 3
> is: 2
> a: 2
> does: 2
> or: 2
> two;;: 2
> ~~~
> {: .language-source}
> > ## Solution
> > [wordcount2_solution.py][wordcount2_sln] contains a working version of the program.
> {: .solution}
{: .challenge}

{% include links.md %}

[setup-instructions]: {{page.root}}/setup.html
[intermediate_python_data]: {{page.root}}/files/intermediate_python_data.zip
[python-sorted]: https://docs.python.org/3/library/functions.html#sorted
[python-counter]: https://docs.python.org/3/library/collections.html#counter-objects
[python-ordereddict]: https://docs.python.org/3/library/collections.html#ordereddict-objects
[python-sys-argv]: https://docs.python.org/3/library/sys.html#sys.argv
[argparse]: https://docs.python.org/3/library/argparse.html
[argparse-tutorial]: https://docs.python.org/3/howto/argparse.html
[wordcount]: {{page.root}}/files/command_lines/wordcount.py
[wordcount1]: {{page.root}}/files/command_lines/wordcount1_solution.py
[wordcount2]: {{page.root}}/files/command_lines/wordcount2.py
[wordcount2_sln]: {{page.root}}/files/command_lines/wordcount2_solution.py
[sample-text]: {{page.root}}/files/command_lines/sample-text.txt
