# Fungsi script Python ini adalah melakukan Load Data dari moviedata.json ke DynamoDB
# Data dari moviedata.json diambil dari ribuan film yang ada di IMDB dalam format JSON
# year dan title dalam moviedata.json akan dijadikan sebagai Primary Key untuk table Movies
# sisa informasi tambahan dalam data akan disimpan dalam attribute tersendiri dengan nama info

from decimal import Decimal # Lakukan import library decimal
import json # Lakukan import library json
import boto3 # Lakukan import library boto3


def load_movies(movies, dynamodb=None): # Function ini digunakan untuk melakukan load data ke DynamoDB
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000") # Endpoint dari DynamoDB ini adalah localhost:8000

    table = dynamodb.Table('Movies') # Table yang dituju adalah table Movies
    for movie in movies: # Untuk setiap film yang ada di moviedata.json
        year = int(movie['year']) # Nilai year adalah year dari data
        title = movie['title'] # Nilai title adalah title dari data
        print("Adding movie:", year, title) # Printkan status pemasukkan data
        table.put_item(Item=movie) # Masukkan data ke DynamoDB


if __name__ == '__main__': # Fungsi Main untuk menjalankan Function load_movies
    with open("moviedata.json") as json_file: # Buka file moviedata.json
        movie_list = json.load(json_file, parse_float=Decimal) # Lakukan parsing format JSON
    load_movies(movie_list) # Jalankan Function load_movies