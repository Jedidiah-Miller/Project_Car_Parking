'''
a parking space
'''
class ParkingSpace(object):

  def __init__(self, n: int, plate: str=None, color: str=None):
    self.number = n
    self.plate = plate
    self.color = color