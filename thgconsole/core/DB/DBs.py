from thgconsole.core.DB.db_config import *

class Mission(Base):
    __tablename__ = 'miission'
    id = Column(Integer,primary_key=True)
    nome = Column(String(250),nullable=False)


