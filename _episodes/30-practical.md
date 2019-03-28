---
title: "Final practical: How Many Articles Reference that they use R and/or Python?"
questions:
- "Can I write a command line Python progam using ArgParse?"
objectives:
- "Write a Python script that accepts arguments."
- "Write a Python script opens a file and searches for words."
- "Document your Python script using comments."
keypoints:
- ""
- ""
- ""
---

## Final Practical

* This final practicle is going to combine all that you have learnt about Python into one command line program!
* The challenge is to write a command line Python progam using Argparse (under version control) that can:
	* Open a plain text file of a research article.
	* Search the article for references to `R` and/or `Python`.
		* <i>bonus: search for the versions of `R` or `Python`<i\>
	* Return the number of times the article refers to `R` and/or `Python`.
	* Choose whether or not to save the output and choose the output file name.

## Example articles
### Python 
**PDF**
* https://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.1005871&type=printable

**XML**
* https://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.1005871&type=manuscript

### Python and R 
**PDF** 
* https://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.1005510&type=printable

**XML**
* https://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.1005510&type=manuscript

### R 
**PDF**
* https://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.1004140&type=printable

**XML**
* https://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.1004140&type=manuscript


> ## Part 1 - Setup of Git Repository and Python Program
>
> Open `Git Bash` and move to the directory where you want to work with your new Python project. <br/>
> Now we need to initiate our new `Git Repository` so that we have our work under version control!
>
> > ## CHALLENGE: Initiate your git repository
> > > ## Solution
> > > ~~~
> > > git init python_prac
> > > ~~~
> > > {: .language-bash}
> > {: .solution}
>
>
> Next move to your new folder `python_prac` and set up an appropriate sub-folder structure for this project. 
> What folders will you need?
>
> Download the XML versions of the manuscript and save them in the appropriate folder.
>
> Create your Python program by opening your chosen text <br/> 
> editor and saving it to the appropriate place with an appropriate name. <br/>
> e.g. using VIM in `Git Bash`. Write a comment `#` at the top of your program stating what it does and then save it.
>
> ~~~
> cd scripts
> vim ref_finder.py
> ~~~
> {: .language-bash}
>
> Run `git status` to see if our new file is under version control.
>
> ~~~
> git status
> ~~~
> {: .language-bash}
> ~~~
> On branch master
>
> No commits yet
>
> Untracked files:
>   (use "git add <file>..." to include in what will be committed)
> 
>         scripts/ref_finder.py
>
> nothing added to commit but untracked files present (use "git add" to track)
> ~~~
> {: .output}
>
> > ## CHALLENGE: Add and commit your python program so that is it under version control.
> > > ## Solution
> > > ~~~
> > > git add scripts/ref_finder.py
> > > git commit -m "inital commit"
> > > ~~~
> > > {: .language-bash}
> > {: .solution}
> {: .challenge}
{: .callout}



## Now we are ready to start coding!!

## Part 2 - Structure of Python Program

> ## CHALLENGE: How do we Start? Write down in words what you want your program to do.
> > ## Hint
> > 1. Read in the words in a chosen text document (text file - XML) line-by-line.
> > 2. Search each line for the words "R" and/or "Python".
> > 3. Keep a running tally of the number of times the words "R" and/or "Python" occur.
> > 4. Print out the result.
> > 5. Save the result to a text document.
> {: .solution}
{: .challenge}

Let's start by getting our code to work interactively in Jupyter first.

> ## CHALLENGE: Open a Jupyter Notebook and write code to read a text file line by line and print each line.
> > ## Solution
> > ~~~
> > file = 'file location'
> > with open(file, "r") as f:
> >    for line in f:
> >        print(line)
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}

> ## CHALLENGE: Copy your Jupyter Notebook code into a new cell and 
> integrate a string search for 'Python' and print the number of counts.
> > ## Solution
> > ~~~
> > file = 'file location'
> > count = 0
> > with open(file, "r") as f:
> >     for line in f:
> >         count += line.count(' Python ')
> >         print("Python was found", count, "times")
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}

> ## CHALLENGE: In a new cell in your Jupyter Notebook, turn your script into a reusable function.
> > ## Solution
> > ~~~
> > def ref_finder(file_location):
> >     """counts occurences of the word 'Python' in a text file"""
> >     count = 0
> >     with open(file_location, "r") as f:
> >         for line in f:
> >             count += line.count(' Python ')
> >         print("Python was found", count, "times")
> >         return(count)
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}

> ## CHALLENGE: Copy your function into your ref_finder.py program and integrate Argparse 
> so that your program can accept any file from the command line.
>>## Solution
>>~~~
>>import argparse
>>
>>def ref_finder(file_location):
>>    """counts occurences of the word 'Python' in a text file"""
>>    count = 0
>>    with open(file_location, "r") as f:
>>        for line in f:
>>                count += line.count(' Python ')
>>        print("Python was found", count, "times")
>>        return(count)
>>
>>parser = argparse.ArgumentParser()
>>parser.add_argument("file_location")
>>args = parser.parse_args()
>>ref_finder(args.file_location)
>>~~~
>>{: .language-python}
>{: .solution}
{: .challenge}

> ## CHALLENGE: Update your ref_finder.py program to include optional arguments so you can search for references to 'R' or 'Python'.
>> ## Solution
>> ~~~
>> import argparse
>>
>> def ref_finder(file_location, language):
>>     """counts occurences of a string in a text file"""
>>     count = 0
>>     with open(file_location, "r") as f:
>>         for line in f:
>>                 count += line.count(' ' + language + ' ')
>>         print(string, "was found", count, "times")
>>         return(count)
>>
>> parser = argparse.ArgumentParser()
>> parser.add_argument("file_location")
>> parser.add_argument("language")
>> args = parser.parse_args()
>> ref_finder(args.file_location, args.language)
>> ~~~
>> {: .language-python}
> {: .solution}
{: .challenge}

> ## CHALLENGE: Update your ref_finder.py program so that it can search for both 'R' and 'Python' as an optional argument, printing the counts for both.
>> ## Solution
>> ~~~
>> import argparse
>>
>> def ref_finder(file_location, language, count_both):
>>     """counts occurences of a string in a text file"""
>>     file = file_location
>>     if both == True:
>>         string1 = ' R '
>>         string2 = ' Python '
>>         with open(file, "r") as f:
>>         for line in f:
>>             R_count += line.count(string1)
>>             Py_count += line.count(string2)
>>         print(string1, "was found", R_count, "times")
>>         print(string2, "was found", Py_count, "times")
>>     else:
>>         string = language
>>         with open(file, "r") as f:
>>             for line in f:
>>                 count += line.count(' '+string+' ')
>>             print("string", "was found", count, "times")
>>
>> parser = argparse.ArgumentParser()
>> parser.add_argument("file_location")
>> parser.add_argument("language")
>> parser.add_argument("-b", "--count_both", default = False)
>> args = parser.parse_args()
>> ref_finder(args.file_location, args.language, args.count_both)
>> ~~~
>> {: .language-python}
> {: .solution}
{: .challenge}

> ## Extension challenge
> Update your program so that it tells you which versions of the software are references in the manuscript.
{: .challenge}

> ## Super challenge
> Update your program to use the structure of XML so that you only count occurences of 'R' or 'Python' in 
> the **reference** section of the manuscript.
>
> Is there a Python module that can help?
{: .challenge}

> ## Yet another challenge
> Run your program on a collection of manuscripts (can you find an XML manuscript repository?) tabulate your results. 
> Output your data to a new file, and visualise it in R.
{: .challenge}

{: .challenge}
