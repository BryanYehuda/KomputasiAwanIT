# Fungsi script Python ini adalah melakukan query semua data film yang ada di range tahun tertentu
# year dan title akan dijadikan sebagai Primary Key untuk table Movies
# sisa informasi tambahan dalam data akan disimpan dalam attribute tersendiri dengan nama info

from pprint import pprint # Lakukan import library pprint
import boto3 # Lakukan import library boto3 
from boto3.dynamodb.conditions import Key # Lakukan import key


def scan_movies(year_range, display_movies, dynamodb=None): # Function ini digunakan untuk melakukan query semua data film yang ada di range tahun tertentu
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000") # Endpoint dari DynamoDB ini adalah localhost:8000

    table = dynamodb.Table('Movies') # Table yang dituju adalah table Movies
    scan_kwargs = {
        'FilterExpression': Key('year').between(*year_range), # Cari data yang sesuai dengan year dan title yang diminta
        'ProjectionExpression': "#yr, title, info.rating",
        'ExpressionAttributeNames': {"#yr": "year"}
    }

    done = False
    start_key = None
    while not done: # Selama semua data belum berhasil didapatkan
        if start_key:
            scan_kwargs['ExclusiveStartKey'] = start_key
        response = table.scan(**scan_kwargs) # Cari data dengan year yang diminta
        display_movies(response.get('Items', [])) # Kembalikan data yang didapatkan
        start_key = response.get('LastEvaluatedKey', None)
        done = start_key is None


if __name__ == '__main__': # Fungsi Main untuk menjalankan Function scan_movies
    def print_movies(movies):
        for movie in movies:
            print(f"\n{movie['year']} : {movie['title']}") # Outputkan status pencarian data
            pprint(movie['info'])

    query_range = (1950, 1959) # Range year yang diminta
    print(f"Scanning for movies released from {query_range[0]} to {query_range[1]}...")
    scan_movies(query_range, print_movies) # Jalankan functionnya