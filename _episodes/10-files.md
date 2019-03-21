---
title: "Working with Files"
teaching: 20
exercises: 30
questions:
- "How do I open a file in Python?"
- "How do I access the data or text inside an open file?"
objectives:
- "Open a text file."
- "Close a file when processing is finished."
- "Read lines of text from a file."
- "Open a text file for writing and write lines of text to it."
- "Understand the importance of closing files when finished with them."
- "Learn some useful patterns for line-by-line processing of text files with
  Python."
keypoints:
- "Files are opened with the `open()` function."
- "The `open()` function returns a file object."
- "Files need to be closed when they are no longer required by your program."
- "The `close()` method of the file object closes a file."
- "The `with` statement provides an elegant and safe way to automatically close
  your files."
- "Data can be read from text files a line at a time by the `readline()` file
  object method."
- "If you want to process each line of a text file in order, then iteration is
  useful."
- "Data can be written to a file with the `write()` file object method."
- "Patterns are common and repeatable recipes for common problems. The text file
  sequential processing pattern is simple, robust and efficient."

---

## Opening Files

To open a file, we use the `open()` function, which returns a **file** object:

~~~
my_file = open("my_data_file.txt", "r")
~~~
{: .language-python}

Here, 
* `my_file` is a variable name corresponding to the open file
* `open()` is *function* that takes two arguments

The first argument, `"my_data_file.txt"` is a *string* containing the filename.

The second argument, `"r"`, is also a string. This is the *mode* of the open 
file, and indicates how we want to use the file. The mode can be:
    - `"r"` : the file will only be read (this is the default)
    - `"w"` : only writing (an existing file with the same name will be erased)
    - `"a"` : for appending; any data written to the file is automatically added to the end
    - `"r+"`: both reading and writing.

> ## File found?
>
> Try and open one of the text files we downloaded:
> ~~~
> silly_quotes = open("monty_python.txt")
> ~~~
> {: .language-python}
> What is the `type` of `silly_quotes`?
>
> Now try and open a file that isn't there:
> ~~~
> missing = open("flying_circus.txt")
> ~~~
> {: .language-python}
> 
> What happended? What is the type of `missing`?
{: .challenge}

> ## What are some reasons that opening a file might fail?
> Try to think of some reasons that opening a file might fail. How common are
> they? Are there any particular situations that your program needs to handle?
>
> Often no special handling apart from displaying an error message is required,
> but thinking about these questions can help us write more robust code.
{: .discussion}

## Closing Files

Files need to be closed when they are no longer needed. One reason is that
computers can 'lock' files while they are open, to prevent unexpected
changes while the file is in use. For example, you don't want to accidently be 
editing a text file in word at the same time as you have a Python program 
automatically using its contents.

In Python, closing files involves a call to the `close()` method on the file
object. You can check the status of a file with the `closed` property:

~~~
my_file = open("my_data_file.txt", "r")
# do some processing
print(my_file.closed)  # should print False
my_file.close()
print(my_file.closed)  # should print True
~~~
{: .language-python}

## Reading from a File

Once we have created a file object using `open()`, we can access lines of the file
using the `readline()` method.

* `readline()` reads a single line from the file as a `string`
* repeated calls to `readline()` will return subsequent lines of the file, in order, until the end of the file is
reached.

> ## When will it end?
> `readline()` leaves the newline character (`\n`) at the end of the string, and is
> only omitted on the last line of the file. This means that the end of the file
> is indicated when `readline()` returns an empty string. This allows blank lines in the file
> to be indicated by the string `"\n"`.
{: .callout}

> ## Open, shut them
> 
> Using Python:
> 1. Open a file on your computer, and store the file object in a variable
> 2. Use the readline() method to print the first line of your file.
> 3. Close your file
> 4. Use the `closed` property to check whether your file is really closed.
>
{: .challenge}

> ## while `line`
> Examine the following code:
> 
> ~~~
> data_file = open("observation_data.csv", "r")
> data_list = []
> header = data_file.readline()
> line = data_list.readline()
> while line:
>     data_list.append(line)
>     line = data_list.readline()
> ~~~
> {: .language-python}
>
> What does this code do? Write out an English language explanation 
> of each line of code. Discuss you explanation with the person sitting next to you.
>
{: .language-python}

> ## Print some text
>
> In this exercise, write some Python code to read lines of text from
> `a_few_lines_of_text.txt` and print them one at a time. 
> Your program should close the file when there are no more lines.
>
> You should see this output:
>
> ~~~
> This file contains just a few lines of text.
>
> Not a lot.
>
> Just a few.
> ~~~
> {: .source}
>
> Now, modify your code so it also prints out the line number before the line's text. 
>
> You should see this output:
>
> ~~~
> 0 This file contains just a few lines of text.
>
> 1 Not a lot.
>
> 2 Just a few.
> ~~~
> {: .source}
>
> > ## Solution
> > One possible solution is:
> >
> > ~~~
> > f = open("a_few_lines_of_text.txt")
> > count = 0  # initialise the line count
> > line = f.readline()  # read the first line before entering the loop
> > while line:  # readline() returns an empty string at end of file
> >     print(count, line)
> >     count = count + 1
> >     line = f.readline()
> > f.close()
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}

> ## Why all the blank lines?
> In the previous exercise, the input file does not contain blank lines, so where are they coming from?
> The answer is the `print` function. `print` is adding a newline character to the string read from the
> file, which already contains a newline character.
{: .callout }

`file` objects are also *iterable*, meaning we can iterate over all the lines, just like we can iterate through elements of a `list` object, or characters in a `string` object. This is memory efficient, fast, and leads to simple code:
~~~
for line in f:
    print(line)
~~~
{: .language-python}

> ## Using file iteration
> Update your previous program to use the file iteration approach. You should
> see the same output.
> > ## Solution
> > ~~~
> > f = open("a_few_lines_of_text.txt")
> > count = 0  # initialise the line count
> > for line in f:
> >     print(count, line)
> >     count = count + 1
> > f.close()
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}

Iterating a collection where both the data and the index (the line count in our
case) are required is a very common operation, and Python provides the
[`enumerate()`][enumerate-function] function
for just this purpose.

Let's see how this works for a list first:

~~~
my_list = ['a','b','c','d','e']
for index, value in enumerate(my_list):
    print(index, value)
~~~
{: .language-python}

> ## Update your text reading program to use `enumerate`
> Update your previous program to use the `enumerate()` function. You should
> see the same output.
> > ## Solution
> > ~~~
> > f = open("a_few_lines_of_text.txt")
> > for count, line in enumerate(f):
> >     print(count, line)
> > f.close()
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}

## Writing to a File

Text can be written to a text file that has been opened for writing with the
`write()` method on the file object:
~~~
f = open("my_text.txt", "w")
f.write("This is a line of text")
f.close()
~~~
{: .language-python}

> ## Write to a file
> 
> Use Python to make a new file and save some text:
> ~~~
> f = open("new_file", "w")
> f.write("Some initial text")
> f.write("A second line of text")
> f.close()
> ~~~
> Now, open your new file using your favourite text editor. 
> Is the content what you expect? If not, how would you fix it?
>
> Open your file again and try this fix:
> ~~~
> f = open("new_file", "w")
> f.write("Line number one\n")
> f.write("Line number two\n")
> f.close()
> ~~~
> {: .language-python}
> Open it again with your favourite text editor. What happened to your original text?
{: .challenge}

> ## `write()` and line breaks
> Note that `write()` does not add a newline to the end. 
> If you want a newline or carriage return, you need to add it yourself
> using the string `\n`.
{: .callout}

## File Opening Recipe: Context Managers

It is 'best practice' to always open files using the [`with`][with-statement] statement.

`with` automatically closes your file as soon as your code is finished with it. Just like 
the `for` and `if` statements we have already encountered, `with` ends with a colon `:` 
character, and all the code that belongs to it is indented. For example:

~~~
with open("a_file.txt", "w") as f:
    for line in f:
        print(line)
        
print(f.closed)
~~~
{: .language-python}

In addition to being simpler, this approach is also safer. The file will
always be closed when the indented code block is finished,
even when unexpected exceptions or other errors occur.

This leads us to a robust and useful pattern for sequentially processing every
line in a text file:
~~~
with open("a_file.txt", "w") as f:
    for line in f:
        # process the line
~~~
{: .language-python}

## Putting it all together
> ## Reading and writing files at the same time
> In this exercise, write a Python program to read lines of text from
> `a_few_lines_of_text.txt`. For each line, write the line number followed by `": "`
> and then the input text to a separate file called "numbered_lines_of_text.txt".
> For example, if the third line of text is
> "this is the third line" then the third line of
> the new file would be "2: this is the third line".
>
> Your program should close both files when finished, including after any errors
> are encountered.
> 
> Hint: `with` can be used to safetly open multiple files at once, e.g.
> `with open("a_file") as file_one, open("another_file) as file_two:` ...
>
> > ## Solution
> > ~~~
> > with open("../data/a_few_lines_of_text.txt") as f_in, open("numbered_lines_of_text.txt", "w") as f_out:
> >     for count, line in enumerate(f_in):
> >         f_out.write(count + ': ' + line + '\n'))
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}


## More Information

For more information on basic file IO in Python, please refer to the [Reading and
 Writing Files][python-tutorial-files] section of the Python documentation.

{% include links.md %}

[python-tutorial-files]: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
[with-statement]: https://docs.python.org/3/reference/compound_stmts.html#with
[enumerate-function]: https://docs.python.org/3/library/functions.html#enumerate
