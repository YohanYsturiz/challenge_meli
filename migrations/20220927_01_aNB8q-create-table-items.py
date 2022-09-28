"""
create table items
"""

from yoyo import step

__depends__ = {}

steps = [
    step(
        """
            CREATE TABLE item (
                id SERIAL PRIMARY KEY, 
                site VARCHAR(50), 
                item_code INT, 
                price VARCHAR(50), 
                start_time VARCHAR(50), 
                name VARCHAR(50), 
                description VARCHAR(150), 
                nickname VARCHAR(150), 
                created_at TIMESTAMP
            )
        """,
        "DROP TABLE item"
    )
]
