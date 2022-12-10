from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:DAta2542@localhost:3306/prospectosdb")

meta = MetaData()

conn = engine.connect()