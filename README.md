# dbk-tools

Tools for working with Deutsche Bank file formats.

**NOTE**: I am no longer a customer of Deutsche Bank so I have no use for this tool. I will continue to accept pull requests but I do not intend to work on it any further. If someone wants to fork and maintain, I will happily update this README to point to the active fork.

## Introduction

Deutsche Bank (DBK) allows you to download your account transactions, but the file formats they use are poorly structured and impossible to use with standard personal accounting software.

I happen to use [You Need A Budget](http://www.youneedabudget.com/) (YNAB) for my personal finances, so these tools have been written to output files that YNAB understands.

If you're using a different tool, and would like to collaborate, I'd love to receive pull requests!

## dbkconv.py

### Purpose

Convert a DBK transaction CSV file to a YNAB account CSV file.

### Use

For normal account transactions, run:

```
./dbkconv.py Input_Transaction.csv > CleanTransaction.csv
```

This will output a reformatted CSV file for use with YNAB.

### Dependencies

- [pyenv](https://github.com/yyuu/pyenv) (optional, but I highly suggest using it)
- Python 3
- [chardet](https://pypi.python.org/pypi/chardet)

I recommend you use [Homebrew](https://github.com/Homebrew/homebrew) to install Python, and [pip](https://pypi.python.org/pypi/pip) to install chardet.
