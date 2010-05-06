Installation and Setup
======================

To run the GeoFormAlchemy demo application make sure that GeoFormAlchemy
and Spatialite are installed. You can change the path to the Spatialite
library in the file ``demoapp/model/__init__.py``. 

Run the setup::
    
    python setup.py develop
    
And start the Paster web server::

    paster serve development.ini --reload
    
Now open the administration interface in your web browser at: http://127.0.0.1:5000/admin
