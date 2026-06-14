class Table:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = []
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(0)
            self.data.append(row)

    def get_value(self, row, col):
        if row < 0 or row >= self.rows:
            return None
        if col < 0 or col >= self.cols:
            return None
        return self.data[row][col]

    def set_value(self, row, col, value):
        self.data[row][col] = value

    def n_rows(self):
        return self.rows

    def n_cols(self):
        return self.cols