from sqlalchemy import create_engine
from sqlalchemy import text
from dotenv import load_dotenv
import os

load_dotenv()
doc_string = os.getenv('doc_string')

engine = create_engine(
    doc_string
)
def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        result_dicts = []
        for row in result.all():
            result_dicts.append(dict(row._mapping))
        print(result_dicts)
        return result_dicts
