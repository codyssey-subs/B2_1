from datetime import datetime

class BudgetRepository:
    def __init__(self):
        self.budgets = {}

    def set_budget(self, month: str, amount: int):
        try:
            datetime.strptime(month, "%Y-%m")
        except:
            raise ValueError("month는 YYYY-MM 형식이어야 합니다.")

        if amount < 0:
            raise ValueError("amount는 0 이상이어야 합니다.")
        
        self.budgets[month] = amount

        return True

    def get_budget(self, month: str):
        try:
            datetime.strptime(month, "%Y-%m")
        except ValueError:
            raise ValueError("month는 YYYY-MM 형식이어야 합니다.")

        return self.budgets.get(month)

