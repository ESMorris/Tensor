
class Tensor():

    def __init__(self, data, shape):
        self.data = data
        self.shape = shape
        self.shape_length = len(shape)
        self.data_length = len(data)


    def checking_shape_and_data(self):
        if self.shape_length == 0:
            return []

        for num in self.shape:
            if num < 0:
                return False

        for num in self.data:
            if type(num) != int and type(num) != float:
                return False

        return True


    def create_tensor(self):
        total_elements_in_matrix = 1

        for num in self.shape:
            total_elements_in_matrix *= num

        # 2d matrix
        if self.shape_length == 2:
            result = []
            count = 0

            for i in range(self.shape[0]):
                temp = []
                for j in range(self.shape[1]):
                    for num in range(count, count + 1):
                        if count >= self.data_length or count == total_elements_in_matrix:
                            temp.append(0)
                        else:
                            temp.append(self.data[num])
                        count += 1
                result.append(temp)
            return result

        # 3d matrix
        elif self.shape_length == 3:
            result = []
            count = 0

            for i in range(self.shape[0]):
                temp = []
                for j in range(self.shape[1]):
                    temp_j = []
                    for k in range(self.shape[2]):
                        for num in range(count, count + 1):
                            if count >= self.data_length or count == total_elements_in_matrix:
                                temp_j.append(0)
                            else:
                                temp_j.append(self.data[num])
                        count += 1
                    temp.append(temp_j)
                result.append(temp)
            return result

        # 4d matrix
        elif self.shape_length == 4:
            result = []
            count = 0

            for i in range(self.shape[0]):
                temp = []
                for j in range(self.shape[1]):
                    temp_j = []
                    for k in range(self.shape[2]):
                        temp_k = []
                        for l in range(self.shape[3]):
                            for num in range(count, count + 1):
                                if count >= self.data_length or count == total_elements_in_matrix:
                                    temp_k.append(0)
                                else:
                                    temp_k.append(self.data[num])
                            count += 1
                        temp_j.append(temp_k)
                    temp.append(temp_j)
                result.append(temp)
            return result
        else:
            return False







# Initial testing
shape0 = [2, 3, 2]
data0 = [0, 1, 2, 3, 4, 5, 0.1, 0.2, -3]

tensor0 = Tensor(data0, shape0)
if tensor0.checking_shape_and_data():
    print(tensor0.create_tensor())
else:
    print(tensor0.checking_shape_and_data())

print()

shape1 = [5, 2]
data1 = [0, 1, 2, 3, 4, 5, 0.1, 0.2, -3, -2, -1, 3, 2, 1]

tensor1 = Tensor(data1, shape1)
if tensor1.checking_shape_and_data():
    print(tensor1.create_tensor())
else:
    print(tensor1.checking_shape_and_data())

print()

shape2 = [2, 2, 2, 2]
data2 = [0, 1, 2, 3, 4, 5, 0.1, 0.2, -3, -2, -1, 3, 2, 1]

tensor2 = Tensor(data2, shape2)
if tensor2.checking_shape_and_data():
    print(tensor2.create_tensor())
else:
    print(tensor2.checking_shape_and_data())