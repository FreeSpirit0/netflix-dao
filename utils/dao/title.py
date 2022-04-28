from utils.dao.dao import Dao
from models.title import Title


class TitleDao(Dao):
    def get(self, id):
        title ,= self.session.query(Title).filter(Title.id == id)
        return title

    def get_all(self):
        return self.session.query(Title).all()

    def create(self, title):
        self.session.add(title)
        self.session.commit()