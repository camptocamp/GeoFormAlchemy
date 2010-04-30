from sqlalchemy import Column, types, ForeignKey
from sqlalchemy.orm import relationship

from geoalchemy import GeometryColumn, Point, GeometryDDL

from demoapp.model.meta import engine, Base
from demoapp.model.categories import Category

class Place(Base):
    __tablename__ = 'places'
    
    id = Column(types.Integer, primary_key=True)
    name = Column(types.String, nullable=False)
    
    category_id = Column(types.Integer, ForeignKey('categories.cid'))
    category = relationship(Category)
    

    the_geom = GeometryColumn(Point(dimension=2, srid=4326))

GeometryDDL(Place.__table__)
