---
title: "Testing"
teaching: 30
exercises: 30
questions:
- "What are the different kinds of testing?"
- "How can I write unit tests for Python code?"
- "What is Test Driven Development?"
- "What are equivalence classes and boundary conditions?"
- "What is a doctest?"
- "What is static analysis?"
objectives:
- "Learn about the key aspects of Python testing."
- "Write a function according to a series of simple requirements and corresponding unit tests to verify expected behaviour is satisfied."
keypoints:
- "..."
- "..."
- "..."
- "..."
- "..."
- "..."
---

## Outline
- Assertion
- unit
- Unit test
- Test driven Dev
- Boundary conditions
- Equivalence classes
- Reference test
- Doc test
- Static Analysis (pylint, ...)

## Introduction
See Notes

## What is testing and why test?
Validation and verification (the latter)

## What are the different kinds of testing?
System, integration, unit, ...

## Installing pytest
> For unit testing, we will be using the Python module `pytest`. From a command-line terminal with Python on the path, type the following command to install the pytest module:
> ~~~
> pip install pytest
> ~~~
> {: .language-bash}
> If you see an error like this on Windows with Anaconda:
> ~~~
> Could not install packages due to an EnvironmentError: [WinError 5] Access is denied: 'c:\\programdata\\anaconda3\\lib\\site-packages\\pip\\_internal\\basecommand.py'
> ~~~
> then run the Anaconda Prompt as Administrator.
> After the installation finishes, from a Python prompt, you should be able to import the module:
> ~~~
> import pytest
> ~~~
> {: .language-python}

## RPN expression evaluator
Remember [Reverse Polish Notation](https://commons.wikimedia.org/w/index.php?curid=1236760) (RPN) or post-fix calculators like these?

![HP 10C](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/HP-10C_programmable_calculator.jpg/220px-HP-10C_programmable_calculator.jpg)

A traditional infix expression such as `12*3+5` becomes `12 3 * 5 +`.

Suppose you are asked to write a function that takes a string representing a RPN expression and returns a real number result, along with the following requirements:
1. Accept a string containing one or more _single space_ delimited real
numbers, returning the last number entered.

1. If `+` is encountered after a _single space_, add the last two numbers, returning the result.

1. If `*` is encountered after a _single space_, multiply the last two numbers
or results, returning the result.

1. If two or more operands are not available for an addition or     multiplication operation, an exception should be thrown with the message: "too few operands".

 How would you go about writing a function to satisfy these requirements? Real world requirements captured in a natural language may be ambiguous. Moreover, explicit requirements like these often hide other implicit ones. So, analysing even simple requirements can lead to more.

 We need to write a function -- let's call it `rpn` -- somewhat like this:
> ~~~
> def rpn(expr):
>   """
>   Given a string representing a RPN expression, return the result of evaluating it.
>
>   Args:
>       expr (string): The RPN expression.
>
>   Returns:
>       float: The result of evaluating the expression.
>   """
> ~~~
> {: .language-python}

With a text editor, enter and save the beginnings of the `rpn` function above in a file called `rpn.py`.

As we start to satisfy requirements, we will also need to know whether the function is working as expected and the sooner the better. For this we need to write unit tests: code that tests code.

> From a Python interpreter prompt, type:
> ~~~
> from rpn import rpn
> rpn("12 3 * 5 +")
> ~~~
> {: .language-python}
> You will see no output after involing `rpn` since it does nothing and returns no value.

## Requirement 1
#### Accept a string containing one or more single space delimited real numbers, returning the last number entered
Even before adding anything more to `rpn`, we have enough information to write our first test.

The first requirement says that our function must accept a string containing one or more numbers separated by a space and return the last one. Let's write a test that checks for this.

> ## Write your first test
> Open up your text editor, enter and save the following Python code in a file called `rpn_pytest.py` in the same location as `rpn.py`.
> ~~~
> from rpn import rpn
>
> def test_rpn_single_num():
>    assert rpn("42") == 42.0
> ~~~
> {: .language-python}
>
> From a command-line terminal, type:
> ~~~
> py.test -v rpn_pytest.py
> ~~~
> {: .language-bash}
> > ## Solution
> > You should see something like this (with a lot of verbosity omitted):
> > ~~~
> > ...
> > rpn_pytest.py::test_rpn_num1 FAILED             [100%]
> >  ...
> >  def test_rpn_num1():
> >      assert rpn("42") == 42.0
> > E       AssertionError: assert None == 42.0
> > E        +  where None = rpn('42')
> >
> > rpn_pytest.py:21: AssertionError
> > ================ 1 failed in 0.14 seconds ================
> > ~~~
> > {: .language-bash}
> {: .solution}
{: .challenge}
Here we are creating a test and asserting that when passed the string `"42"`, `rpn` will return the number `42.0`.

Since `rpn` does nothing yet, it's no surprise that this test failed. Let's add code to our function so that the test passes.
> Edit `rpn.py` so that the function has been changed to this:
> ~~~
> def rpn(expr):
>    tokens = expr.split(" ")
>    last = tokens[-1]
>    return float(last)
> ~~~
> {: .language-python}
> Run the test again from the command-line:
> ~~~
> py.test -v rpn_pytest.py
> ~~~
> {: .language-bash}
> > ## Solution
> > Now the test should pass:
> > ~~~
> > ...
> > rpn_pytest.py::test_rpn_num1 PASSED             [100%]
> > ============== 1 passed in 0.05 seconds ==============
> > ~~~
> > {: .language-bash}
> > 
> > Repeat this edit-test cycle with alternative implementations of `rpn` and make sure the test still passes, e.g.
> > ~~~
> > def rpn(expr):
> >     return float(expr.split(" ")[-1])
> > ~~~
> > {: .language-python}
> > and
> > ~~~
> > def rpn(str):
> >    for token in str.split(" "):
> >        pass
> >
> >    return float(token)
> > ~~~
> > {: .language-python}
> >
> An important benefit here is that we can make changes to our code and have some confidence that problems will be caught by writing and running tests early. It is important to count the cost of testing in project planning. 
> {: .solution}
{: .challenge}

> ## py.test notes
> * `py.test` has numerous options, but our usage will be simple here. Run `py.test --help` for more.
> * Any function starting with `test` will be invoked as a test.
{: .callout}

> ## Write another test for requirement 1
> Requirement 1 dictates that more than one number separated by single spaces.
>
> Write a test function to assert that `rpn` returns `3.0` when `"42 3"` is passed to it.
> > ## Solution
> > It should look like this:
> > ~~~
> > def test_rpn_multiple_num():
> >     assert rpn("42 3") == 3.0
> > ~~~
> > {: .language-bash}
> > Re-run the unit tests to make sure it passes:
> > ~~~
> > py.test -v rpn_pytest.py
> > ...
> > collected 2 items
> > 
> > rpn_pytest.py::test_rpn_num1 PASSED             [ 50%]
> > rpn_pytest.py::test_rpn_num2 PASSED             [100%]
> > 
> > ============= 2 passed in 0.06 seconds ===============
> > ~~~
> > {: .language-bash}
> {: .solution}
{: .challenge}

> ## Equivalence Class
> We could write many tests similar to those above:
> * Test that passing `"56"` to `rpn` returns `56.0`.
> * Test that passing `"1 2 3 4 5"` to `rpn` returns `5.0`.
>
> Each of these tests would fall into so-called equivalence classes:
> * Test that passing a single number as a string to `rpn` yields that number as a corresponding value of type float.
> * Test that passing a string containing more than one number, each separated by a space, to `rpn` yields the right-most number as a corresponding value of type float.
{: .callout}

## Requirement 2
#### If `+` is encountered after a _single space_, add the last two numbers, returning the result.

> ## Write a test for the second requirement
> Edit `rpn_pytest.py` to add a test that asserts that 45 will be returned by `rpn` if the string `"42 3 +"` is passed to it.
> ~~~
> def test_rpn_add_with_two_num():
>     assert rpn("42 3 +") == 45.0
> ~~~
> {: .language-python}
>
> Re-running the unit tests should yield an error for the new test:
> ~~~
> py.test -v rpn_pytest.py
> ...
> E       ValueError: could not convert string to float: '+'
> ~~~
> {: .language-bash}
> Here is one approach to satisfying requirement 2:
> TODO: causing 42 then 3 to be accumulated ("pushed onto the stack"), removed, > added and the result pushed.
> ~~~
> def rpn(str):
>    nums = []
>
>    for x in str.split(" "):
>        if x == "+":
>            n2 = nums.pop()
>            n1 = nums.pop()
>            nums.append(n1+n2)
>        else:
>            nums.append(float(x))
>
>    return nums.pop()
> ~~~
> {: .language-python}
> 
> > ## Solution
> > TODO: test for "42 3 7 +" => 10.0
> > ~~~
> > ...
> > ~~~
> > {: .language-bash}
> {: .solution}
{: .challenge}

> ## Boundary Condition
> It's important to test the change in behaviour of a function relating to conditional statements such as `if`, `while`, `for`.
> TODO:
> * Other "edge cases", e.g. when number of things is a category; related to equiv classes also though
> * See example from slides
> * also empty string
{: .callout}

## Tests TODO
* As in one day workshop
* Handle multiple spaces between tokens?
* Negative numbers; like CHS on HP calculator
* Invalid tests:
  * Invalid chars or delimiters
* Multiple asserts per test function; our simple example has only shown one

## Links
* [Python Testing Resources](https://confluence.csiro.au/display/~ben29w/Python+Testing+Resources)
* https://doc.rust-lang.org/book/ch11-00-testing.html
* The Humble Programmer
* Kent Beck quotes

## Notes
* Embedded C book ideas/quotes about TDD ?
* Add Safari links to Kent Beck, Embedded C TDD, ... ?
  * TDD vs Debug Later Programming (James Grenning, PragPub)
  * "Test code and TDD are first about supporting the writer of the code, getting the code to behave. Looking further out, it’s really about the reader, because the tests describe what we are building and then communicate it to the reader." (Grenning, "The TDD Microcycle")
* Slides re: major points
* May not want to include Python Testing Resources link above since it is on Confluence; perhaps just add links from there here?
* Sub-section with instructions for installing pytest, hypothesis?
* Look again at the string calculator/TDD notebooks 

{% include links.md %}

