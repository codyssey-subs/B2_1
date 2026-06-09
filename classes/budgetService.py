class BudgetService:
    def __init__(self, budget_repository, category_repository, transaction_repository):
        self.budget_repository = budget_repository
        self.category_repository = category_repository
        self.transaction_repository = transaction_repository

    def add_transaction(self, date, transaction_type, category, amount, memo="", tags=""):
        if not self.category_repository.is_exist(category):
            raise ValueError("존재하지 않는 카테고리입니다.")
        
        transaction = Transaction(
            transaction_id=None,
            date=date,
            transaction_type=transaction_type,
            category=category,
            amount=amount,
            memo=memo,
            tags=tags
        )
        return self.transaction_repository.add(transaction)

    def list_transactions(self, limit: int =10):
        transactions = self.transaction_repository.stream_all()
        return transactions[:limit]

    def search_transactions(self, filters: dict):
        transactions = self.transaction_repository.stream_all()

        result = []

        for transaction in transactions:
            if "from" in filters and filters["from"]:
                if transaction.date < filters["from"]:
                    continue
            if "to" in filters and filters["to"]:
                if transaction.date > filters["to"]:
                    continue
            if "category" in filters and filters["category"]:
                if transaction.category != filters["category"]:
                    continue
            if "type" in filters and filters["type"]:
                if transaction.type != filters["type"]:
                    continue
            if "q" in filters and filters["q"]:
                if filters["q"] not in transaction.memo:
                    continue
            if "tag" in filters and filters["tag"]:
                if filters["tag"] not in transaction.tags:
                    continue

            result.append(transaction)

        return result

    def summarize_month(self, month: str, top: int):
        transactions = self.transaction_repository.stream_all()

        month_transactions = []

        for transaction in transactions:
            if transaction.date.startswith(month):
                month_transactions.append(transaction)

        if len(month_transactions) == 0:
            return None

        total_income = 0
        total_expense = 0
        category_expenses = {}

        for transaction in month_transactions:
            if transaction.type == "income":
                total_income += transaction.amount

            elif transaction.type == "expense":
                total_expense += transaction.amount

                category = transaction.category
                category_expenses[category] = category_expenses.get(category, 0) + transaction.amount

        balance = total_income - total_expense
        budget = self.budget_repository.get_budget(month)

        if budget == 0:
            usage_rate = 0
        else:
            usage_rate = total_expense / budget * 100

        top_expenses = sorted(
            category_expenses.items(),
            key=lambda item: item[1],
            reverse=True
        )[:top]

        print_summary(month, total_income, total_expense, balance, budget, usage_rate, top_expenses)

    def update_transaction(self, transaction_id: str, data: dict):
        if "category" in data:
                if not self.category_repository.is_exist(data["category"]):
                    raise ValueError("존재하지 않는 카테고리입니다.")
    
            return self.transaction_repository.update(transaction_id, data)

    def delete_transaction(self, transaction_id: str):
        return self.transaction_repository.delete(transaction_id)


    def print_summary(month, total_income, total_expense, balance, budget, usage_rate, top_expenses):
        if summary is None:
            print("데이터 없음")
            return
        print(f"총 수입: {summary['total_income']}원")
        print(f"총 지출: {summary['total_expense']}원")
        print(f"잔액: {summary['balance']}원")
        print(f"예산: {summary['budget']}원 (사용률 {summary['usage_rate']:.1f}%)")
        print()

        print(f"지출 TOP {len(summary['top_expenses'])}")

        for index, (category, amount) in enumerate(summary["top_expenses"], start=1):
            print(f"{index}) {category} {amount}원")