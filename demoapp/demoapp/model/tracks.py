from sqlalchemy import Column, types, ForeignKey
from sqlalchemy.orm import relationship

from geoalchemy import GeometryColumn, LineString, GeometryDDL

from demoapp.model.meta import Base
from demoapp.model.categories import Category

class Track(Base):
    __tablename__ = 'tracks'
    
    id = Column(types.Integer, primary_key=True)
    name = Column(types.String, nullable=False)
    
    category_id = Column(types.Integer, ForeignKey('categories.cid'))
    categorie = relationship(Category)

    the_geom = GeometryColumn(LineString(dimension=2, srid=4326))

GeometryDDL(Track.__table__)
    
