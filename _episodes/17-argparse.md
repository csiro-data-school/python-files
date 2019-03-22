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

- The input text. This is required.
- An optional set of punctuation characters that will be ignored in the text.
- An optional flag indicating whether comparisons are case-sensitive.
- An optional integer specifying the minimum word frequency required for the
  word to be displayed.

We will tackle these one at a time, but first we have to get the boilerplate out
of the way. `argparse` has a few lines of code that are always required to
initialise and process the command-line arguments. They are present in the
previous example, but here there are with everything else removed:

FIXME todo

# FIXME: Old content follows


## What command-line arguments do we need?

The previous exercise identified some limitations of the word count program. Now
we will improve the program by adding command-line arguments with the following
goals:

- The first argument should specify the input file name.
- The optional second argument specifies a string of punctuation characters
  that should be ignored in the input text.
- If no arguments are supplied, the program should print a usage message.


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
[python-sys-argv]: https://docs.python.org/3/library/sys.html#sys.argv
[argparse]: https://docs.python.org/3/library/argparse.html
[argparse-tutorial]: https://docs.python.org/3/howto/argparse.html
[argparse1]: {{page.root}}/files/command_lines/argparse1.py
[wordcount]: {{page.root}}/files/command_lines/wordcount.py
[wordcount1]: {{page.root}}/files/command_lines/wordcount1_solution.py
[wordcount2]: {{page.root}}/files/command_lines/wordcount2.py
[sample-text]: {{page.root}}/files/command_lines/sample-text.txt
