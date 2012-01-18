instructions = {
    "keys": ("n", "s", "a", "b"),
    #"change_variables": {
    #    "t": "n-a"
    #},
    "rows": ("n"),
    "columns": ("b"),
    "pages": ("a","s"),

    "row headings":  "$n=%d$",
    "col headings":  "$e_{%d}$",
    "page headings": "Coefficient of $x^{%d}$ when $s=%d$",
    #"filters": [
    #    "s == a",
    #]
}

def entry_to_string(record):
    output = ""
    for (a,b) in record:
        output += "\\binom{%d}{%d}" % (a,b)
    return output
