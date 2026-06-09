
class CategoryRepository:
    def __init__(self, category_name: str):
        self.categories = []
    
    def add(self, name: str):
        name = name.strip()

        if name == "":
            raise ValueError("카테고리 이름은 비어 있을 수 없습니다.")
        if self.is_exist(name):
            return False

        self.categories.append(name)

        return True

    def list_all(self):
        return self.categories.copy() #안전을 위해 리스트 전체를 복사해서 전달

    def remove(self, name: str):
        name = name.strip()

        if not self.is_exist(name):
            return False
        
        self.categories.remove(name)

        return True

    def is_exist(self, name: str):
        return name.strip() in self.categories