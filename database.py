import sqlalchemy
from sqlalchemy import create_engine, text

engine = create_engine(
    "mysql+pymysql://root:password@127.0.0.1:3306/jobs?charset=utf8mb4"
)

with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    print(result.all())