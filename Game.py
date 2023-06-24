from enum import Enum

class Game(object):
  def __new__(cls): # Creating singleton
    if not hasattr(cls, 'instance'):
      cls.instance = super(Game, cls).__new__(cls)
    return cls.instance

  status: Enum = Enum('status', ['idle', 'playing', 'pause'])
