

class Transaction:
    def __init__(self):
        pass
    def __init__(self, date, type, category, amount, memo, tags):
        self.__id
        self.type = type #income/expense
        self.date = date #YYYY-MM-DD
        self.amount = amount #양수
        self.category = category
        self.memo = memo #선택
        self.tags = tags #선택, 다중?[]