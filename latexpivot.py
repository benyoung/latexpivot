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

print "\\documentclass{article}"
print "\\usepackage{graphicx}"
print "\\usepackage{amsmath}"
print "\\usepackage{amssymb}"
print "\\usepackage{multirow}"
print "\\usepackage[a2paper, landscape, hmargin=1cm, vmargin=1cm]{geometry}"
print "\\begin{document}"
print "\\tiny"


# Page header
for pagenum in range(table.max_page):
    page = sortedpages[pagenum]
    print "%======================================================"
    print "\\par"
    print "\\resizebox{\\textwidth}{!}{"
    print "\\begin{tabular}{|c|" + ("c" * table.max_col) + "|}"
    print "\\multicolumn{*}{|c|}" + table.page_heading % page + "\\\\"
    print "\hline"

# column headers
    to_print = ""
    for colnum in range(table.max_col):
        col = sortedcols[colnum]
        to_print += "& " + table.column_heading % col 
    print to_print, "\\\\"
    print "\hline"

# table body lines - each line starts with a row header
    for rownum in range(table.max_row):
        row = sortedrows[rownum]
        to_print =  ""
        for colnum in range(table.max_col):
            col = sortedcols[colnum]
            to_print += "& " + datatable[(page, row, col)] 
        print table.row_heading % row, to_print, "\\\\"
    print "\\hline"
    print "\\end{tabular}"
    print "}"

print "\end{document}"


