from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from utils.dao.staff import StaffDao
from utils.dao.title import TitleDao


class ShowsDB:
    def __init__(self, connection_string):
        self.__db_engine = create_engine(connection_string)
        session_with_engine = sessionmaker(bind=self.__db_engine)
        self.__db_session = session_with_engine()

    def staffs(self):
        return StaffDao(self.__db_session)

    def titles(self):
        return TitleDao(self.__db_session)