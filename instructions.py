# This class contains parameters for how the table should be rendered.
class table:
    row_heading = "$n = %d$"
    col_heading = "$e_{%d}$"
    page_heading = "Coefficient of $x^{%d}$ when $s=%d$"

    max_col =  15
    max_row =  15
    max_page = 10

# This class defines how we should interpret the data, which data should
# be printed, and how we assign the data to rows, columns, and pages.
# The render method produces the actual latex code which goes in the 
# corresponding row and column of the table.
class datapoint:
    def __init__(self, key, value):
        (n, s, a, b) = key
        self.row = (n)
        self.column = (b)
        self.page = (s,a)

        self.show = True     # Change this to hide some entries
        self.value = value

    def render(self):
        output = ""
        for (a,b) in self.value:
            output += "$\\binom{%d}{%d}$" % (a,b)
        return output


