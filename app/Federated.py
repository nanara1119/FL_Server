class FederatedServer:
    max_count = 10
    global_weight = []
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
        print("averaging : {}".format(cls.local_weights))

    @classmethod
    def get_avg(cls):
        return cls.global_weight
