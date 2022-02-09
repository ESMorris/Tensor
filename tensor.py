from pprint import pprint
from unittest import result


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
        print(total_elements_in_matrix)

        # 2d matrix
        if self.shape_length == 2:
            result = []
            count = 0

            for i in range(self.shape[0]):
                temp = []
                for j in range(self.shape[1]):
                    for num in range(count, count + 1):
                        if count >= len(self.data) or count == 10:
                            temp.append(0)
                        else:
                            temp.append(self.data[num])
                        count += 1
                result.append(temp)
            return result

        # 3d matrix
        # 4d matrix







# Initial testing
# shape = [2, 3, 2]
# data = [0, 1, 2, 3, 4, 5, 0.1, 0.2, -3]

shape = [5, 2]
data = [0, 1, 2, 3, 4, 5, 0.1, 0.2, -3, -2, -1, 3, 2, 1]

tensor = Tensor(data, shape)
if tensor.checking_shape_and_data():
    print(tensor.create_tensor())
else:
    print(tensor.checking_shape_and_data())





# distance = [[[ 0 for k in range(shape0[2])] for j in range(shape0[1])] for i in range(shape0[0])]

# shape = [5, 2]
# data = [0, 1, 2, 3]



# distance = []
# count = 0
# for i in range(shape[0]):
#     temp = []
#     for j in range(shape[1]):
#         for num in range(count, count + 1):
#             if count >= len(data) or count == 10:
#                 temp.append(0)
#             else:
#                 temp.append(data[num])
#             count += 1
#     distance.append(temp)



# print(distance)
# print()


# # This works for test 1
# for i in range(shape0[0]):
#     for j in range(shape0[1]):
#         for k in range(shape0[2]):
#             for num in range(count, count + 1):
#                 if count >= len(data0) or count == 12:
#                     break
#                 else:
#                     distance[i][j][k] = data0[num]
#             count += 1

# # # Test 2 with 


# pprint(distance)