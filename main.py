from models.WaterTransport import WaterTransport
from models.RiverTram import RiverTram
from models.MotorShip import MotorShip
from manager.Manager import Manager

def main():
    waterTransport = WaterTransport(20, 36, 44.4)
    riverTram = RiverTram(34, 55, 33.4, "green")
    motorShip = MotorShip(55, 33, 22.5, "disel")

    manager = Manager([waterTransport, riverTram, motorShip])

    print(manager.findForCapacity(34))
    print(manager.findForMaxSpeed(33))
    print(manager.sortByConsuptionv(False))

if __name__ == '__main__':
    main()