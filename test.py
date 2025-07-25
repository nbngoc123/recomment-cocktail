import psycopg2
import os
from dotenv import load_dotenv
from conected_psql import generate_embeddings

load_dotenv()

class CocktailRecommender:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        print('api đã sẵn sằng rồi anh yêu thịt em đi')
        
    def test(self):
        query_embedding = generate_embeddings(["cocktail with chocolate"], "BAAI/bge-large-en-v1.5")[0]
        
        embedding_str = "[" + ",".join(map(str, query_embedding)) + "]"

        cur = self.conn.cursor()
        cur.execute(
            """SELECT name, recipe, 1 - (embedding <=> %s) as similarity
               FROM cocktails
               ORDER BY similarity DESC
               LIMIT 5""",
            (embedding_str,)
        )
        rows = cur.fetchall()
        for row in rows:
            print(row)
        
if __name__ == "__main__":
    recommender = CocktailRecommender()
    recommender.test()
