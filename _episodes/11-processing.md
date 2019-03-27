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
> Hint: remember you will need to specify the 'path' to your file.
>
> > ## Solution
> > ~~~
> > with open('data/sample.fastq') as f:
> >     for line in f:
> >         print(line)
> > ~~~
> > {: .language-python}
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
> **line 1**: this is a 'header'. It gives us information about the machine
> the sample was sequenced on, and some other technical metadata about the 
> particular sequence read.
> **line 2**: this represents the actual DNA sequence. 
> **line 3**: repeat of the header information. Note, however, it starts with '+'.
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
> 
>
> > ## Solution
> > ~~~
> > with open('data/sample.fastq') as f:
> >     for line in f:
> >         if line[0] == '@'
> >             print(line)
> > ~~~
> > {: .language-python}
{: .challenge}
