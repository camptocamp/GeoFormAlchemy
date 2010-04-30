"""The application's model objects"""
import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy.dialects.sqlite.base import SQLiteDialect
from sqlalchemy.interfaces import PoolListener

from demoapp.model import meta

from demoapp.model.places import Place
from demoapp.model.categories import Category
from demoapp.model.tracks import Track
from demoapp.model.geometries import Geometry
from demoapp.model.lakes import Lake

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    ## Reflected tables must be defined and mapped here
    #global reflected_table
    #reflected_table = sa.Table("Reflected", meta.metadata, autoload=True,
    #                           autoload_with=engine)
    #orm.mapper(Reflected, reflected_table)
    #
    meta.Session.configure(bind=engine)
    meta.engine = engine
    
    # load Spatialite extension
    if isinstance(engine.dialect, SQLiteDialect):
        class SpatialiteConnectionListener(PoolListener):
            def connect(self, dbapi_con, con_record):
                dbapi_con.enable_load_extension(True)
                dbapi_con.execute("select load_extension('/usr/local/lib/libspatialite.so')")
                dbapi_con.enable_load_extension(False)

    engine.pool.add_listener(SpatialiteConnectionListener())


## Non-reflected tables may be defined and mapped at module level
#foo_table = sa.Table("Foo", meta.metadata,
#    sa.Column("id", sa.types.Integer, primary_key=True),
#    sa.Column("bar", sa.types.String(255), nullable=False),
#    )
#
#class Foo(object):
#    pass
#
#orm.mapper(Foo, foo_table)


## Classes for reflected tables may be defined here, but the table and
## mapping itself must be done in the init_model function
#reflected_table = None
#
#class Reflected(object):
#    pass
