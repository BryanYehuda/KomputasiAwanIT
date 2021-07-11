# Fungsi Script Python ini adalah melakukan pembuatan Table
# Kita akan melakukan pembuatan sebuah table yang akan kita berikan nama movies
# Table movies ini akan memiliki sebuah Primary Key yang terdiri dari 2 attribute
# Attribute pertama adalah year dengan tipe data number sebagai Partition Key
# Attribute kedua adalah title dengan tipe data string sebagai Sort Key

import boto3 # Melakukan import library boto3 untuk membantu kita dalam tugas ini

def create_movie_table(dynamodb=None): # Function ini digunakan untuk membuat Table yang kita inginkan
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000") # Endpoint dari DynamoDB ini adalah localhost:8000

    table = dynamodb.create_table(
        TableName='Movies', # Table ini akan bernama Movies
        KeySchema=[
            {
                'AttributeName': 'year', # Mendefinisikan year sebagai Partition Key
                'KeyType': 'HASH'  
            },
            {
                'AttributeName': 'title',
                'KeyType': 'RANGE'  # Mendefinisikan title sebagai Sort Key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'year', # Tipe data year adalah Number atau N
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'title', # Tipe title year adalah String atau S
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10, # Mendefinisikan Kemampuan READ dan WRITE DynamoDB
            'WriteCapacityUnits': 10
        }
    )
    return table


if __name__ == '__main__': # Fungsi Main untuk menjalankan Function create_movie_table
    movie_table = create_movie_table()
    print("Table status:", movie_table.table_status) # Printkan status pembuatan DynamoDB