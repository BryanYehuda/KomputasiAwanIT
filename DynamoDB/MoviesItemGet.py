# Fungsi script Python ini adalah membaca (get) 1 Data dari DynamoDB
# year dan title akan dijadikan sebagai Primary Key untuk table Movies
# sisa informasi tambahan dalam data akan disimpan dalam attribute tersendiri dengan nama info

from pprint import pprint # Lakukan import library pprint
import boto3 # Lakukan import library boto3
from botocore.exceptions import ClientError # Lakukan import ClientError


def get_movie(title, year, dynamodb=None): # Function ini digunakan untuk membaca (get) 1 Data dari DynamoDB
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000") # Endpoint dari DynamoDB ini adalah localhost:8000

    table = dynamodb.Table('Movies') # Table yang dituju adalah table Movies

    try:
        response = table.get_item(Key={'year': year, 'title': title}) # Coba ambil data di Table dengan Key year dan title
    except ClientError as e:
        print(e.response['Error']['Message']) # Jika error keluarkan error messagenya
    else:
        return response['Item'] # Jika ditemukan kembalikan item yang ditemukan tersebut


if __name__ == '__main__': # Fungsi Main untuk menjalankan Function put_movie
    movie = get_movie("The Big New Movie", 2015,) # Data yang akan dicari
    if movie:
        print("Get movie succeeded:") # Keluarkan status hasil pemasukan data
        pprint(movie, sort_dicts=False)