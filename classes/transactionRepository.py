

class TransactionRepository:
    def __init__(self):
        self.transactions = []
        self.__next_id = 1

    def add(self, transaction: Transaction):
        transaction.id = self.next_id
        self.next_id += 1

        self.transactions.append(transaction)
        return transaction

    #yeild 사용 필요!!!
    def stream_all(self):
        return self.transactions.copy() #안전을 위해 리스트 전체를 복사해서 전달

    def update(self, transaction_id: int, data: dict):
        transaction = self.find_by_id(transaction_id)

        if transaction is None:
            return False

        if "date" in data:
            transaction.date = data["date"]
        if "type" in data:
            transaction.type = data["type"]
        if "category" in data:
            transaction.category = data["category"]
        if "amount" in data:
            transaction.amount = data["amount"]
        if "memo" in data:
            transaction.memo = data["memo"]
        if "tags" in data:
            transaction.tags = data["tags"]

        return True

    def delete(self, transaction_id: int):
        transaction = self.find_by_id(transaction_id)

        if transaction is None:
            return False

        self.transaction.remove(transaction)

        return True

    def find_by_id(self, transaction_id: int):
        for transaction in self.transactions:
            if transaction.id == transaction_id:
                return transaction

        return None
