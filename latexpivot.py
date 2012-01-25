#!/usr/bin/python

import sys
from collections import defaultdict

datafile = sys.argv[1]
instructionsfile = sys.argv[2]

# This should create the dictionary "data"
execfile(datafile)

# This should create the "datapoint" class.
execfile(instructionsfile)

# This is one easy way to make a sparse table, indexed by some random thing,
# without worrying about what the order of the keys.
# The key order is: page, row, column.
datatable = defaultdict(str)
pagenames = set()
rownames = set()
colnames = set()

for k in data.keys():
    rec = datapoint(k, data[k])

    if rec.show:
        pagenames.add(rec.page)
        rownames.add(rec.row)
        colnames.add(rec.column)
        datatable[(rec.page, rec.row, rec.column)] = rec.render()

sortedpages = sorted([p for p in pagenames])
sortedrows = sorted([r for r in rownames])
sortedcols = sorted([c for c in colnames])

max_col = min(len(sortedcols), table.max_col)
max_row = min(len(sortedrows), table.max_row)
max_page = min(len(sortedpages), table.max_page)

print "\\documentclass{article}"
print "\\usepackage{graphicx}"
print "\\usepackage{amsmath}"
print "\\usepackage{amssymb}"
print "\\usepackage{multirow}"
print "\\usepackage[a2paper, landscape, hmargin=1cm, vmargin=1cm]{geometry}"
print "\\begin{document}"
print "\\tiny"


# Page header
for pagenum in range(max_page):
    page = sortedpages[pagenum]
    print "%======================================================"
    print "\\par"
    print "\\resizebox{\\textwidth}{!}{"
    print "\\begin{tabular}{|c|" + ("c" * max_col) + "|}"
    print "\hline"
    print "&\\multicolumn{%d}{|c|}{"%max_col + table.page_heading % page + "}\\\\"

# column headers
    to_print = ""
    for colnum in range(max_col):
        col = sortedcols[colnum]
        to_print += "& " + table.col_heading % col 
    print to_print, "\\\\"
    print "\hline"

# table body lines - each line starts with a row header
    for rownum in range(max_row):
        row = sortedrows[rownum]
        to_print =  ""
        for colnum in range(max_col):
            col = sortedcols[colnum]
            to_print += "& " + datatable[(page, row, col)] 
        print table.row_heading % row, to_print, "\\\\"
    print "\\hline"
    print "\\end{tabular}"
    print "}"
 #   print "$"

    print "\\vspace{\\baselineskip}"

print "\end{document}"


