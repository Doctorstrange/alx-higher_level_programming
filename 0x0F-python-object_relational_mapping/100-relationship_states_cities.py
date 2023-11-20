#!/usr/bin/python3
"""Improve the files model_city.py and model_state.py"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    insState = State(name='California')
    insCity = City(name='San Francisco')
    insState.cities.append(insCity)

    session.add(insState)
    session.add(insCity)
    session.commit()
