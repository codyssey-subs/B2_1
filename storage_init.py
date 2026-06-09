#프로그램이 시작될 때마다 저장소를 검사하고, 없으면 자동 생성

from pathlib import Path
import csv

#default 카테고리가 있어야 하는 이유???
DEFAULT_CATEGORIES = ["food", "transport", "rent", "salary", "etc"]

TRANSACTION_FIELDS = ["id", "date", "type", "category", "amount", "memo", "tags"]
CATEGORY_FIELDS = ["name"]
BUDGET_FIELDS = ["month", "amount"]


def init_storage(data_dir: str):
    base = Path(data_dir)
    base.mkdir(parents=True, exist_ok=True)

    files = {
        "transactions": (base / "transactions.csv", TRANSACTION_FIELDS),
        "categories": (base / "categories.csv", CATEGORY_FIELDS),
        "budgets": (base / "budgets.csv", BUDGET_FIELDS),
    }

    for path, fields in files.values():
        if not path.exists(): #없으면 파일 생성
            with path.open("w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=fields)
                writer.writeheader()

    init_default_categories(base / "categories.csv")

#기본 카테고리 설정
def init_default_categories(path: Path):
    with path.open("r", newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    #?????
    if rows:
        return

    with path.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CATEGORY_FIELDS)
        for name in DEFAULT_CATEGORIES:
            writer.writerow({"name": name})