# Fungsi script Python ini adalah melakukan query semua data film yang ada di tahun dengan judul di range tertentu
# year dan title akan dijadikan sebagai Primary Key untuk table Movies
# sisa informasi tambahan dalam data akan disimpan dalam attribute tersendiri dengan nama info

from pprint import pprint # Lakukan import library pprint
import boto3 # Lakukan import library boto3 
from boto3.dynamodb.conditions import Key # Lakukan import key


def query_and_project_movies(year, title_range, dynamodb=None): # Function ini digunakan untuk melakukan query semua data film yang ada di tahun dengan judul di range tertentu
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000") # Endpoint dari DynamoDB ini adalah localhost:8000

    table = dynamodb.Table('Movies') # Table yang dituju adalah table Movies
    print(f"Get year, title, genres, and lead actor")

    response = table.query(
        ProjectionExpression="#yr, title, info.genres, info.actors[0]",
        ExpressionAttributeNames={"#yr": "year"},
        KeyConditionExpression=
            Key('year').eq(year) & Key('title').between(title_range[0], title_range[1]) # Cari data yang sesuai dengan year dan title yang diminta
    )
    return response['Items'] # Kembalikan data tersebut


if __name__ == '__main__': # Fungsi Main untuk menjalankan Function query_and_project_movies
    query_year = 1992 # year yang diminta
    query_range = ('A', 'L') # range title yang diminta
    print(f"Get movies from {query_year} with titles from "
          f"{query_range[0]} to {query_range[1]}") # Outputkan data yang ditemukan
    movies = query_and_project_movies(query_year, query_range)
    for movie in movies: # Ulangi hingga semua film dengan tahun dan judul yang diminta berhasil didapatkan
        print(f"\n{movie['year']} : {movie['title']}")
        pprint(movie['info'])