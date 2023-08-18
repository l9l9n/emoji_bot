from database.models import Category,User,Film
from db import get_session


class CategoryManager():
    def __init__(self) :
        self.model = Category
        self.session = get_session()
        
    
    def insert_category(self,data):
        inserts = []
        for i in data:
            inserts.append(
                Category(
                   name = i[0] 
                )
            )
            
        self.session.add_all(inserts)
        self.session.commit()
    
    def get_all_categories(self):
        result = self.session.query(self.model).all()
        return result