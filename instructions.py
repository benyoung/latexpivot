# Change this to alter the way keys and values get assigned
# rows, columns, and so forth.  
class table:
    row_heading = "$n = %d"
    col_heading = "$e_{%d}"
    page_heading = "Coefficient of $x^{%d}$ when $s=%d$"

    max_col = min(len(sortedcols), 15)
    max_row = min(len(sortedrows), 1000)
    max_page = min(len(sortedpages), 1000)

class datapoint:
    def __init__(self, key, value):
        (n, s, a, b) = key
        self.row = (n)
        self.column = (b)
        self.page = (s,a)

        self.show = true     # Change this to hide some entries

        if self.show:
            self.value = value

    def render(self):
        output = ""
        for (a,b) in self.value:
            output.append("$\\binom{%d}{%d}$" % (a,b))
        return output


