class Transport:
    pass

class WaterTransport(Transport):
    pass

class AirTransport(Transport):
    pass

class Aviation(AirTransport):
    pass

class Airplane(Aviation):
    pass

class Aeronautics(AirTransport):
    pass

class Airship(Aeronautics):
    pass

class AirBalloon(Aeronautics):
    pass

class GroundTransport(Transport):
    pass

class RailwayTransport(GroundTransport):
    pass

class Train(RailwayTransport):
    pass

class AutomobileTransport(GroundTransport):
    pass

class Car(AutomobileTransport):
    pass

class BicycleTransport(GroundTransport):
    pass

class Bicycle(BicycleTransport):
    pass

class AnimalPoweredTransport(GroundTransport):
    pass

class Chariot(AnimalPoweredTransport):
    pass

class SpaceTransport(Transport):
    pass

class Spaceship(SpaceTransport):
    pass