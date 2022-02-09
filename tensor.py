from pprint import pprint


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
        print("Hello from tensor!")







# Initial testing
shape = [2, 3, 2]
data = [0, 1, 2, 3, 4, 5, 0.1, 0.2, -3]
# count = 0

tensor = Tensor(data, shape)
if tensor.checking_shape_and_data():
    tensor.create_tensor()
else:
    print(tensor.checking_shape_and_data())





# distance = [[[ 0 for k in range(shape0[2])] for j in range(shape0[1])] for i in range(shape0[0])]



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