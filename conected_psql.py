import os
import psycopg2
from typing import List
import numpy as np
from together import Together
from dotenv import load_dotenv
load_dotenv()

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
client = Together(api_key = TOGETHER_API_KEY)
def generate_embeddings(input_texts: List[str], model_api_string: str) -> np.ndarray:
        """Sinh embedding qua Together AI."""

        outputs = client.embeddings.create(
            input=input_texts, 
            model=model_api_string,
        )
        return np.array([x.embedding for x in outputs.data]) 

class DatabaseSetup:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        print('api đã sẵn sằng rồi anh yêu thịt em đi')

    def create_database(self):
        cur = self.conn.cursor()
        cur.execute('create extension if not exists vector')
        cur.execute("""
            create table if not exists cocktails (
                id serial primary key,
                name varchar(100) not null,
                ingredients text not null,
                recipe text,
                glass varchar(100),
                category varchar(100),
                iba varchar(100),
                alcoholic varchar(100),
                embedding vector(1024)
            );
        """)
        cur.execute("""
            create index if not exists cocktails_embedding_idx
            on cocktails
            using ivfflat
            (embedding vector_cosine_ops)
            with (lists = 100);
        """)
        self.conn.commit()
        cur.close()
        self.conn.close()
        print('xong rồi ba ơi con đã làm xong rồi chúng ta triển khai thôi :)))')

if __name__ == "__main__":
    db_setup = DatabaseSetup()
    db_setup.create_database()
