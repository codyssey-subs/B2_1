import sys

def main():
    parser = create_parser()

    budget_repository = BudgetRepository()
    category_repository = CategoryRepository()
    transaction_repository = TransactionRepository()

    service = BudgetService(
        budget_repository,
        category_repository,
        transaction_repository
    )
    
    try:
        args = parser.parse_args()
    except SystemExit as e: #수정필요!!!!
        sys.exit(e.code)

    if args.command == "add":
        pass
    elif args.command == "":
        pass
    elif args.command == "":
        pass
    elif args.command == "":
        pass
    else:
        print("알 수 없는 명령어")
        sys.exit(1)

    sys.exit(0)

if __name__ == "__main__":
    main()