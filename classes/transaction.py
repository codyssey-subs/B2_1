from datetime import datetime

class Transaction:
    def __init__(self, transaction_id: str, date: str, transaction_type: str, category: int, amount: int, memo="", tags=None):
        if transaction_type not in ["income", "expense"]:
            raise ValueError("type은 income 또는 expense만 가능합니다.")
        if amount <= 0:
            raise ValueError("amount는 양수여야 합니다.")
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("date는 YYYY-MM-DD 형식이어야 합니다.")
        self.__id = transaction_id
        self.type = transaction_type #income/expense
        self.date = date #YYYY-MM-DD
        self.amount = amount #양수
        self.category = category
        self.memo = memo #선택
        if tags is None or tags == "":
            self.tags = []
        else:
            self.tags = [tag.strip() for tag in tags.split(",") if tag.strip()]