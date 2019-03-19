---
title: "Testing"
teaching: 30
exercises: 30
questions:
- "What is testing and why should I test?"
- "What are the different kinds of testing?"
objectives:
- "Write a function according to a series of simple requirements and corresponding unit tests to verify expected behaviour is satisfied."
keypoints:
- ""
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

## TODO: RPN requirement headings
### first all together, then separately with code and test for each

## RPN expression evaluator

RPN = Reverse Polish Notation
<!--
<img src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Vintage_Hewlett-Packard_Model_HP-16C_Progammable_RPN_Calculator%2C_HP%27s_First_and_Only_Programmable_Calculator%2C_Circa_1988_%289330369298%29.jpg" alt="HP 16-C RPN calculator" style="width:300px">
-->
1. Accept a string containing one or more single-space delimited real
numbers, returning the last number.

1. If "+" is encountered after a space, add the last two numbers.

1. If "*" is encountered after a space, multiply the last two numbers
or results.

1. If there is not two or more operands available for an addition or    
multiplication operation, an exception should be thrown with the message: too few operands.

> ~~~
> def rpn1(str):
>    for x in str.split(" "):
>        pass
>    return float(x)
> ~~~
> {: .language-python}

### Tests TODO
* As in one day workshop
* Invalid tests:
  * Invalid chars or delimiters? 
  * Handle multiple spaces between tokens?

## Links
* [Python Testing Resources](https://confluence.csiro.au/display/~ben29w/Python+Testing+Resources)
* https://doc.rust-lang.org/book/ch11-00-testing.html
* The Humble Programmer
* Kent Beck quotes

## Notes
* Embedded C book ideas/quotes about TDD ?
* Safari links to Kent Beck, Embedded C TDD, ... ?
  * TDD vs Debug Later Programming (James Grenning, PragPub)
  * "Test code and TDD are first about supporting the writer of the code, getting the code to behave. Looking further out, it’s really about the reader, because the tests describe what we are building and then communicate it to the reader." (Grenning, "The TDD Microcycle")
* My slides re: major points
* May not want Python Testing Resources since it is on Confluence; perhaps just add links from there here?
* Sub-section with instructions for installing pytest, hypothesis?
* Instructions re: how to run a UT the first time +/- command-line options
* Look again at the string calculator/TDD notebooks 

{% include links.md %}

