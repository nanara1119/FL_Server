import copy

import numpy as np


class FederatedServer:
    max_count = 10
    global_weight = None
    local_weights = []
    current_count = 0

    @classmethod
    def update(cls, local_weight):
        cls.current_count += 1

        if cls.current_count % cls.max_count == 0:
            cls.avg()
        else:
            cls.local_weights.append(local_weight)

        print("update count : {}".format(cls.current_count))

    @classmethod
    def avg(cls):
        print("averaging : ", len(cls.local_weights[0]), len(cls.local_weights[1]))

        if cls.global_weight is None:
            cls.global_weight = cls.local_weights.pop(0)

        print("222 : ", type(cls.local_weights), len(cls.local_weights))
        print("333 : ", type(cls.local_weights[0]), len(cls.local_weights[0]), type(cls.local_weights[0][0]), len(cls.local_weights[0][0]))
        print("444 : ", type(cls.local_weights[1]), len(cls.local_weights[1]))

        for i in range(len(cls.local_weights)):
            for j in range(len(cls.local_weights[i])):
                temp = np.array(cls.local_weights[i][j])
                #cls.global_weight[j] += cls.local_weights[i][j]
                cls.global_weight[j] += temp

        print("555 : ", type(cls.global_weight), len(cls.global_weight), type(cls.global_weight[0]), len(cls.global_weight[1]))
        cls.global_weight = np.divide(cls.global_weight, 10)
        cls.local_weights = []
        print("avg : {}".format(cls.global_weight))



    @classmethod
    def get_avg(cls):
        return cls.global_weight
