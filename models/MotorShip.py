from models.WaterTransport import WaterTransport

class MotorShip(WaterTransport):
    def __init__(self, transport_capacity, transport_max_speed, transport_consuption, fuel_type):
        super().__init__(transport_capacity, transport_max_speed, transport_consuption)
        self.fuel_type = fuel_type