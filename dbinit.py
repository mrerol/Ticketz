import os
import sys

import psycopg2 as dbapi2

DATABASE_URL = 'postgres://kalcitdkfyeevw:39cdcacf84047dc48c74f58064a25a7406bd3645c95c712b9ba888f28cab791b@ec2-54-243-187-30.compute-1.amazonaws.com:5432/d96hqqveldfnft'

INIT_STATEMENTS = [
    """DROP TABLE IF EXISTS hotels""",

    """CREATE TABLE IF NOT EXISTS hotels 
    (
    
        hotel_id SERIAL NOT NULL PRIMARY KEY,
        name VARCHAR (50) NOT NULL,
        email VARCHAR (50) NOT NULL,
        description VARCHAR (250) NOT NULL,
        city VARCHAR (20),
        address VARCHAR (250) NOT NULL,
        phone VARCHAR (15) NOT NULL,
        website VARCHAR (50)
                
    )""",

    """INSERT INTO hotels VALUES (
                        1,
                        'deneme',
                        'deneme@deneme.com',
                        'demo of description',
                        'istanbul',
                        'deneme sokak deneme cadde deneme',
                        '0321221222',
                        'dememe.com'
    
    )""",

    """INSERT INTO hotels VALUES (
                            2,
                            'deneme',
                            'deneme@deneme.com',
                            'demo of description',
                            'istanbul',
                            'deneme sokak deneme cadde deneme',
                            '0321221222',
                            'dememe.com'
    
        )""",

    """INSERT INTO hotels VALUES (
                            3,
                            'deneme',
                            'deneme@deneme.com',
                            'demo of description',
                            'istanbul',
                            'deneme sokak deneme cadde deneme',
                            '0321221222',
                            'dememe.com'
    
        )""",

    """INSERT INTO hotels VALUES (
                            4,
                            'deneme',
                            'deneme@deneme.com',
                            'demo of description',
                            'istanbul',
                            'deneme sokak deneme cadde deneme',
                            '0321221222',
                            'dememe.com'
    
        )""",

    """INSERT INTO hotels VALUES (
                            5,
                            'deneme',
                            'deneme@deneme.com',
                            'demo of description',
                            'istanbul',
                            'deneme sokak deneme cadde deneme',
                            '0321221222',
                            'dememe.com'
    
        )""",

    """INSERT INTO hotels VALUES (
                            6,
                            'deneme',
                            'deneme@deneme.com',
                            'demo of description',
                            'istanbul',
                            'deneme sokak deneme cadde deneme',
                            '0321221222',
                            'dememe.com'
    
        )"""
]


def initialize(url):
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        for statement in INIT_STATEMENTS:
            cursor.execute(statement)
        cursor.close()


if __name__ == "__main__":
    url = os.getenv("DATABASE_URL")
    if url is None:
        print("Usage: DATABASE_URL=url python dbinit.py", file=sys.stderr)
        sys.exit(1)
    initialize(url)