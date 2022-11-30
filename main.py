import datetime
import os
import sqlite3

import requests
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
from dataclasses import dataclass

#  SQLAlchemy session initialization
Base = declarative_base()
engine = create_engine('sqlite:///sqlalchemy.db')

session_class = sessionmaker(bind=engine)
global_session = session_class()


class School(Base):
    __tablename__ = "schools"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    city = Column(String)

    def __init__(self, name: str, city: str):
        self.name = name
        self.city = city


Base.metadata.create_all(engine)


@dataclass
class Website:
    name: str
    url: str


def remove_file(file_path: str):
    """
    Removes a file from the filesystem
    """
    if os.path.exists(file_path):
        os.remove(file_path)
        return True
    return False


def add_school(session, name: str, city: str):
    """
    Adds a school to a database using SQLAlchemy
    """
    school = School(name=name, city=city)
    session.add(school)
    session.commit()


def get_school_by_name(name: str):
    """
    Queries a schoool based on its name, using SQLAlchemy
    """
    return global_session.query(School).filter(School.name == name).all()


def query_api(website: Website):
    """
    Makes a get request to the provided api*
    """
    resp = requests.get(website.url)
    if resp.status_code == 200:
        text = "Site is available"
    else:
        text = "Site is unavailable"
    resp.close()
    return text


def add_date_to_list(dates: list[datetime.datetime]):
    dates.append(datetime.datetime.now())


def query_from_sqlite(values: list[str]):
    """
    Initialized a connection to an sqlite database using the sqlite3 library,
    sets up a cursor, and queries the database.
    """
    cur = sqlite3.connect("sqlite3.db").cursor()
    results = cur.execute(f"SELECT {','.join(values)}").fetchall()
    if results:
        return False
    return True


"""
--------------------------------------------------------------------
--------------------------------------------------------------------
.oOOOo.                                                    
o     o                                                    
O.                                               O         
 `OOoo.                                         oOo        
      `O 'OoOo. .oOo. 'o     O `oOOoOO. .oOoO'   o   .oOo. 
       o  o   O O   o  O  o  o  O  o  o O   o    O   OooO' 
O.    .O  O   o o   O  o  O  O  o  O  O o   O    o   O     
 `oooO'   o   O `OoO'  `Oo'oO'  O  o  o `OoO'o   `oO `OoO'
--------------------------------------------------------------------
--------------------------------------------------------------------
"""


def main():
    # A main function that runs the above logic.
    # Snowmate won't generate tests for this function

    add_school(global_session, "Joe Doe School", "NY")
    get_school_by_name("Joe Doe School")

    # create a dummy file and run the remove_file function
    file_name = "dummy_file"
    with open(file_name, 'w') as f:
        f.write("content")
    remove_file(os.path.join(os.path.dirname(__file__), file_name))

    website = Website("google", "https://www.google.com")
    query_api(website)
    add_date_to_list(
        [datetime.datetime.now()]
    )
    query_from_sqlite(['1', '2'])


if __name__ == '__main__':
    # Install, import and add snowlib.start(...) here ---->

    main()
