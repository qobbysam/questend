from email.policy import default
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from geoalchemy2 import *
import uuid

username = "gisuser"
password = "1234"
host = "localhost"
port ="5432"
dbname = "gis"

url = 'postgresql://{}:{}@{}:{}/{}'.format(username,password,host,port, dbname)
engine = create_engine(url, echo=True)
Session = sessionmaker(bind=engine)
session = Session()


metadata = MetaData(engine)


Base = declarative_base(metadata=metadata)

def init_db():
    metadata.create_all(engine)


class LastUpdate(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    time = Column(DateTime, default=datetime.now())

class DrugTestSpot(Base):
    __tablename__ = 'spots'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(Unicode, nullable=False)
    height = Column(Integer)
    created = Column(DateTime, default=datetime.now())
    geom = Column(Geometry('POINT', srid=4326, spatial_index=True) )
    sitecode = Column(Unicode, nullable=False)
    status = Column(Unicode, nullable=True)
    address1 = Column(Unicode, nullable=True)
    address2 = Column(Unicode, nullable=True)
    city = Column(Unicode, nullable=True)
    state = Column(Unicode, nullable=True)
    zipcode = Column(Unicode, nullable=True)
    county = Column(Unicode, nullable=True)
    primary_phone_number = Column(Unicode, nullable=True)
    secondary_phone_number = Column(Unicode, nullable=True)
    faxnumber = Column(Unicode, nullable=True)
    activedate = Column(DateTime)
    isactive = Column(Boolean,default=False)
    timezone = Column(Unicode, nullable=True)
    collectionsitetypeid = Column(Unicode, nullable=True)
    scheduling = Column(Boolean, default=False)
    phlembotomy = Column(Boolean, default=False)
    nidacollections = Column(Boolean, default=False)
    sapcollections = Column(Boolean, default=False)
    observedcollection = Column(Boolean, default=False)
    breath_alcohol_regulated = Column(Boolean, default=False)
    breath_alcohol_nonregulated = Column(Boolean, default=False)
    ebreathalcohol = Column(Boolean, default=False)
    pediatrics = Column(Boolean, default=False)
    haircollection = Column(Boolean, default=False)
    glucosetolerance = Column(Boolean, default=False)
    onsitecollections = Column(Boolean, default=False)
    onsitepoct = Column(Boolean, default=False)
    oral_fluid_collections = Column(Boolean, default=False)
    oral_fluid_poct = Column(Boolean, default=False)
    bfw = Column(Boolean, default=False)
    urinepoct = Column(Boolean, default=False)
    insuranceexam = Column(Boolean, default=False)
    physicals = Column(Boolean, default=False)
    biometrics = Column(Boolean, default=False)
    electronicccf = Column(Boolean, default=False)
    administrative = Column(Boolean, default=False)
    consumerservices = Column(Boolean, default=False)
    historycyto = Column(Boolean, default=False)
    idaa_accessioning = Column(Boolean, default=False)
    logistics = Column(Boolean, default=False)
    paramedicalservices = Column(Boolean, default=False)
    testing = Column(Boolean, default=False)
    regulated_electronic_ccf =Column(Boolean, default=False)
    hrselectronicccf = Column(Boolean, default=False)
    federally_regulated_physicals = Column(Boolean, default=False)
    appointmentschedulingflag = Column(Boolean, default=False)
    opentopublic = Column(Boolean, default=False)
    hoursofoperation = Column(Unicode, nullable=True)
    courierpickup = Column(Unicode, nullable=True)
    hoursafter5 = Column(Boolean, default=False)
    hours24_7 = Column(Boolean, default=False)
    hoursweekend = Column(Boolean, default=False)
    drugoperationhours = Column(Unicode, nullable=True)


    def __str__(self):

        return self.name

