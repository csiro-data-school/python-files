---
title: "Getting Help When You Need It: Working with Documentation"
teaching:
exercises:
questions:
- "FIXME"
objectives:
- "FIXME"
keypoints:
- "FIXME"
---

## Checking on Types: the `type()` function

Python is a *duck-typed* language. Sometimes it isn't necessary to ensure that
variables are a specific type, it can be sufficient to simply try to use
variables in the required way. They will either *walk like a duck*, and the
operation will work, or an exception will be raised (FIXME-link to exceptions
episode).

However, sometimes it is helpful to check on the exact type of a variable. This
can be done with the built-in `type` function. `type` will accept any Python
object, including variables and literal values.

> ## Exploring the `type()` Function
> In an interactive Python console, or a Jupyter Notebook, execute the following
> code snippets. Is the output what you expected?
> ~~~
> a = 7
> type(a)
>
> type(7)
>
> type("seven")
>
> def a_function():
>     pass
>
> type(a_function)
>
> type(print)
>
> type(if)
> ~~~
> {: .language-python}
> > ## Solution
> > Perhaps the only unexpected outcome is the syntax error for `type(if)`. Both
> > `print` and `if` are built in to the language, so why is one an error but
> > not the other? The answer is that `print` is a function and so has a type,
> > while `if` is a language keyword. Keywords are parsed by the language but do
> > not typically result in a typed runtime object.
> {: .solution}
{: .challenge}



- type()
- help()
- methods
- Intro to doc String
- ?help Jupyter
- links to docs online

{% include links.md %}

