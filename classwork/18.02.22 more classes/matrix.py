class Matrix:
    valid = False
    def __init__(self, matrix):
        self.matrix = matrix

    def check(self, matrix):
        if len(matrix) == 0:
            print('Error. The matrix is empty')
        else:
            first_len = len(matrix[0])
            for i in matrix[1:]:
                if len(i) != first_len:
                    break
                else:
                    self.m = matrix
                    self.valid = True

    def transpose(self):
        if self.valid:
            new_m = [[]*len(self.matrix[0])]
            for i in range(len(self.matrix[0])):
                for j in range(len(self.matrix)):
                    new_m[i].append(self.matrix[j][i])
        else:
            return 'Error. The matrix is wrong'
        

