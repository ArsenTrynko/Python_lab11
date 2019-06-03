class Manager:

    def __init__(self, list):
        self.list = list

    def findForMaxSpeed(self, transport_max_speed):
        return list(filter(lambda transport:transport.transport_max_speed == transport_max_speed, self.list))

    def findForCapacity(self, transport_capacity):
        return list(filter(lambda transport:transport.transport_capacity == transport_capacity, self.list))

    def sortByConsuptionv(self, reverse):
        return sorted(self.list, key=lambda transport:transport.transport_consuption, reverse=reverse)