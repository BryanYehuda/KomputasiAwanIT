# Fungsi script Python ini adalah melakukan penghapusan table Movies

import boto3 # Lakukan import library boto3

def delete_movie_table(dynamodb=None): # Function ini digunakan untuk melakukan penghapusan table Movies
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000") # Endpoint dari DynamoDB ini adalah localhost:8000

    table = dynamodb.Table('Movies') # Table yang dituju adalah table Movies
    table.delete() # Hapus table


if __name__ == '__main__': # Fungsi Main untuk menjalankan Function delete_movie_table
    delete_movie_table() # Jalankan function
    print("Movies table deleted.") # Outputkan status