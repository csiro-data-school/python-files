---
title: "Getting Help When You Need It: Working with Documentation"
teaching: 5
exercises: 5
questions:
- "What does the `type()` function do?"
objectives:
- "FIXME"
keypoints:
- "FIXME"
---

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

