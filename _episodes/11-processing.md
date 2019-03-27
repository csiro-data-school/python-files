---
title: file processing
---

Python excells at processing text files. This is because:

* Python reads files line-by-line, one at a time
* Each line is read in as a `string`
* Strings are easy to manipulate in Python, using functions, methods, and indexing

In this lesson, we will workshop an example using an input data file 
in [fastq](https://en.wikipedia.org/wiki/FASTQ_format) format.

To start, download your [sample.fastq]({{ page.root }}/data/sample.fastq) and 
save it into your `data` directory.

> ## Reading in your file
> 
> Using the `with` statement, the `open` function, and a `for` loop,
> open this file and print its contents.
>
> > Hint 
> > Remember you will need to specify the 'path' to your file.
> {: .solution}
>
> > ## Solution
> > ~~~
> > with open('data/sample.fastq') as f:
> >     for line in f:
> >         print(line)
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}

> ## fastq format
> fastq files are plain text files that are used to store DNA sequences.
> After DNA has been extracted from a biological sample, the concentrated
> DNA is prepared and placed into a 'sequencing' machine. The machine
> 'reads' the DNA sequence, letter-by-letter (or, more accurately, base-by-base).
> However, it can only read a small number of bases in a row, let's say 36. 
> The machine spits out millions of these short, 36 base pair long reads. 
> Researchers receive these DNA 'reads' in the form of a fastq file. 
> 
> Within a fastq file, each short 'read' takes up four lines:
> 
> ~~~
> @SRR098032.1.1 HWI-EAS216:4:1:0:1752 length=36
> TAACGGTTATTCTGCGGTTGAGATTGTTGGGGCNGC
> +SRR098032.1.1 HWI-EAS216:4:1:0:1752 length=36
> B@<:?<>=;?>8</7<83<66559<44:898/%!%=
> ~~~
> {: .output}
>
> **line 1**: this is a 'header'. It gives us information about the machine
> the sample was sequenced on, and some other technical metadata about the 
> particular sequence read.
>
> **line 2**: this represents the actual DNA sequence. 
>
> **line 3**: repeat of the header information. Note, however, it starts with '+'.
>
> **line 4**: quality scores. Sequencing machines make mistakes, the technology is 
> not perfect. Each character in this line represents a quality 'score'. 
>
> We use processing a fastq file as an example in this lesson, not because everyone
> needs to know how to process fastq files, but because of this unique structure. 
> It demonstrates a case where our data is not neatly structured into a table, and 
> where each 'entry' in our data is made up of multiple lines.
{: .callout}

> ## Selecting lines
> 
> You can read in and print your fastq file with the following code:
> 
> ~~~
> with open('data/sample.fastq') as f:
>     for line in f:
>         print(f)
> ~~~
> {: .language-python}
> 
> Modify this code, so that only 'header' lines are printed.
>
> > ## Hint
> > You could use an `if` statement.
> {: .solution}
>
> > ## Solution
> > ~~~
> > with open('data/sample.fastq') as f:
> >     for line in f:
> >         if line[0] == '@' and len(line) > 36:
> >             print(line)
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}

We know lines are read in as strings, which means we can perform any string operations on them.

> ## line.split()
> What does this program do?
> ~~~
> with open('data/sample.fastq') as f:
>     for line in f:
>         if line[0] == '@' and len(line) > 36:
>            line.split(' ')
> ~~~
> {: .language-python}
> 
> Read the documentation for line.split()
{: .challenge}

> ## header fields
>  
> In our example, headers have the structure:
> ~~~
> @SRR098032.1.1 HWI-EAS216:4:1:0:1752 length=36
> ~~~
> {: .output}
>
> We can see three 'fields', which are separated by 
> spaces. The first of these is a unique identifier
> for the sequencing machine. All sequencing machines around
> the world have one, a bit like the sequencing machine's 
> barcode.
>
> The second 'field' is a bit more complicated. 
> When DNA is loaded into a sequencing machine, 
> it is first placed on a disposable 'flow cell', which is 
> a bit like a glass slide. This second field tells us the 
> physical location of the DNA on the 'flow cell'. This is 
> of the form `flow-cell ID:lane:tile:x-coord:y-coord`
> 
> > # read metadata
> > why might it be important to record the phyical location 
> > of a sequence read on a flow cell?
> {: .discussion}
>
> The final field is more intuitive; it simply tells us that the
> length of the read is 36 bases. 
{: .callout}

> ## line.split()
> Modify the code below, so that your program only prints out the flowcell information.
> ~~~
> with open('data/sample.fastq') as f:
>     for line in f:
>         if line[0] == '@' and len(line) > 36:
>            line.split(' ')
> ~~~
> {: .language-python}
> 
> Your expected output is:
> ~~~
> HWI-EAS216:4:1:0:1752
> HWI-EAS216:4:1:0:963
> HWI-EAS216:4:1:0:554
> HWI-EAS216:4:1:0:1229
> HWI-EAS216:4:1:0:475
> HWI-EAS216:4:1:0:834
> HWI-EAS216:4:1:0:1203
> HWI-EAS216:4:1:0:1123
> HWI-EAS216:4:1:0:1642
> HWI-EAS216:4:1:0:603
> HWI-EAS216:4:1:0:904
> HWI-EAS216:4:1:0:1572
> HWI-EAS216:4:1:0:1713
> ~~~
> {: .output}
{: .challenge}

> ## Challenge
> Further modify the program to print out *only* the coordinates. 
>
> Expected output:
> ~~~
> 0 1752
> 0 963
> 0 554
> 0 1229
> 0 475
> 0 834
> 0 1203
> 0 1123
> 0 1642
> 0 603
> 0 904
> 0 1572
> 0 1713
> ~~~
> {: .output}
{: .challenge}

## Writing output from one file to another

As a reminder, our general recipe for writing to a file is:
~~~
with open('data/out.txt') as f:
    f.write('some text')
~~~
{: .language-python}

How can we open one file, process its contents, and the processed contents to another file?

Chaining `open` functions after a `with` statement works:

~~~
with open('data/sample.fastq') as in_file, open('data/headers.txt', 'w') as out_file:
    for line in in_file:
        if line[0] == '@' and len(line[0]) > 36:
            out_file.write(line)
~~~
{: .language-python}

> ## write metadata
> 
> 1. Modify the example above so that only the flowcell metadata field is written out.
> Call your new file 'metadata.txt'
> 2. Modify the example again, makind a new file 'metadata.csv' where the individual 
> components of the metadata are separated by `,` the contents of your new file 
> should look like:
>    ~~~
>    HWI-EAS216, 4, 1, 0, 1752
>    HWI-EAS216, 4, 1, 0, 963
>    HWI-EAS216, 4, 1, 0, 554
>    HWI-EAS216, 4, 1, 0, 1229
>    HWI-EAS216, 4, 1, 0, 475
> ~~~
> {: .language-python}
> 3. CHALLENGE: Modify it again, making the file 'metadata.tsv'. The fields should now be 
> tab separated. Use the string `join()` method in your solution.
{: .challenge}

    
