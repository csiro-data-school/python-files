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

{% include links.md %}

