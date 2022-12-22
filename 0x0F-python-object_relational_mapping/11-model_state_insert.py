#!/usr/bin/python3
"""list all States from the database hbtn_0e_6_usa"""


def main():
    """connect to db, read data and display as expected using ORM"""
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    louisiana = State(name='Louisiana')
    session.add(louisiana)
    session.commit()
    session.flush()
    # added_data = session.query(State)
    # .filter(State.name == 'Louisiana').first()
    print('{}'.format(louisiana.id))
    session.close()


if __name__ == '__main__':
    """execute the main function"""
    main()
