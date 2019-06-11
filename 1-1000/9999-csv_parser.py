"""
CSV parser
"""


class SolutionClass:
    def parseCsvLine(self, line):
        fields = []
        field = ''
        inQuote = False
        i = 0

        while i < len(line):
            c = line[i]
            if inQuote:
                if c != '"':
                    field += c
                elif i + 1 < len(line) and line[i + 1] == '"':
                    field += '"'
                    i += 1
                else:
                    inQuote = False
                    fields.append(field)
                    field = ''
                    while i < len(line) and line[i] != ',':
                        i += 1
            else:
                if c == '"':
                    inQuote = True
                elif c == ',':
                    fields.append(field.strip())
                    field = ''
                elif c != ' ' or field:
                    field += c
            i += 1

        if field:
            fields.append(field)

        return '|'.join(fields)

# Space: O(1)
# Time: O(n^3)


if __name__ == "__main__":
    s = 'John,Smith,[email]john.smith@gmail.com[/email],Los Angeles,1'
    print(SolutionClassDynamicProgramming().longestPalindrome(s))
