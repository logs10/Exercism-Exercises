class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def row(self, index):
        # define row function
        row_list = list(self.matrix_string.split('\n'))
        done = []
        for row in row_list:
            done.append(row.split(' '))
        return [int(x) for x in done[index - 1]]

    def column(self, index):
        # define column function
        row_list = list(self.matrix_string.split('\n'))
        done = []
        for row in row_list:
            done.append(row.split(' '))
        unpacked = list(zip(*done))
        finish = []
        for i in unpacked:
            finish.append([int(x) for x in i])
        return finish[index - 1]


x = Matrix("89 1903 3\n18 3 1\n9 4 800")
