from time import time
import pandas as pd
from sqlalchemy import create_engine

from app.db import sessionmaker, Base
from app.models import Posts

chunks = pd.read_csv('posts.csv', encoding='UTF-8')


if __name__ == "__main__":
    t = time()
    engine = create_engine("postgresql://postgres:postgres@postgres:5432/postgres")
    SessionLocal = sessionmaker(bind=engine)
    s = SessionLocal()
    Base.metadata.create_all(bind=engine)
    try:
        for row in range(1, len(chunks)):
            record = Posts(**{
                'text': chunks.text[row],
                'created_date': chunks.created_date[row],
                'rubrics': chunks.rubrics[row],
            })
            s.add(record,)

        s.commit()
    except Exception as e:
        print(e)
        s.rollback()
    finally:
        print('Connection is closed')
        s.close()
    print("Time elapsed: " + str(time() - t) + " s.")
