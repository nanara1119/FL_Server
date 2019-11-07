import copy

import numpy as np

import logging
logger = logging.getLogger(__name__)

class FederatedServer:
    max_count = 10
    global_weight = None
    local_weights = []
    current_count = 0
    current_round = 0

    @classmethod
    def update(cls, local_weight):
        local_weights = copy.deepcopy(local_weight)
        cls.current_count += 1

        if cls.current_count % cls.max_count == 0:
            #cls.current_count = 0
            cls.current_round += 1
            cls.avg()
        else
            cls.local_weights.append(local_weight)

        logger.info("update round : {}, count: {}".format(cls.current_round, cls.current_count))
        #print("update count : {}".format(cls.current_count))

    @classmethod
    def avg(cls):
        if cls.global_weight is None:
            cls.global_weight = cls.local_weights.pop(0)

        for i in range(len(cls.local_weights)):
            for j in range(len(cls.local_weights[i])):
                temp = np.array(cls.local_weights[i][j], dtype=np.float32)
                cls.global_weight[j] += temp

        cls.global_weight = np.divide(cls.global_weight, cls.max_count) #   평균 계산
        cls.local_weights = []  #   다음 라운드를 위해 이전의 local weight 리스트 삭제
        print("global weight update : {}".format(cls.global_weight))

    @classmethod
    def get_avg(cls):
        return cls.global_weight

    @classmethod
    def get_current_count(cls):
        return cls.current_count

    @classmethod
    def get_current_round(cls):
        return cls.current_round