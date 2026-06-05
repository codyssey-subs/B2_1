import argparse

def create_parser():
    parser = argparse.ArgumentParser(
        prog="python -m budget_app",
        description="가계부 CLI 프로그램"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
        help="사용 가능한 명령어"
    )

    add_parser(subparsers)

    list_parser(subparsers)

    update_parser(subparsers)

    delete_parser(subparsers)

    search_parser(subparsers)

    summary_parser(subparsers)

    budget_parser(subparsers)

    category_parser(subparsers)

    import_parser(subparsers)
    export_parser(subparsers)
    
    return parser



#add
def add_parser(subparsers):
    add_parser = subparsers.add_parser(
        "add",
        help="수입 또는 지축 내역 추가"
    )
    add_parser.add_argument("--date", required=True, help="날짜: YYYY-MM-DD")
    add_parser.add_argument("--type", required=True, choices=["income", "expense"])
    add_parser.add_argument("--category", required=True)
    add_parser.add_argument("--amount", required=True, type=int)
    add_parser.add_argument("--memo", default="")
    add_parser.add_argument("--tags", default="")

#list
def list_parser(subparsers):
    list_parser = subparsers.add_parser(
        "list",
        help="가계부 내역 조회"
    )
    list_parser.add_argument("-limit", required=True, type=int)

#search
def search_parser(subparsers):
    search_parser = subparsers.add_parser(
        "search",
        help="조건에 맞는 거래 내역 검색"
    )
    search_parser.add_argument("--from", dest="from_date", help="검색 시작 날짜: YYYY-MM-DD")
    search_parser.add_argument("--to", dest="to_date", help="검색 종료 날짜: YYYY-MM-DD")
    search_parser.add_argument("--category", help="검색할 카테고리")
    search_parser.add_argument("--type", choices=["income", "expense"], help="거래 타입: income 또는 expense")
    search_parser.add_argument("-q", "--query", dest="q", help="메모에서 검색할 키워드")
    search_parser.add_argument("--tag", help="검색할 태그")

#summary
def summary_parser(subparsers):
    summary_parser = subparsers.add_parser(
        "summary",
        help="월별 수입/지출 요약 조회"
    )
    summary_parser.add_argument("--month", required=True, help="요약할 월: YYYY-MM")
    summary_parser.add_argument("--top", type=int, default=5, help="카테고리별 지출 TOP N, 기본값: 5")

#budget
def budget_parser(subparsers):
    budget_set_parser = subparsers.add_parser(
        "budget set",
        help="월별 예산 설정"
    )
    budget_set_parser.add_argument("--month", required=True, help="예산을 설정할 월: YYYY-MM")
    budget_set_parser.add_argument("--amount", required=True, type=int, help="예산 금액")

#category
def category_parser(subparsers):
    category_parser = subparsers.add_parser(
        "category",
        help="카테고리 관리"
    )
    category_subparsers = category_parser.add_subparsers(dest="category_command", required=True, help="카테고리 관련 명령어")
    category_add_parser = category_subparsers.add_parser("add", help="카테고리 추가")
    category_add_parser.add_argument("--name", required=True, help="추가할 카테고리 이름")
    category_subparsers.add_parser("list", help="카테고리 목록 조회")
    category_remove_parser = category_subparsers.add_parser("remove", help="카테고리 삭제")
    category_remove_parser.add_argument("--name", required=True, help="삭제할 카테고리 이름")

#update
def update_parser(subparsers):
    update_parser = subparsers.add_parser(
        "update",
        help="id를 기준으로 거래 내역 수정"
    )
    update_parser.add_argument("--id", required=True, type=int, help="수정할 거래 ID")
    update_parser.add_argument("--date", help="수정할 날짜: YYYY-MM-DD")
    update_parser.add_argument("--type", choices=["income", "expense"], help="수정할 거래 타입: income 또는 expense")
    update_parser.add_argument("--category", help="수정할 카테고리")
    update_parser.add_argument("--amount", type=int, help="수정할 금액")
    update_parser.add_argument("--memo", help="수정할 메모")
    update_parser.add_argument("--tags", help="수정할 태그, 쉼표로 구분")

#delete
def delete_parser(subparsers):
    delete_parser = subparsers.add_parser(
        "delete",
        help="id를 기준으로 거래 내역 삭제"
    )
    delete_parser.add_argument("--id", required=True, type=int, help="삭제할 거래 ID")

#import
def import_parser(subparsers):
    import_parser = subparsers.add_parser(
        "import",
        help="CSV 파일에서 거래 내역 일괄 등록"
    )
    import_parser.add_argument("--from", dest="from_file", required=True, help="가져올 CSV 파일 경로")

#export
def export_parser(subparsers):
    export_parser = subparsers.add_parser(
        "export",
        help="조건에 맞는 거래 내역을 CSV로 저장"
    )
    export_parser.add_argument("--out", required=True, help="저장할 CSV 파일 경로")
    export_parser.add_argument("--month", help="내보낼 월: YYYY-MM")
    export_parser.add_argument("--from", dest="from_date", help="내보낼 시작 날짜: YYYY-MM-DD")
    export_parser.add_argument("--to", dest="to_date", help="내보낼 종료 날짜: YYYY-MM-DD")