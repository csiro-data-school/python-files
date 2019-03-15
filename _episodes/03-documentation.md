---
title: "Getting Help When You Need It: Working with Documentation"
teaching: 5
exercises: 5
questions:
- "How do I navigate the Python documentation?"
- "How can the `help()` function be used?"
- "What does the `type()` function do?"
objectives:
- "FIXME"
keypoints:
- "FIXME"
---

## The Python Documentation

The official documentation is a good place to start for any language. [The
official Python documentation][python-documentation] is generally well
organised and described, so this episode only highlights a few aspects.

The first thing to note is the the url
[https://docs.python.org/](https://docs.python.org/) automatically redirects you
to the most recent stable release of Python. If you require documentation for
a specific version, it can be selected by the drop-down box at the top left of
the page.

There are several ways to check the version of Python you are using, including:

- From a command-line, the commands `python --version` and `python3 --version`
  will report the full version.
  - Note that `python --version` may report that it is either Python 2 or 3. On
    systems where `python` is Python 2, it is common for `python3` to also be
    present.
- When running an interactive Python interpreter, the version is printed when
  the interpreter starts.
- The version can be checked programmatically:
  ~~~
  import platform
  print(platform.python_version())
  ~~~
  {: .language-python}

> ## Check your version of Python
> Using one of the methods listed above, check the version of Python you are
> using for this course.
> 
> Switch the online documentation to the same version.
{: .challenge}

> ## Find and use the `platform` online documentation
> We used the `platform.python_version()` function to retrieve the version
> string for the current Python interpreter. But the `platform` module can tell
> us a lot more information about the version of Python in use, as well as the
> underlying operating system. 
> 
> Find the documentation for the `platform` module in the online documentation.
> Which function can be used to identify the type of operating system that is
> running Python?
> > ## Solution
> > The platform documentation is in the [Library Reference
> > section][python-library]. It can be found by browsing, using the search bar
> > at the top-right of the page, or by using your browser's search in a page
> > function.
> > 
> > The operating system type is returned (if it can be determined) by the
> > `platform.system()` function:
> > [https://docs.python.org/3/library/platform.html#platform.system][platform-system]
> {: .solution}
{: .challenge}

## Checking on Types: the `type()` function

Python is a *duck-typed* language. Sometimes it isn't necessary to ensure that
variables are a specific type, it can be sufficient to simply try to use
variables in the required way. They will either *walk like a duck*, and the
operation will work, or an exception will be raised (see the [exceptions
episode]({{ page.root }}/05-exceptions/)).

However, sometimes it is helpful to check on the exact type of a variable. This
can be done with the built-in `type` function. `type` will accept any Python
object, including variables and literal values.

> ## Exploring the `type()` Function
> In an interactive Python console, or a Jupyter Notebook, execute the following
> code snippets. What does the output mean?
> ~~~
> # 1
> a = 7
> type(a)
>
> # 2
> type(7)
>
> # 3
> type(int)
>
> # 4
> type("seven")
>
> # 5
> def a_function():
>     pass
> type(a_function)
>
> # 6
> type(print)
> type(if)
> ~~~
> {: .language-python}
> > ## Solution
> > 1. `a` is a variable of type `int`
> > 2. `7` is a literal of type `int`
> > 3. `int` represents a class, and has type `type`. If you define your own
> >    classes, they will also return "<class 'type'>". Note that `type(int)`
> >    does not return `int` since the code is asking for the type of the class
> >    `int` itself. `int` is a class that defines the integers, integers will
> >    have type `int`, but `int` itself is a type.
> > 4. '"seven"' is a string literal. Strings in Python have type `str`.
> > 5. This defines a function called `a_function`. The function does nothing,
> >    but that doesn't alter the fact that it is a function.
> > 6. Both `print` and `if` are built in to the language, so why is one line an
> >    error but not the other? The answer is that `print` is a function and so
> >    has a type, while `if` is a language keyword. Keywords are parsed by the
> >    language but do not typically result in a typed runtime object.
> {: .solution}
{: .challenge}



- help()
- methods
- Intro to doc String
- ?help Jupyter
- links to docs online

{% include links.md %}

[python-documentation]: https://docs.python.org/3/
[python-library]: https://docs.python.org/3/library/index.html
[platform-system]: https://docs.python.org/3/library/platform.html#platform.system
