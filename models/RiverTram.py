from models.WaterTransport import WaterTransport

class RiverTram(WaterTransport):

    def __init__(self, transport_capacity, transport_max_speed, transport_consuption, color):
        super().__init__(transport_capacity, transport_max_speed, transport_consuption)
        self.color = color