#!/usr/bin/python

import sys
from collections import defaultdict

if 1 :
    data = {}
#    execfile("datafile") # creates data2
    execfile("newdata")
    data2 = data
else: 
    execfile("data2.py")
# This is one easy way to make a sparse table, indexed by some random thing,
# without worrying about what the order of the keys.
# The key order is: page, row, column.
datatable = defaultdict(list)
pagenames = set()
rownames = set()
colnames = set()

for k in data2.keys():
    (n,s,a,b) = k;
# We now have the following data:(n,s,a,b,c,qnum,offset)

# First record the important column, namely b= s-a for all n,s,a
    if b==s-a:
        for c in range(len(data2[k][1])):
            (qnum, qoffset) = data2[k][1][c]
            pagenames.add((a, "column"))
            rownames.add(s)
            colnames.add(n)
            datatable[((a, "column"), s, n)].append((c,qnum,qoffset))

# Then, record the important main diagonal, namely n = s+1+t, b=s-a+t
# which is the same as n-1 = b+a
    if n-1 == b+a:
        for c in range(len(data2[k][1])):
            (qnum, qoffset) = data2[k][1][c]
            pagenames.add((a, "diagonal"))
            rownames.add(s)
            colnames.add(n)
            datatable[((a, "diagonal"), s, n)].append((c,qnum,qoffset))

sortedpages = sorted([p for p in pagenames])
sortedrows = sorted([r for r in rownames])
sortedcols = sorted([c for c in colnames])

# Call this to write something or other in a latex table
def entry_to_string(record):
    if(record == []):
        return "& "
    else:
        to_print = "& \\rule{0in}{10pt}"
        printables = []
        for (c,qnum,qoffset) in record:
            printables.append( "\\raisebox{%d pt}{$\\stackrel{%s}{%s}$}" % (c * 2, qnum, qoffset)) 
        return to_print + "".join(printables)

print "\\documentclass{article}"
print "\\usepackage{graphicx}"
print "\\usepackage{amsmath}"
print "\\usepackage{amssymb}"
print "\\usepackage{multirow}"
print "\\usepackage[a2paper, landscape, hmargin=1cm, vmargin=1cm]{geometry}"
print "\\begin{document}"
print "\\tiny"

max_col = min(len(sortedcols), 15)
max_row = min(len(sortedrows), 1000)
max_page = min(len(sortedpages), 1000)

# Page header
for pagenum in range(max_page):
    page = sortedpages[pagenum]
    print "%======================================================"
    print "\\par"
#    print "$"
    print "\\resizebox{\\textwidth}{!}{"
    print "\\begin{tabular}{|c|" + ("c" * max_col) + "|}"
    print "\\multicolumn{6}{|c|}{Coefficients of $x^{%d}$ on the important %s}\\\\\n" % (page[0], page[1])
    print "\hline"

# column headers
    to_print = ""
    for colnum in range(max_col):
        col = sortedcols[colnum]
        to_print += " & $n=%d$ " % col 
    print "n", to_print, "\\\\"
    print "\hline"

# table body lines - each line starts with a row header
    for rownum in range(max_row):
        row = sortedrows[rownum]
        to_print =  ""
        for colnum in range(max_col):
            col = sortedcols[colnum]
            record = datatable[(page, row, col)] # a list of tuples
            to_print += entry_to_string(record)
        print "s=%d"%(row), to_print, "\\\\"
    print "\hline"
    print "\\end{tabular}"
    print "}"
 #   print "$"

print "\end{document}"


