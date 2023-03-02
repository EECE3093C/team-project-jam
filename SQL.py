import sqlalchemy
import numpy as np
import pandas as pd
import os
from sqlalchemy import select
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
class Base(DeclarativeBase):
     pass
class BackLog(Base):
    __tablename__ = "BackLog"

    QueueID: Mapped[int] = mapped_column(primary_key= True, autoincrement= True)
    Song: Mapped[str] = mapped_column(String(300))
    Artist: Mapped[str] = mapped_column(String(300))
    URL: Mapped[str] = mapped_column(String)
    UserId: Mapped[int] = mapped_column()

class MasterQueue(Base):
    __tablename__ = "MasterQueue"

    QueueID: Mapped[int] = mapped_column(primary_key= True, autoincrement= True)
    Song: Mapped[str] = mapped_column(String(300))
    Artist: Mapped[str] = mapped_column(String(300))
    URL: Mapped[str] = mapped_column(String)
    UserId: Mapped[int] = mapped_column()
    UserQueuePosition: Mapped[int] = mapped_column()

class UserList(Base):
    __tablename__ = "UserList"

    UserID: Mapped[int] = mapped_column(primary_key= True, autoincrement= True)
    User: Mapped[str] = mapped_column(String(300))
    Host: Mapped[int] = mapped_column()
    Connection: Mapped[str] = mapped_column(String,nullable= True)
    Rank: Mapped[int] = mapped_column()
def BuildDb():
    dbEngine=sqlalchemy.create_engine(f'sqlite:////Query.db') #make path variable pull from web front end
    Base.metadata.create_all(dbEngine)
    return link,dbEngine
def AddUser(Name,Host,engine):
    with Session(engine) as session:
        NewUser = UserList(
            User = Name,
            Host = Host,
            Rank = 0,
        )
        session.add_all([NewUser])
        session.commit()
def AddSong(Song,Artist,URL,UserId,engine):
    with Session(engine) as session:
        stmt = select(MasterQueue.UserQueuePosition).where(MasterQueue.UserId.in_([UserId]))
        if stmt == None:
            UserQueuePos = 0
        else:
            UserQueuePos = stmt.max() + 1
        Song = MasterQueue(
            Song = Song,
            Artist = Artist,
            URL = URL,
            UserId = UserId,
            UserQueuePosisiton = UserQueuePos,
        )
        session.add_all([Song])
        session.commit()
BuildDb()
print("hello World")
        

    


