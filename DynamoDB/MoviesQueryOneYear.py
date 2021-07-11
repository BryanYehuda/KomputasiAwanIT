# Fungsi script Python ini adalah melakukan query semua data film yang ada di tahun tertentu
# year dan title akan dijadikan sebagai Primary Key untuk table Movies
# sisa informasi tambahan dalam data akan disimpan dalam attribute tersendiri dengan nama info

import boto3 # Lakukan import library boto3
from boto3.dynamodb.conditions import Key # Lakukan import key


def query_movies(year, dynamodb=None): # Function ini digunakan untuk melakukan query semua data film yang ada di tahun tertentu
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000") # Endpoint dari DynamoDB ini adalah localhost:8000

    table = dynamodb.Table('Movies') # Table yang dituju adalah table Movies
    response = table.query(
        KeyConditionExpression=Key('year').eq(year) # Cari data yang sesuai dengan year yang diminta
    )
    return response['Items'] # Kembalikan data tersebut


if __name__ == '__main__': # Fungsi Main untuk menjalankan Function query_movies
    query_year = 1985 # year yang diminta
    print(f"Movies from {query_year}") # Outputkan data yang ditemukan
    movies = query_movies(query_year)
    for movie in movies:
        print(movie['year'], ":", movie['title']) # Ulangi hingga semua film dengan tahun yang diminta berhasil didapatkan