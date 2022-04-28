from utils.dao.dao import Dao
from models.staff import Staff


class StaffDao(Dao):
    def get(self, id):
        staff ,= self.session.query(Staff).filter(Staff.id == id)
        return staff

    def get_all(self):
        return self.session.query(Staff).all()

    def create(self, staff):
        self.session.add(staff)
        self.session.commit()