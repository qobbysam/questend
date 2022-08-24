from datetime import datetime
import json
import uuid 
from zeep import Client, Settings
from zeep.helpers import serialize_object
from tinydb import TinyDB, Query
import uuid
import distutils
import xmltodict

from shapely.geometry import Point
from geoalchemy2.shape import to_shape, from_shape
import sys
#print(sys.path)
import os

#from db_models import DrugTestSpot, session, init_db


url = "https://qcs-uat.questdiagnostics.com/services/esservice.asmx?wsdl"
username = "cli_ArtemisHealthUAT"
password = "xRq0vUf2pH05"

base_dir = os.getcwd()
db_name = "location.db"

db_path = os.path.join(base_dir, db_name)

db = TinyDB(db_path)
settings = Settings(xml_huge_tree=True)
client = Client(url, settings=settings)

last_update = datetime.now()


from email.policy import default
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from geoalchemy2 import *
import uuid

username_post = "gisuser"
password_post = "1234"
host_post = "localhost"
port_post ="5432"
dbname_post = "gis"

url = 'postgresql://{}:{}@{}:{}/{}'.format(username_post,password_post,host_post,port_post, dbname_post)
engine = create_engine(url, echo=True)
Session = sessionmaker(bind=engine)
session = Session()


metadata = MetaData(engine)


Base = declarative_base(metadata=metadata)

def init_db():
    metadata.create_all(engine)


# class LastUpdate(Base):
#     id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
#     time = Column(DateTime, default=datetime.now())

class DrugTestSpot(Base):
    __tablename__ = 'spots'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(Unicode, nullable=False)
    height = Column(Integer)
    created = Column(DateTime, default=datetime.now())
    geom = Column(Geometry('POINT', srid=4326, spatial_index=True) )
    longitude = Column(Unicode, nullable=False)
    latitude = Column(Unicode, nullable=False)
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
    
    def as_dict(self):
        
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}




def dict_to_spot(location):
    return DrugTestSpot(**location)


def save_db_update_postgres(list_of_objs):
    init_db()
    print("saving  ", len(list_of_objs) )
    session.bulk_update_mappings( DrugTestSpot,list_of_objs)


def res_to_list(res):
    dic__ = xmltodict.parse(res)

    size= dic__['CollectionSiteDetails']['NumberOfCollectionSitesChanged']

    if int(size) <= 0:
        return []
        
    location_list = dic__['CollectionSiteDetails']['CollectionSiteDetail']

    print("finish parse")
    to_save = []

    sucess_cont = 0
    fail_cont = 0
    not_safe = 0


    for location in location_list:
        try:
            safedb, ok = produce_db_safe(location)
            
            if not ok:
                fail_cont = fail_cont + 1
                continue
            else:
                
                
                #print(len(safedb))
                
                try:
                    #to_app = dict_to_spot(safedb)
                    to_save.append(safedb)
                    sucess_cont = sucess_cont + 1
                except Exception as e:
                    not_safe = not_safe + 1
                    print(safedb)
                    print(e)
                    continue

        except:
            #print("failed to parse")
            fail_cont = fail_cont + 1
            continue

    print("sc ", sucess_cont, "  f ",fail_cont, "  ns ", not_safe)

    return to_save  


def save_db_postgres(list_of_objs):
    init_db()
    print("saving  ", len(list_of_objs) )

    #bulk_upsert(session,list_of_objs)
    
    session.bulk_insert_mappings(DrugTestSpot,list_of_objs)
    session.flush()
    session.commit()
    # print("saving  ", len(list_of_objs) )

    print ("finished saving")

def save_db(result_):
    #table = db.table(tablename)

    to_save = {
                "time_added": str(datetime.now()),

                "result" : result_,
            }

    db.insert(to_save)


'''consume saved file '''

def consume_to_post():
    #q = Query()

    res = db.all()[0]

    dict_out = json.loads(res['result'])
    location_list = dict_out['CollectionSiteDetails']['CollectionSiteDetail']
    print("finish parse")
    # for key,value in location_list.items():
    #     print(key)
    to_save = []

    sucess_cont = 0
    fail_cont = 0
    not_safe = 0

    for location in location_list:
        try:
            safedb, ok = produce_db_safe(location)
            
            if not ok:
                fail_cont = fail_cont + 1
                continue
            else:
                
                
                #print(len(safedb))
                
                try:
                    #to_app = dict_to_spot(safedb)
                    to_save.append(safedb)
                    sucess_cont = sucess_cont + 1
                except Exception as e:
                    not_safe = not_safe + 1
                    print(safedb)
                    print(e)
                    continue

        except:
            #print("failed to parse")
            fail_cont = fail_cont + 1
            continue
        
    
            #print("adding one")           
            #jsn = json.dumps(dic__)

    print("sc ", sucess_cont, "  f ",fail_cont, "  ns ", not_safe)
    
    save_db_postgres(to_save)


    
from sqlalchemy.dialects import postgresql

def bulk_upsert(session, 
                items):
  session.execute(
    postgresql.insert(DrugTestSpot.__table__)
    .values(items)
    .on_conflict_do_update(
      index_elements=[DrugTestSpot.id],
      set_=items
    )
  )





def do_first_pull():

      
    res_ = client.service.FullRetrieveCollectionSiteDetails(username, password)
    #dic__ = serialize_object(res_ )

    dic__ = xmltodict.parse(res_)

    location_list = dic__['CollectionSiteDetails']['CollectionSiteDetail']

    print("finish parse")
    # for key,value in location_list.items():
    #     print(key)
    to_save = []

    sucess_cont = 0
    fail_cont = 0
    not_safe = 0


    for location in location_list:
        try:
            safedb, ok = produce_db_safe(location)
            
            if not ok:
                fail_cont = fail_cont + 1
                continue
            else:
                
                
                #print(len(safedb))
                
                try:
                    #to_app = dict_to_spot(safedb)
                    to_save.append(safedb)
                    sucess_cont = sucess_cont + 1
                except Exception as e:
                    not_safe = not_safe + 1
                    print(safedb)
                    print(e)
                    continue

        except:
            #print("failed to parse")
            fail_cont = fail_cont + 1
            continue
        
        
        
        
            #print("adding one")
            
                
            
    



    #jsn = json.dumps(dic__)

    print("sc ", sucess_cont, "  f ",fail_cont, "  ns ", not_safe)
    
    save_db_postgres(to_save)




def save_to_db():
    print("saving to db")

def produce_db_safe(location):
    ok = False
    if not location['OpenToPublic'] or not location['IsActive']:
        return "", ok
    else:
        ok = True

        safedb = normalise(location)

        return safedb, ok


def get_point(long, lat):

    point = from_shape(Point(float(long), float(lat)), srid=4326)

    return point

def normalise(location):

    point = get_point(location["Longitude"], location["Latitude"])
    out = {}
    out['longitude'] = location["Longitude"]
    out['latitude'] = location["Latitude"]
    out["id"] = uuid.uuid4()
    out["name"] = location["Address"]["Name"]
    out["height"] = 1
    out["created"] = datetime.now()
    out["geom"] = point
    out["sitecode"] = location["SiteCode"]
    out["status"] = location["Status"]
    out["address1"] = location["Address"]["Address1"]
    out["address2"] = location["Address"]["Address2"]
    out["city"] = location["Address"]["City"]
    out["state"] = location["Address"]["State"]
    out["zipcode"] = location["Address"]["Zip"]
    out["county"] = location["Address"]["County"]
    out["primary_phone_number"] = location["PrimaryPhoneNumber"]
    out["secondary_phone_number"] = location["SecondaryPhoneNumber"]
    out["faxnumber"] = location["FaxNumber"]
    out["activedate"] = location["ActiveDate"]
    out["isactive"] = bool(distutils.util.strtobool(location["IsActive"]))

    out["collectionsitetypeid"] = location["CollectionSiteTypeId"]

    out["scheduling"] = bool(distutils.util.strtobool(location["Scheduling"]))
    out["phlembotomy"] = bool(distutils.util.strtobool(location["Phlebotomy"]))
    out["nidacollections"] = bool(distutils.util.strtobool(location["NIDACollections"]))
    out["sapcollections"] = bool(distutils.util.strtobool(location["SAPCollections"]))
    out["observedcollection"] =bool(distutils.util.strtobool( location["ObservedCollection"]))
    out["breath_alcohol_regulated"] = bool(distutils.util.strtobool(location["BreathAlcoholRegulated"]))
    out["breath_alcohol_nonregulated"] = bool(distutils.util.strtobool(location["BreathAlcoholNonRegulated"]))
    out["ebreathalcohol"] = bool(distutils.util.strtobool(location["eBreathAlcohol"]))
    out["pediatrics"] = bool(distutils.util.strtobool(location["Pediatrics"]))
    out["haircollection"] = bool(distutils.util.strtobool(location["HairCollections"]))
    out["glucosetolerance"] = bool(distutils.util.strtobool(location["GlucoseTolerance"]))
    out["onsitecollections"] = bool(distutils.util.strtobool(location["OnSiteCollections"]))
    out["onsitepoct"] = bool(distutils.util.strtobool(location["OnSitePOCT"]))
    out["oral_fluid_collections"] =bool(distutils.util.strtobool( location["OralFluidCollections"]))
    out["oral_fluid_poct"] = bool(distutils.util.strtobool(location["OralFluidPOCT"]))
    out["bfw"] = bool(distutils.util.strtobool(location["BFW"]))
    out["urinepoct"] = bool(distutils.util.strtobool(location["UrinePOCT"]))
    out["insuranceexam"] = bool(distutils.util.strtobool(location["InsuranceExam"]))
    out["physicals"] = bool(distutils.util.strtobool(location["Physicals"]))
    out["biometrics"] = bool(distutils.util.strtobool(location["Biometrics"]))
    out["electronicccf"] = bool(distutils.util.strtobool(location["ElectronicCCF"]))
    out["administrative"] =bool(distutils.util.strtobool( location["Administrative"]))
    out["consumerservices"] = bool(distutils.util.strtobool(location["ConsumerServices"]))
    out["historycyto"] = bool(distutils.util.strtobool(location["HistoCyto"]))
    out["idaa_accessioning"] =bool(distutils.util.strtobool( location["IdaaAccessioning"]))
    out["logistics"] = bool(distutils.util.strtobool(location["Logistics"]))
    out["paramedicalservices"] = bool(distutils.util.strtobool(location["ParamedicalServices"]))
    out["testing"] = bool(distutils.util.strtobool(location["Testing"]))
    out["regulated_electronic_ccf"] = bool(distutils.util.strtobool(location["RegulatedElectronicCCF"]))
    out["hrselectronicccf"] = bool(distutils.util.strtobool(location["HRSElectronicCCF"]))
    out["federally_regulated_physicals"] = bool(distutils.util.strtobool(location["FederallyRegulatedPhysicals"]))
    out["appointmentschedulingflag"] = bool(distutils.util.strtobool(location["AppointmentSchedulingFlag"]))
    out["opentopublic"] = bool(distutils.util.strtobool(location["OpenToPublic"]))
    out["hoursofoperation"] = location["HoursOfOperation"]
    out["courierpickup"] = location["CourierPickup"]
    out["hoursafter5"] = bool(distutils.util.strtobool(location["HoursAfter5"]))
    out["hours24_7"] = bool(distutils.util.strtobool(location["Hours24_7"]))
    out["hoursweekend"] = bool(distutils.util.strtobool(location["HoursWeekend"]))

    out["drugoperationhours"] = location["DrugOperationHours"]

    return out

# def checkres():
    
#     res_ = client.service.FullRetrieveCollectionSiteDetails(username, password)

#     return res_







def pull_near_me(long,lat,miles=10):
    quotient = 1609
    #long= "-83.003897"
    #lat = "40.087551"

    actual = miles * quotient

    point = Point(float(long), float(lat))

    

    shape_ = from_shape(point, srid=4326).ST_Transform(3857).ST_Buffer(actual).ST_Transform(4326)

    locs = session.query(DrugTestSpot).filter(DrugTestSpot.geom.ST_Intersects(shape_)).all()

    return locs