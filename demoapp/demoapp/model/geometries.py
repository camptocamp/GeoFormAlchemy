from sqlalchemy import Column, types, ForeignKey
from sqlalchemy.orm import relationship

from geoalchemy import GeometryColumn, GeometryDDL
from geoalchemy import geometry

from demoapp.model.meta import Base
from demoapp.model.categories import Category

class Geometry(Base):
    __tablename__ = 'geometries'
    
    id = Column(types.Integer, primary_key=True)
    name = Column(types.String, nullable=False)
    
    category_id = Column(types.Integer, ForeignKey('categories.cid'))
    category = relationship(Category)
    

    the_geom = GeometryColumn(geometry.Geometry(dimension=2, srid=4326))

GeometryDDL(Geometry.__table__)
    
