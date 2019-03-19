---
title: "Errors and Exceptions"
teaching: 20
exercises: 10
questions:
- "How do you handle errors in your Python code?"
objectives:
- "Explain the difference between syntax errors and run-time exceptions."
- "Understand that Python has built-in exceptions, and where to find information
  on them."
- "Write code that handles exceptions using try-catch blocks."
- "Write code to raise an exception."
- "Understand the difference between the *Look Before You Leap* and *Easier to Ask
Forgiveness than Permission* programming styles."
keypoints:
- "Illegal language constructs are called syntax errors. They are detected by
  the Python parser."
- "Legal code can also produce errors during execution, known as run-time errors."
- "In Python, run-time errors raise exceptions."
- "Exceptions are handled with the `try-catch` language feature."
- "You can raise your own exceptions with the `raise` keyword."
- "Look Before You Leap (LBYL) is a defensive programming style where you check for
  problems before executing important code."
- "It's Easier to Ask Forgiveness than Permission (EAFP) is a programming style
  where you wait for errors to occur and then handle them later."

---

> ## This episode contains Python features you may not have seen yet
> This episode refers to some language features that you may not have seen
> before, as they are presented in later episodes.
>
> Don't worry about this, as the focus here is not on using these features. All
> you need to consider is that these operations can go wrong, and that there are
> different ways of dealing with the errors.
>
> In all cases, the purpose of the code will be explained as we go.
{: .callout}

## Errors Happen

You have almost certainly encountered errors in your Python code. For beginners,
the most common is the syntax error, which occurs when your code is not valid
Python. For example:

~~~
>>> for i in range(10) print(i)
  File "<stdin>", line 1
    for i in range(10) print(i)
                           ^
SyntaxError: invalid syntax
~~~
{: .language-python}

> ## Why does that example produce a syntax error?
> The message *"SyntaxError: invalid syntax"* is correct, but not very helpful.
> 
> Note that the caret (`^`) indicates where Python detected a problem. What do
> you think the problem is?
> > ## Solution
> > The colon (`:`) that delimits the `for` loop from the loop body is missing.
> > The reason that the `print` is marked with the caret is that any code
> > following the `for` statement is invalid unless the statement is
> > delimited by a colon (`:`). So `print` is the first invalid code even though
> > the actual error occurs earlier.
> > 
> > The correct code would be:
> > ~~~
> > for i in range(10): print(i)
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}

Other types of errors cannot be detected when parsing your file. They are known
as *"Run-time Errors"*.

- In Python, run-time errors are called *exceptions*.
- Causing an exception to occur is called *raising an exception*.
- Intercepting and processing an exception is known as *catching an exception*.

> ## Run the following snippet of Python code
>
> ~~~
> numerator = 7
> denominator = 0
> result = numerator / denominator
> ~~~
> {: .language-python}
> What happens?
> > ## Solution
> > You get a `ZeroDivisionError`. This is the Python exception that indicates
> > a run-time error caused by a division by zero. Note that the code is
> > syntactically valid Python, so this is not a syntax error.
> > ~~~
> > >>> numerator = 7
> > >>> denominator = 0
> > >>> result = numerator / denominator
> > Traceback (most recent call last):
> >   File "<stdin>", line 1, in <module>
> > ZeroDivisionError: division by zero
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}

The `ZeroDivisionError` is built-in to Python. The next exercise looks at some
more [built-in exceptions][built-in-exceptions].

> ## Exploring the Built-in Exceptions
> Have a look at the documentation for
> [built-in exceptions][built-in-exceptions].
> See if you can find each of the following errors. If have encountered any
> other errors recently, see if you can find those as well.
>
> - `ZeroDivisionError`
> - `FileNotFoundError`
> - `TypeError`
> - `MemoryError`
> - `IndexError`
> - `KeyError`
>
{: .challenge}

## Handle exceptions with `try` and `catch`

The standard pattern for handling exceptions is:
~~~
try:
    # Some code that might produce an error
    ...
catch KeyError:
    # Do something with the KeyError
    ...
catch NameError:
    ...
catch:
    # Catch any error possible
    ...
else:
    # Do something that only needs to execute if no exceptions were raised in
    # the `try` block.
    ...
finally:
    # This code runs at the end, regardless of whether there is an error or not
    # Typically used for clean-up actions
    ...
~~~
{: .language-python}

- Code that might raise an exception is placed inside a `try` code block.
- Specific exception types are caught with `catch` statements following the
  `try` code block.
- If you don't specify the exception type (`catch:`), the clause will match all
  possible exceptions. This should be used with caution as it can mask many
  errors.
- Code that should only execute if no errors are raised by the `try` block is
  placed in the optional `else` section. This must come after all `catch`
  clauses.
- Code that must execute whether there is an exception or not can be placed in
  an optional `finally` block.
- Catching `Exception` will match all possible errors. In general, it is better
  to catch the most specific error possible. Look at the [exception
  hierarchy][exception-hierarchy] documentation to see how the built-in
  exceptions relate to each other.
- Any exceptions not handled by your try-catch will propagate further up in your
  program.
- Exceptions that are not handled by anything are called "*unhandled
  exceptions*". In small scripts unhandled exceptions might be fine, but in
  larger and more complex programs they usually indicate errors that should be
  handled.

In addition to their type, exception objects contain other information that
can help understand the error. This information can be seen by printing the
exception. But to do this, the caught exception has to be assigned to a variable
using the `as` keyword:

~~~
try:
    print(a)
catch NameError as e:
    print(e)
~~~
{: .language-python}

## Raising Exceptions

The `raise` statement allows you to raise a specific exception from your code.
It accepts a single argument - the exception to be raised:

~~~
>>> raise NameError('HiThere')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: HiThere
~~~
{: .language-python}

The other common use of `raise` is in a `catch` block. It is used when you want
to do something with an exception but also allow the exception to propagate back
to the outer code. For example:

~~~
try:
    function_that_uses_too_much_memory()
catch MemoryError:
    print("out of memory")
    raise  # causes the MemoryError to be raised again
~~~
{: .language-python}

## A tale of two programming styles

You are writing some code that reads from an input file. Other programs, for
reasons known only to them, occassionally create and destroy this file. Part of
the design requirements are that your program should not crash if there are
errors opening the file. In particular, if the file does not exist your program
needs to print the message *"I'm sorry, Dave. I'm afraid I can't do that"* (it
seems that the designer is a *2001: A Space Odyssey* fan).

Searching the [Python library documentation][python-library-docs] you see that
there is a function that lets you check for the existance of a file:
[`os.path.isfile`][python-isfile]. It returns `True` if the file exists,
otherwise it returns `False`. Armed with this knowledge, you write your code
(assume that `input_file_name` is already assigned the correct value):
~~~
import os  # Makes the os.path.isfile function available to our code

if os.path.isfile(input_file_name):
    input_file = open(input_file_name)  # Nothing magic here, open() just opens a file
    process_file(input_file)
else:
    print("I'm sorry, Dave. I'm afraid I can't do that")
~~~
{: .language-python}

This code is an example of a defensive programming style often
described by the catchy phrase *"Look before you leap"* (or LBYL). In LBYL
programming, we check for possible problems before trying to execute the
critical code. Examples include:

- checking for the existance of a file before trying to open it.
- checking if a denominator is zero before a division.
- checking if a variable supports a particular operation.
- checking if you have enough money before ordering lunch.

But there is a problem hiding in the previous solution. Since modern operating
systems tend to do many things at the same time, it is possible for the file to
be created or deleted in the time between the `isfile` check and attempting to
open it. If the check passes but the file is deleted before opening it, `open`
will raise the `FileNotFoundError`, leading to an unhandled exception and an
incorrect program. This is an example of a race condition.

Now consider the following code:
~~~
try:
    input_file = open(input_file_name)
    process_file(input_file)
catch FileNotFoundError:
    print("I'm sorry, Dave. I'm afraid I can't do that")
~~~
{: .language-python}

This code does not check for the existance of the file before opening it. It
just marches right in and tries to open the file. If a `FileNotFoundError` is
raised, then this exception is caught and the required message is printed. 


This is an example of a programming style called *"It's easier to ask
forgiveness than permission"* (or EAFP). While some describe this as the more
*Pythonic* approach (and indeed you see this style a lot in Python), I think
that both approaches can be valid in different circumstances.

> ## When do you think one approach or the other will be more useful?
> Some points to consider:
> - How bad is it if the error occurs?
> - How many circumstances do you need to check? Can you think of them all, or
>   perhaps trust the library implementers to do so?
> - What is expected to occur most often: the error condition or the non-error
>   case?
>       - If the error case is rare, exceptions let you put it at the end of
>         your code rather than the start.
> - Can the situation change between the error checks and the critical code?
> - Do the error checks duplicate code with the critical processing?
{: .discussion}

> ## Is the Race Condition still present?
> Is the race condition indicated in the LBYL example present in the
> EAFP solution? Discuss.
{: .discussion}

{% include links.md %}

[python-open-function]: https://docs.python.org/3/library/functions.html#open
[python-library-docs]: https://docs.python.org/3/library/index.html
[python-isfile]: https://docs.python.org/3/library/os.path.html#os.path.isfile
[built-in-exceptions]: https://docs.python.org/3/library/exceptions.html#bltin-exceptions
[exception-hierarchy]: https://docs.python.org/3/library/exceptions.html#exception-hierarchy
