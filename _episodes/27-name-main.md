---
title: "What's in a __name__?"
teaching: 10
exercises: 10
questions:
- "How do modules know when they are executing as a program, or being imported?"
- "What does `if __name__ == \"__main__\"` do?"
objectives:
- "Understand the meaning and use of `__name__`."
- "Be able to use `if __name__ == \"__main__\"` when required in your programs."
keypoints:
- "`__name__` is a string containing the module name."
- "For files directly executed by Python, `__name__` gets the special value
  \"__main__\", indicating that this is the main file."
- "The `if __name__ == \"__main__\"` expression prevents code from running when
  the module is being imported."

---

## `__name__` is a string containing the module name

Recall from the [modules episode][modules-episode] that modules are just Python
files. Every module in Python has the special attribute `__name__`. When
a module is imported, `__name__` for that module will be set to the module name.
Let's have a look at this in action.

> ## Print the `__name__` of the `math` and `sys` modules
> 
> In an interactive Python interpreter, import the `math` and `sys` modules and
> print their `__name__` strings.
> 
> Try importing a module with an alias and then print that name string. Does it
> show the alias name?
> > ## Solution
> > ~~~
> > $ python3
> > Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
> > [GCC 8.2.0] on linux
> > Type "help", "copyright", "credits" or "license" for more information.
> > >> import math
> > >> print(math.__name__)
> > math
> > >> import sys
> > >> print(sys.__name__)
> > sys
> > >> import csv as c
> > >> print(c.__name__)
> > csv
> > ~~~
> > {: .source}
> > 
> > Note that in each case, the value of `__name__` is the same as the module
> > name. The alias does not change this.
> {: .solution}
{: .challenge}

## There's Always an Exception to the Rule

> ## Printing the Exception to the Rule
> 
> Create a new Python script called "name.py". In it, print the value of
> `__name__`.
> When you run the script, do you see the module (file) name?
> > ## Solution
> > No. You should see the special value "__main__".
> {: .solution}
{: .challenge}

There is one special condition where `__name__` **does not** equal the module
name. For Python files (recall that a Python file is a module) directly executed
by Python, `__name__` gets a special value of "__main__", indicating that the
current module (file) is the main program.

## So, about that `if __name__ == "__main__"`?

In short, `if __name__ == "__main__"` is used for code that should only run when
a Python script is running as the main module. 

> ## How is this helpful? 
>
> Create and run a short program called "my_useful_program.py" with the following code in
> it:
> ~~~
> def my_useful_function():
>     return "is my_useful_function useful?"
> 
> print(my_useful_function())
> ~~~
> {: .language-python}
> 
> After using this program for a while, you decide that `my_useful_function()` is
> so useful that you want to import it into another program to use there. To
> emulate this, open a Python interpreter and import the function:
> ~~~
> from my_useful_program import my_useful_function
> ~~~
> {: .language-python}
> 
> Can you explain what just happened?
> 
> > ## Solution
> > 
> > When a module is imported, all the code gets executed once. So the code in the
> > file that makes sense when running "my_useful_program.py" as a program still
> > runs when the function is imported. A lot of the time this is not what we want.
> {: .solution}
{: .challenge}

{% include links.md %}

[modules-episode]: {{page.root}}/25-modules/index.html
