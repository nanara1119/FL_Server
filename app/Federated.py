import copy

import numpy as np

import logging
logger = logging.getLogger(__name__)

class FederatedServer:
    max_count = 2
    global_weight = None
    local_weights = []
    current_count = 0
    current_round = 0

    def __init__(self):
        print("Federated init")

    """
        개별 Client로 부터 전달받은 weight를 리스트에 저장
        지정된 갯수의 weight를 전달받으면 average를 수행  
    """
    @classmethod
    def update(cls, local_weight):
        weight_list = []
        for i in range(len(local_weight)):
            temp = np.array(local_weight[i])
            weight_list.append(temp)

        cls.current_count += 1
        cls.local_weights.append(weight_list)

        if cls.current_count == cls.max_count:
            cls.avg()
            cls.current_count = 0
            cls.current_round += 1
            logger.info("----------------------------------------")
            logger.info("current round : {}".format(cls.current_round))
            logger.info("----------------------------------------")

    """
        전체 client로부터 전달받은 weight들을 average함        
    """
    @classmethod
    def avg(cls):
        temp_list = []

        #   weight의 shape를 모름, 하나를 꺼내어 사용
        temp_weight = cls.local_weights.pop()

        #   계산하기 쉽도록 numpy array 형식으로
        for i in range(len(temp_weight)):
            temp = np.array(temp_weight[i])
            temp_list.append(temp)

        temp_list = np.array(temp_list)

        # 각 local_weight의 layer별 weight들을 더함
        '''
            np.average() / np.mean() 
        '''
        for i in range(len(cls.local_weights)):
            for j in range(len(cls.local_weights[i])):
                temp = np.array(cls.local_weights[i][j])
                temp_list[j] += temp

        # 새로운 global weight
        cls.global_weight = np.divide(temp_list, cls.max_count)
        cls.local_weights = []

    @classmethod
    def get_avg(cls):
        """ 현재 global weight 조회"""
        return cls.global_weight

    @classmethod
    def get_current_count(cls):
        """ 현재 local weight 갯수 조회 """
        return cls.current_count

    @classmethod
    def get_current_round(cls):
        """ 현재 round number 조회 """
        return cls.current_round

    @classmethod
    def set_client_count(cls, count):
        """  FL 참여 client 갯수 설정 (admin) """
        cls.max_count = count

    @classmethod
    def get_client_count(cls):
        """  FL 참여 client 갯수 조회 (admin) """
        return cls.max_count

    @classmethod
    def reset_parm(cls):
        """ FL 환경 설정 변수 초기화 (admin)"""
        cls.max_count = 3
        cls.global_weight = None
        cls.local_weights = []
        cls.current_count = 0
        cls.current_round = 0