from pprint import pprint



class Tensor():

    def __init__(self, data, shape) -> list:
        self.data = data
        self.shape = shape
        



# Initial testing
shape0 = [2, 3, 2]
data0 = [0, 1, 2, 3, 4, 5, 0.1, 0.2, -3]
count = 0



distance = [[[ 0 for k in range(shape0[2])] for j in range(shape0[1])] for i in range(shape0[0])]



print(distance)
print()


# This works for test 1
for i in range(shape0[0]):
    for j in range(shape0[1]):
        for k in range(shape0[2]):
            for num in range(count, count + 1):
                if count >= len(data0) or count == 12:
                    break
                else:
                    distance[i][j][k] = data0[num]
            count += 1

# # Test 2 with 


pprint(distance)