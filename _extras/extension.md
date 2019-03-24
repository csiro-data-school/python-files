---
title: "Additional content"
---

## About Files

- Files store data on disk.
- They can be either text or binary files.
- Text files store text data in standard encodings that can be understood by
  many programs.
    - Often have name extensions that indicate the type of file, such as `.py`
      for Python scripts, `.csv` for comma-separated values data,
      and `.txt` for plain text files.
    - There are different encodings for text data that affect how the text is
      stored. Common encodings are ASCII and UTF-8. We will ignore encodings
      from here on.
- Binary files store binary data. Apart from conventions about the ordering of
  bytes on disk, binary files can have almost any internal structure.
    - There are some well documented binary file standards, such as PDF, and
      NetCDF.
    - However, frequently binary files can only be read by the software that
      created them.
- Python supports working with both binary and text files.
- We only explore working with text files here.

- Files are normally opened in text mode. By appending `"b"` to the mode,
  the file will be opened in binary mode.
