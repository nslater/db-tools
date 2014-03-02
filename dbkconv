#!/usr/bin/env python3

# Convert a DBK transaction CSV file to a YNAB account CSV file

import sys
import re
import io
import csv
import datetime

import chardet

def help():
    "Print usage information and exit"
    print("Usage: %s [-a|-c] < FILE" % sys.argv[0])
    sys.exit(1)

def error(msg):
    "Print error and exit"
    print("Error: %s" % msg)
    sys.exit(1)

# Grab our flag
try:
    flag = sys.argv[1].replace("-", "")
except:
    help()

def fmt_date(date):
    "Switch date format from American to European"
    date = datetime.datetime.strptime(date, "%m/%d/%Y")
    date = date.strftime("%d/%m/%Y")
    return date

def payee(str):
    "Get payee from transaction details"
    # Remove any word with numbers in it
    # Horrible bodge, but better than nothing!
    return " ".join(s for s in str.split() if not any(c.isdigit() for c in s))

def unsign(str):
    "Get unsigned number"
    # YNAB doesn't like signed values
    return str.replace("-", "").strip()

def convert_account(date, cleared, desc, debit, credit, cur):
    "Convert from Deutsche Bank account format to YNAB format"
    return [fmt_date(date), payee(desc), "", desc, unsign(debit), credit]

def convert_cc(date, cleared, payee, for_cur, for_debit, rate, debit, cur):
    "Convert from Deutsche Bank credit card format to YNAB format"
    return [fmt_date(date), payee, "", "", unsign(debit), ""]

# Check for valid flag and set up convert function
if flag == "a":
    convert = convert_account
elif flag == "c":
    convert = convert_cc
else:
    help()

# Check that stdin is attached
if sys.stdin.isatty():
    error("nothing attached to stdin")

# Read stdin in binary mode
in_file_b = sys.stdin.buffer.read()

# Guess encoding
in_file_enc = chardet.detect(in_file_b)

# Attempt decoding
in_file_s = in_file_b.decode(in_file_enc["encoding"])

# Filter out the garbage
csv_lines = []
for line in in_file_s.split("\n"):
    if re.match("^\d+/\d+/\d+;", line):
        csv_lines.append(line)
csv_s = "\n".join(csv_lines)

# Parse as a CSV file
reader = csv.reader(io.StringIO(csv_s), delimiter=";")

# Prepare to write to stdout
writer = csv.writer(sys.stdout)

# Write CSV header
writer.writerow(["Date", "Payee", "Category", "Memo", "Outflow", "Inflow"])

# Convert all lines and output
for line in reader:
    writer.writerow(convert(*line))
