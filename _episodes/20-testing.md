---
title: "Testing"
teaching: 60
exercises: 30
questions:
- "What is testing?"
- "How do I write tests for Python code?"
- "What is Test Driven Development?"
- "What are equivalence classes and boundary conditions?"
- "What is a doctest?"
objectives:
- "Learn about the key aspects of Python testing."
- "Write a function according to a series of simple requirements and corresponding unit tests to verify that expected behaviour is satisfied."
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
- Static Analysis (pylint, ...) (TODO: omit?)

## Introduction
See Notes

## What is testing?
There are two closely related ideas:
* Verification: building it correctly
* Validation: building the right thing

Verification is about checking that the development of software conforms to a specification, a set of requirememts. Validation is concerned with whether or not the software to be built will satisfy the original need, whether it will be fit for purpose. Testing primarily relates to verification.

Software can be tested:
* at the level of the whole system (via a GUI or some other interface);
* at the point of integration between components;
* via units of code such as functions;
* with reference to known good output from a program.

We will focus on unit testing in this episode

A "unit" is the smallest component that can be tested, such as:
* a function
* an object, or at least one or more of an object's methods (functions)
* a module

For the purpose of this episode, the component under test will be a function.

## Installing pytest
There are a number of unit testing libraries and tools available for Python (and similar frameworks across many languages, collectively often referred to as [xUnit](https://en.wikipedia.org/wiki/XUnit)). The standard `unittest` library supplied with Python requires at least some understanding of classes (a future episode).

For unit testing in this episode, we will be using the Python module `pytest` that allows us to simply write functions that test other functions. There are also plug-ins available for `pytest` that make its use attractive. 

Before going any further, we need to install `pytest`.

> From a command-line terminal with Python on the path, type the following command to install the pytest module:
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
> Of course, you can also try this before installing `pytest` to see whether you already have it.  

## RPN expression evaluator
Remember [Reverse Polish Notation](https://commons.wikimedia.org/w/index.php?curid=1236760) (RPN) or post-fix calculators like these?

![HP 10C](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/HP-10C_programmable_calculator.jpg/220px-HP-10C_programmable_calculator.jpg)

A traditional infix expression such as `12*3+5` becomes `12 3 * 5 +`.

The operator follows the operands (numbers), e.g. `*` follows `12` and `3` (post-fix).

Then once the result of multiplying `3` by `12` is available, we're effectively left with an expression that looks like this: `36 5 +`. 

Suppose you are asked to write a function that takes a string representing a RPN expression and returns a real number result.

The following specific requirements are given:
1. Accept a string containing one or more _single space_ delimited real
number tokens and store each number in turn.

1. After all tokens have been processed, extract the last number stored and return it.

1. If `+` is encountered after a _single space_, extract the last two numbers stored, add them, and store the result.

1. If `*` is encountered after a _single space_, extract the last two numbers stored, multiply them, and store the result.

1. If two or more numbers are not available in storage for an operation (e.g addition) to proceed, an exception should be thrown with the message: "too few operands".

 How would you go about writing a function to satisfy these requirements? Real world requirements captured in a natural language may be ambiguous. Moreover, explicit requirements like these often hide other implicit ones. So, analysing even simple requirements can lead to more.

 We know we need a function -- let's call it `rpn` -- somewhat like this:
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

> From a Python interpreter prompt, type:
> ~~~
> from rpn import rpn
> rpn("12 3 * 5 +")
> ~~~
> {: .language-python}
> You will see no output after involing `rpn` since it does nothing and returns no value.

As we start to satisfy requirements, we will also need to know whether the function is working as expected and the sooner the better. For this we need to write unit tests: code that tests code.

## Requirements 1 & 2
* #### Accept a string containing one or more _single space_ delimited real number tokens and store each number in turn.
* #### After all tokens have been processed, extract the last number stored and return it.

Since at a high level we have been asked to write a function that takes a string as input and returns a real number result as output, after a bit of thought, it makes sense to consider the first two requirements together.

However, even before adding anything more to `rpn`, we have enough information to write our first test.

The first two requirements together say that our function must accept a string containing one or more numbers separated by single spaces and return the last one stored.

Let's write a test that checks for this.

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
> > rpn_pytest.py::test_rpn_num1 FAILED                    [100%]
> >  ...
> >  def test_rpn_single_number():
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

Since `rpn` does nothing yet, it's no surprise that this test failed.

Notice that in writing the test, we did not have to worry about the meaning of "token" (in this case, a sequence of non-space characters separated by single spaces, e.g. `42`) or how to go about storing numbers given such tokens. We are treating the function `rpn` as a black box (so-called black-box testing).

Let's add code to our function so that the test passes.
> Edit `rpn.py` so that the function is changed to look like this:
> ~~~
> def rpn(str):
>   nums = []
>
>   for token in str.split(" "):
>       nums.append(float(token))
>
>   return nums.pop()
> ~~~
> {: .language-python}
> Now, run the test again from the command-line:
> ~~~
> py.test -v rpn_pytest.py
> ~~~
> {: .language-bash}
> > ## Solution
> > Now the test should pass:
> > ~~~
> > ...
> > rpn_pytest.py::test_rpn_num1 PASSED                    [100%]
> > ============== 1 passed in 0.05 seconds ==============
> > ~~~
> > {: .language-bash}
> {: .solution}
{: .challenge}

> ## Test Driven Development
> The idea of writing a test then writing code to make it pass before moving on is called Test Driven Development.
>
> See [Test-driven development](https://en.wikipedia.org/wiki/Test-driven_development) for more.
> 
{: .callout}

> ## py.test notes
> * `py.test` has numerous options, but our usage will be simple here. Run `py.test --help` and [pytest}(https://docs.pytest.org/en/latest/) for more.
> * Any function starting with `test` will be invoked as a test.
{: .callout}

> ## Write another test for requirement 1
> Requirement 1 dictates that more than one number separated by single spaces be permitted.
>
> Write a test function to assert that `rpn` returns `3.0` when `"42 3"` is passed to it.
> > ## Solution
> > It should look something like this:
> > ~~~
> > def test_rpn_multiple_numbers():
> >     assert rpn("42 3") == 3.0
> > ~~~
> > {: .language-python}
> > Re-run the unit tests to make sure it passes:
> > ~~~
> > py.test -v rpn_pytest.py
> > ...
> > collected 2 items
> > 
> > rpn_pytest.py::test_rpn_num1 PASSED                    [ 50%]
> > rpn_pytest.py::test_rpn_num2 PASSED                    [100%]
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

## Requirement 3
#### If `+` is encountered after a _single space_, extract the last two numbers stored, add them, and store the result.

> ## Write a test for the third requirement
> Edit `rpn_pytest.py` to add a test that asserts that 45 will be returned by `rpn` if the string `"42 3 +"` is passed to it, completing the missing right hand side of the numeric equality operation:
> ~~~
> def test_rpn_add_with_two_numbers():
>     assert rpn("42 3 +") == _
> ~~~
> {: .language-python}
>
> > ## Solution
> > The completed test is:
> > ~~~
> > def test_rpn_add_with_two_numbers():
> >     assert rpn("42 3 +") == 45.0
> > ~~~
> > {: .language-python}
> > Re-running the unit tests will yield an error for the new test:
> > ~~~
> > py.test -v rpn_pytest.py
> > ...
> > E       ValueError: could not convert string to float: '+'
> > ~~~
> > {: .language-bash}
> {: .solution}
{: .challenge}

> ## Implement the third requirement
> To satisfy the test in the last exercise, 42 then 3 must be stored (pushed onto a [stack](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)) of numbers, which can simply be thought of as appending to a list).
>
> When a `+` is seen the two numbers must be removed (popped from the top of the stack, i.e. removed from the end of the list), added, and the result accumulated (pushed onto a stack, i.e. appended to the list).
> ![stack1](/fig/RPNstack42plus3.png) <!--{: width="242" height="120px"}-->
> Here is one approach to satisfying requirement 2. Complete the missing right hand side of the assignment to `result`:
> ~~~
> def rpn(str):
>    nums = []
>
>    for token in str.split(" "):
>        if token == "+":
>            n2 = nums.pop()
>            n1 = nums.pop()
>            result = _ _ _
>            nums.append(result)
>        else:
>            nums.append(float(token))
>
>    return nums.pop()
> ~~~
> {: .language-python}
> > ## Solution
> > The `result` assignment should look like this:
> > ~~~
> > result = n1+n2
> > ~~~
> > {: .language-python}
> > Re-running the tests should now give:
> > ~~~
> > ...
> > rpn_pytest.py::test_rpn_single_number PASSED           [ 33%]
> > rpn_pytest.py::test_rpn_multiple_numbers PASSED        [ 66%]
> > rpn_pytest.py::test_rpn_add_with_two_numbers PASSED    [100%]
> > ~~~
> > {: .language-bash}
> {: .solution}
{: .challenge}

> Edit `rpn_pytest.py`, adding a test to assert that `10` will be returned by `rpn` if the string `"42 3 7 +"` is passed to it.
> > ## Solution
> > ~~~
> > def test_rpn_add_with_three_numbers():
> >     assert rpn("42 3 7 +") == 10
> > ~~~
> > {: .language-python}
> > Re-running the tests should now give:
> > ~~~
> > ...
> > rpn_pytest.py::test_rpn_single_number PASSED           [ 25%]
> > rpn_pytest.py::test_rpn_multiple_numbers PASSED        [ 50%]
> > rpn_pytest.py::test_rpn_add_with_two_numbers PASSED    [ 75%]
> > rpn_pytest.py::test_rpn_add_with_three_numbers PASSED  [100%]
> > ~~~
> > {: .language-bash}
> {: .solution}
{: .challenge}

> ## Why not add up everything?
> In the example above (`"42 3 7 +"`) we have this sequence of stack changes:
> ![42 3 7 + stack changes](/fig/RPNstack42plus3plus7.png)
>
> Add a unit test to check that `rpn` can add all three numbers.
> > ## Solution
> > ~~~
> > def test_rpn_add_all_three_numbers():
> >     assert rpn("42 3 7 + +") == 52.0
> > ~~~
> > {: .language-python}
> > Re-running the unit tests should give:
> > ~~~
> > py.test -v rpn_pytest.py
> > ...
> > rpn_pytest.py::test_rpn_single_number PASSED           [ 20%]
> > rpn_pytest.py::test_rpn_multiple_numbers PASSED        [ 40%]
> > rpn_pytest.py::test_rpn_add_with_two_numbers PASSED    [ 60%]
> > rpn_pytest.py::test_rpn_add_with_three_numbers PASSED  [ 80%]
> > rpn_pytest.py::test_rpn_add_all_three_numbers PASSED   [100%]
> > ~~~
> > {: .language-bash}
> {: .solution}
{: .challenge}

> ## When 0.1 + 0.2 doesn't equal 0.3
> Real number operations sometimes yield unexpected results due to the vagaries of floating point implementaions.
>
> See [Why don't my numbers add up](https://floating-point-gui.de/) for more.
>
> Add this `import` near the top of `rpn_pytest.py`:
> ~~~
> import pytest
> ~~~
> {: .language-python}
> Then add the following test function:
> ~~~
> def test_rpn_add_inexact():
>    assert rpn("0.1 0.2 +") == 0.3
> ~~~
> {: .language-python}
> Re-running the tests gives:
> ~~~
> rpn_pytest.py::test_rpn_add_inexact FAILED               [100%]
> ...
>    def test_rpn_add_inexact():
>       assert rpn("0.1 0.2 +") == 0.3
> E       AssertionError: assert 0.30000000000000004 == 0.3
> E        +  where 0.30000000000000004 = rpn('0.1 0.2 +')
> ...
> ~~~
> {: .language-bash}
> pytest provides a function called `approx` to determine whether a number is approximately the same as or close to -- within some tolerance (+/- 0.000001 by default) -- some number.
>
See [pytest.approx](https://docs.pytest.org/en/latest/reference.html#pytest-approx) for more.
>
> Replacing `test_rpn_add_inexact` with the following will result in a passing test:
> ~~~
> def test_rpn_add_approx():
>     assert rpn("0.1 0.2 +") == pytest.approx(0.3)
> ~~~
> Notice that there was nothing explicit in the requirements about this, but you will find yourself sometimes having to think in terms of numerical tolerance when writing tests.
{: .callout}

## Requirement 4
#### If `*` is encountered after a _single space_, extract the last two numbers stored, multiply them, and store the result.

Let's move onto the next requirement.

> ## Test and implement multiplication
> Add these two unit tests to `rpn_pytest.py`:
> ~~~
> def test_rpn_multiply_with_two_numbers():
>     assert rpn("42 3 *") == 126.0
>
> def test_rpn_multiply_with_three_numbers():
>     assert rpn("42 3 2 * *") == 252.0
> ~~~
> {: .language-python}
> Since we haven't implemented multiplication yet, the tests will of course fail.
>
> Add handling of multiplication to the `rpn` function by completing the missing code indicated with `_`.
> ~~~
> def rpn(str):
>    nums = []
>
>    for token in str.split(" "):
>        if token == "+":
>            n2 = nums.pop()
>            n1 = nums.pop()
>            result = n1+n2
>            nums.append(result)
>        elif token == "_":
>            _______________
>            _______________
>            result = ___
>            nums.append(result)
>        else:
>            nums.append(float(token))
>
>    return nums.pop()
> ~~~
> {: .language-python}
> > ## Solution
> > You should see:
> > ~~~
> > def rpn(str):
> >    nums = []
> >
> >    for token in str.split(" "):
> >        if token == "+":
> >            n2 = nums.pop()
> >            n1 = nums.pop()
> >            result = n1+n2
> >            nums.append(result)
> >        elif token == "*":
> >            n2 = nums.pop()
> >            n1 = nums.pop()
> >            result = n1*n2
> >            nums.append(result)
> >        else:
> >            nums.append(float(token))
> >
> >    return nums.pop()
> > ~~~
> > The two tests we added above should pass now:
> > ~~~
> > ...
> > rpn_pytest.py::test_rpn_multiply_with_two_numbers PASSED    [ 87%]
> > rpn_pytest.py::test_rpn_multiply_with_three_numbers PASSED  [100%]
> > ...
> > ~~~
> > {: .language-bash}
> {: .solution}
{: .challenge}

Adding the multiplication case resulted in duplicated code. This would be compounded for each new operation added, e.g. `-`, `/`, `^`.

> ## Factoring out common code
> Modify `rpn.py` to introduce a `popargs` function that takes the list of numbers (the stack) and returns the two top numbers. Also remove the assignment to `result`.
> ~~~
> def rpn(str):
>    nums = []
>
>    for token in str.split(" "):
>        if token == "+":
>            n1, n2 = popargs(nums)
>            nums.append(n1+n2)
>        elif token == "*":
>            n1, n2 = popargs(nums)
>            nums.append(n1*n2)
>        else:
>            nums.append(float(token))
>
>    return nums.pop()
>
> def popargs(nums):
>    n2 = nums.pop()
>    n1 = nums.pop()
>    return n1, n2
> ~~~
> {: .language-python}
> Re-running the tests should show that they all still pass.
>
> The change above is a modest improvement. Another improvement would be to have a dictionary of operator strings (`+`, `*`, ...) to `lambda` expressions (functions without a name).
>
> Adding new operations on two numbers would then just be a matter of adding another dictionary entry.
>
> Change `rpn` as follows:
> ~~~
> def rpn(str):
>    opfuncs = {
>        "+": lambda x,y: x+y, 
>        "*": lambda x,y: x*y 
>    }
>
>    nums = []
>
>    for token in str.split(" "):
>        if token in opfuncs:
>            n1, n2 = popargs(nums)
>            func = opfuncs[token]
>            nums.append(func(n1, n2))
>        else:
>            nums.append(float(token))
>
>    return nums.pop()
> ~~~
> {: .language-python}
> Again, re-running the tests should show that they all still pass.

> ## Refactoring
> The practice of modifying code in order to factor out commonality, improve performance or maintainability, or otherwise modify internal implementation without changing interface (e.g. function parameters or return type) or functionality is known as refactoring.
>
> An important benefit here is that we can make changes to our code and have some confidence that problems will be caught by writing and running tests early and often.
>
> It also promotes what Richard Gabriel has called [habitability](https://www.dreamsongs.com/Files/PatternsOfSoftware.pdf) of code:
>
> > Habitability is the characteristic of source code that enables programmers, coders, bug-fixers, and people coming to the code later in its life to understand its construction and intentions and to change it comfortably and confidently... Habitability makes a place livable, like home. And this is what we want in software -- that developers feel at homes.
{: .callout}

> ## Regression Tests
> When a bug is found or reported, sometimes a unit test can be used to capture the problem
{: .callout}

> ## Documentation
> Tests also provide documentation, in the form of code, of what the code must be able to do.
{: .callout}

> ## The Cost
> Developing software is more than just writing code that implements functionality. It is important to count the cost of testing in project planning.
{: .callout}

## Requirement 5
#### If two or more numbers are not available in storage for an operation (e.g addition) to proceed, an exception should be thrown with the message: "too few operands".

> ## Boundary Condition
> It's important to test the change in behaviour of a function relating to conditional statements such as `if`, `while`, `for`.
> TODO:
> * Other "edge cases", e.g. when number of things is a category; related to equiv classes also though
> * See example from slides: min()
> * Also empty string: one or more tokens, so "", "n"
{: .callout}

## Tests TODO
* Additional requirement or bug report: Handle multiple spaces between tokens?
* Negative numbers; like CHS on HP calculator
* Multiple asserts per test function; our simple example has only shown one
* What other tests can you think of? 
  * `12 3 * 5 +` from intro
  * Invalid test: Invalid chars or delimiters
  * Add more operators

## Links
* https://doc.rust-lang.org/book/ch11-00-testing.html
* The Humble Programmer
* Kent Beck quotes

## Notes
* Embedded C book ideas/quotes about TDD ?
* Add Safari links to Kent Beck, Embedded C TDD, ... ?
  * TDD vs Debug Later Programming (James Grenning, PragPub)
  * "Test code and TDD are first about supporting the writer of the code, getting the code to behave. Looking further out, it’s really about the reader, because the tests describe what we are building and then communicate it to the reader." (Grenning, "The TDD Microcycle")
* Slides re: major points
* Sub-section with instructions for installing pytest, hypothesis?
* Look again at the string calculator/TDD notebooks 

{% include links.md %}