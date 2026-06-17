class Device:
    def turn_on(self):
        pass

    def turn_off(self):
        pass

    def set_state(self, state):
        pass

class TV(Device):
    def __init__(self, brand):
        self.brand = brand
        self.is_on = False
        self.channel = "1"

    def turn_on(self):
        self.is_on = True
        print(f"{self.brand} TV включён")

    def turn_off(self):
        self.is_on = False
        print(f"{self.brand} TV выключен")

    def set_state(self, state):
        if self.is_on:
            self.channel = state
            print(f"{self.brand} TV переключён на канал {state}")
        else:
            print(f"{self.brand} TV выключен, нельзя сменить канал")

class Light(Device):
    def __init__(self, brand):
        self.brand = brand
        self.is_on = False
        self.brightness = "0%"

    def turn_on(self):
        self.is_on = True
        print(f"{self.brand} лампа включена")

    def turn_off(self):
        self.is_on = False
        print(f"{self.brand} лампа выключена")

    def set_state(self, state):
        if self.is_on:
            self.brightness = state
            print(f"{self.brand} лампа установлена на {state} яркости")
        else:
            print(f"{self.brand} лампа выключена, нельзя изменить яркость")

class SonyTV(TV):
    def __init__(self):
        super().__init__("Sony")

class SamsungTV(TV):
    def __init__(self):
        super().__init__("Samsung")

class PhilipsLight(Light):
    def __init__(self):
        super().__init__("Philips")

class IKEALight(Light):
    def __init__(self):
        super().__init__("IKEA")