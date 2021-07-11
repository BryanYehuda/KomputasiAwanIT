# Fungsi script Python ini adalah melakukan update 1 Data yang ada di DynamoDB
# year dan title akan dijadikan sebagai Primary Key untuk table Movies
# sisa informasi tambahan dalam data akan disimpan dalam attribute tersendiri dengan nama info

from decimal import Decimal # Lakukan import library Decimal
from pprint import pprint # Lakukan import library pprint
import boto3 # Lakukan import library boto3


def update_movie(title, year, rating, plot, actors, dynamodb=None): # Function ini digunakan untuk melakukan update 1 Data yang ada di DynamoDB
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000") # Endpoint dari DynamoDB ini adalah localhost:8000

    table = dynamodb.Table('Movies') # Table yang dituju adalah table Movies

    response = table.update_item( # Lakukan update data dengan Key yang dikirimkan
        Key={
            'year': year,
            'title': title
        },
        UpdateExpression="set info.rating=:r, info.plot=:p, info.actors=:a",
        ExpressionAttributeValues={
            ':r': Decimal(rating),
            ':p': plot,
            ':a': actors
        },
        ReturnValues="UPDATED_NEW" # Kembalikan status Updated
    )
    return response


if __name__ == '__main__': # Fungsi Main untuk menjalankan Function update_movie
    update_response = update_movie( 
        "The Big New Movie", 2015, 5.5, "Everything happens all at once.", # Data yang akan diupdate
        ["Larry", "Moe", "Curly"])
    print("Update movie succeeded:") # Keluarkan status hasil pemasukan data
    pprint(update_response, sort_dicts=False)