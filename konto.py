#!/usr/bin/env python3

import sys
import re
import io
import csv

import chardet

# Read stdin in binary mode
in_file_b = sys.stdin.buffer.read()

# Guess encoding
in_file_enc = chardet.detect(in_file_b)

# Attempt decoding
in_file_s = in_file_b.decode(in_file_enc["encoding"])

# Filter out garbage
csv_lines = []
for line in in_file_s.split("\n"):
    if re.match("^\d+/\d+/\d+;", line):
        csv_lines.append(line)
csv_s = "\n".join(csv_lines)

# Parse as a CSV file
reader = csv.reader(io.StringIO(csv_s), delimiter=";")

# Input file looks like this:
# Book, Cleared, Details, Debit, Credit, Currency

# Output should look like this:
# Date, Payee, Category, Memo, Outflow, Inflow

def convert(booked, cleared, details, debit, credit, currency):
    "Convert from Deutsche Bank format to YNAB format"
    # Remove any word with numbers in it
    # Horrible bodge, but better than nothing!
    payee = " ".join(
        s for s in details.split() if not any(c.isdigit() for c in s))
    return [booked, payee, "", details, debit, credit]

# Prepare to write to stdout
writer = csv.writer(sys.stdout)

# Convert all lines and output
for line in reader:
    writer.writerow(convert(*line))
