import numpy as np


class FederatedServer:
    max_count = 10
    global_weight = None
    local_weights = []
    current_count = 0

    @classmethod
    def update(cls, local_weight):
        cls.current_count += 1

        if cls.current_count == cls.max_count:
            cls.avg()
        else:
            cls.local_weights.append(local_weight)

        print("update count : {}".format(cls.current_count))

    @classmethod
    def avg(cls):
        print("averaging : {} /// {}".format(cls.local_weights, cls.global_weight))

        if cls.global_weight is None:
            cls.global_weight = cls.local_weights.pop(0)

        for i in range(len(cls.local_weights)):
            for j in range(len(cls.local_weights[i])):
                cls.global_weight[j] += cls.local_weights[i][j]
        cls.global_weight = np.divide(cls.global_weight, 10)
        cls.local_weights = []
        print("avg : {}".format(cls.global_weight))

    @classmethod
    def get_avg(cls):
        return cls.global_weight
