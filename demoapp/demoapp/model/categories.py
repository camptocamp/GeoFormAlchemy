from sqlalchemy import Column, types

from demoapp.model.meta import engine, Base

class Category(Base):
    __tablename__ = 'categories'
    
    cid = Column(types.Integer, primary_key=True)
    name = Column(types.String)
    description = Column(types.String)

    def __str__(self):
        return self.name

