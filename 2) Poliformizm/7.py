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

    def delete_row(self, row):
        new_data = []
        for i in range(self.rows):
            if i != row:
                new_data.append(self.data[i])
        self.data = new_data
        self.rows = self.rows - 1

    def delete_col(self, col):
        new_data = []
        for i in range(self.rows):
            new_row = []
            for j in range(self.cols):
                if j != col:
                    new_row.append(self.data[i][j])
            new_data.append(new_row)
        self.data = new_data
        self.cols = self.cols - 1

    def add_row(self, row):
        new_row = []
        for j in range(self.cols):
            new_row.append(0)
        new_data = []
        for i in range(self.rows):
            if i == row:
                new_data.append(new_row)
            new_data.append(self.data[i])
        if row == self.rows:
            new_data.append(new_row)
        self.data = new_data
        self.rows = self.rows + 1

    def add_col(self, col):
        new_data = []
        for i in range(self.rows):
            new_row = []
            for j in range(self.cols):
                if j == col:
                    new_row.append(0)
                new_row.append(self.data[i][j])
            if col == self.cols:
                new_row.append(0)
            new_data.append(new_row)
        self.data = new_data
        self.cols = self.cols + 1