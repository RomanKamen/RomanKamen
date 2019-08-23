from sqlalchemy import Column, Integer, String

from GameEngine.database import Base


class CardModel(Base):
    __tablename__ = 'cards'
    id = Column(Integer, primary_key=True)

    name = Column(String(64), nullable=False)
    description = Column(String(128))
    image = Column(String(256))

    hp = Column(Integer, nullable=False)
    armor = Column(Integer, nullable=False, default=0)
    damage = Column(Integer, nullable=False)
    manacost = Column(Integer, nullable=False)
    race = Column(String(32), nullable=False, default='keril')