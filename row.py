class Row:
    def __init__(self, cols, line):
        for col, _ in enumerate(line):
            try:
                setattr(self, cols[col], line[col])
            except IndexError:
                continue
