# Fungsi script Python ini adalah memasukkan 1 Data tambahan ke dalam DynamoDB
# year dan title akan dijadikan sebagai Primary Key untuk table Movies
# sisa informasi tambahan dalam data akan disimpan dalam attribute tersendiri dengan nama info

from pprint import pprint # Lakukan import library pprint
import boto3 # Lakukan import library boto3


def put_movie(title, year, plot, rating, dynamodb=None): # Function ini digunakan untuk memasukkan 1 Data tambahan ke dalam DynamoDB
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000") # Endpoint dari DynamoDB ini adalah localhost:8000

    table = dynamodb.Table('Movies') # Table yang dituju adalah table Movies
    response = table.put_item(
       Item={
            'year': year, # Nilai year adalah year dari data
            'title': title, # Nilai title adalah title dari data
            'info': {
                'plot': plot, # Nilai plot adalah plot dari data
                'rating': rating # Nilai rating adalah rating dari data
            }
        }
    )
    return response


if __name__ == '__main__': # Fungsi Main untuk menjalankan Function put_movie
    movie_resp = put_movie("The Big New Movie", 2015, # Data yang akan dimasukkan
                           "Nothing happens at all.", 0)
    print("Put movie succeeded:") # Keluarkan status hasil pemasukan data
    pprint(movie_resp, sort_dicts=False)