---
title: "Modules"
teaching: 0
exercises: 0
questions:
- "Key question (FIXME)"
objectives:
- "First learning objective. (FIXME)"
keypoints:
- "First key point. Brief Answer to questions. (FIXME)"
---

## Modules and Packages

[Modules][python-modules] in Python are simply Python files with the .py
extension.

To import a module, we use the `import` command.

The [full list of built-in modules][python-standard-modules] can be found in the
Python documentation.

For example:
~~~
# import the library
import os

# use it
os.listdir()
~~~
{: .language-python}

> ## The `math` module
>
> In the python interpreter, import the `math` module and print the value of
> `math.pi`.
> 
> What happens if you don't import the math module first?
> > ## Solution
> > ~~~
> > $ python3
> > Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
> > [GCC 8.2.0] on linux
> > Type "help", "copyright", "credits" or "license" for more information.
> > >> import math
> > >> print(math.pi)
> > 3.141592653589793
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}

## `import` has many forms

When reading Python code, you may have seen many different types of import
statements, such as:
~~~
import math
import math as m
from math import pi
from math import *
~~~
{: .language-python}

Let's look at each one in turn.

### `import math`

The first, `import math` imports everything from the `math` module. To access
anything in `math`, you need to prefix with `math.`. This prevents conflicts
with other code, including your own.

> ## Two pi
>
> Either in a file or Python interpreter, try running the following code:
> ~~~
> pi = 3.14
> import math
> print(pi)
> print(math.pi)
> ~~~
> {: .language-python}
> Do you see that the values of `pi` and `math.pi` are different? And how using
> the module name makes it easy to know which is which?
{: .challenge}

### `import math as m`

The second form, `import math as m` is mostly the same, it just changes the name
that you need to use to refer to the imported objects. In this case, `m.`
instead of `math.`. When you start using packages from the SciPy ecosystem, you
will see this type of import a lot. Most of the common packages have
a conventional abbreviation. This keeps code concise but retains readability.
For example, rather than:
~~~
import numpy
a = numpy.array([1,2,3])
print(a)
~~~
{: .language-python}

It is more common to write:
~~~
import numpy as np
a = np.array([1,2,3])
print(a)
~~~
{: .language-python}

`np` is the conventional abbreviation (or alias) for numpy.

> ## Three pi
>
> Either in a file or Python interpreter, try running the following code:
> 
> **Make sure to start a new interpreter session, or this example won't work.**
> ~~~
> pi = 3.14
> import math as m
> print(pi)
> print(m.pi)
> print(math.pi)
> ~~~
> {: .language-python}
> > ## Solution
> > ~~~
> > $ python3
> > Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
> > [GCC 8.2.0] on linux
> > Type "help", "copyright", "credits" or "license" for more information.
> > >> pi = 3.14
> > >> import math as m
> > >> print(pi)
> > 3.14
> > >> print(m.pi)
> > 3.141592653589793
> > >> print(math.pi)
> > Traceback (most recent call last):
> >   File "<stdin>", line 1, in <module>
> > NameError: name 'math' is not defined
> > ~~~
> > {: .source}
> > The last error is because the `import math as m` changed the alias used to
> > refer to the imported math module.
> {: .solution}
{: .challenge}

### `from math import pi`

This one looks a little different. It starts with `from` rather than `import`,
but it is still an import statement. `from math import pi` is still importing
from the math module, but rather than importing everything and then needing to
access those symbols with the `math.` prefix, it specifically imports just the
definition of `pi`. There is another critical difference. See if you can work
out what it is?

> ## The differences between `import math` and `from math import pi`
>
> **Make sure to start a new interpreter session, or this example won't work.**
> 
> Either in a file or Python interpreter, try running the following code:
> ~~~
> from math import pi
> print(pi)
> print(math.pi)
> ~~~
> {: .language-python}
> > ## Solution
> > When importing specific symbols, nothing else from the module will be
> > available to your code. In this example, we have imported `pi` but nothing
> > else. Not even the `math.` prefix is defined.
> > 
> > The other critical difference is that the imported symbol no longer requires
> > a prefix. You need to take care that it doesn't conflict with your own
> > variables or functions.
> {: .solution}
{: .challenge}

### `from math import *`

The code `from math import *` looks very similar to `from math import pi`, but
the effect on your code is huge. The `*` is a wildcard that matches everything
in the math module. The effect is to import everything **without** the `math.`
prefix. While this can be very convenient during interactive coding sessions and
in small programs, great care must be taken to avoid conflicts. If two modules
that you are using both define a function called `count_words`, then the version
you end up with depends on which was imported last. Things might work, but when
they fail errors like this can be very hard to find.

For these reasons, it it generally recommended to avoid this type of 
import. However, it can still be convenient so long as you are aware of the
risks.

{% include links.md %}

[python-documentation]: https://docs.python.org/3/
[python-modules]: https://docs.python.org/3/tutorial/modules.html
[python-standard-modules]: https://docs.python.org/3/tutorial/modules.html#standard-modules
