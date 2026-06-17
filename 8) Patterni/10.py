class LightingSystem:
    def __init__(self):
        self.is_on = False
        self.brightness = 50

    def turn_on(self):
        self.is_on = True
        return "Освещение: включено"

    def turn_off(self):
        self.is_on = False
        return "Освещение: выключено"

    def set_brightness(self, value):
        self.brightness = value
        return "Яркость освещения установлена на " + str(value) + "%"

    def get_status(self):
        if self.is_on:
            return "Освещение: включено | " + str(self.brightness) + "%"
        else:
            return "Освещение: выключено"

class ClimateControlSystem:
    def __init__(self):
        self.is_on = False
        self.temperature = 22
        self.special_mode = False

    def turn_on(self):
        self.is_on = True
        return "Климат-контроль: включен"

    def turn_off(self):
        self.is_on = False
        return "Климат-контроль: выключен"

    def set_temperature(self, value):
        self.temperature = value
        return "Температура установлена на " + str(value) + "°C"

    def turn_on_special_climate_mode(self):
        self.special_mode = True
        return "Особый климат-режим активирован"

    def turn_off_special_climate_mode(self):
        self.special_mode = False
        return "Особый климат-режим выключен"

    def get_status(self):
        if self.is_on:
            result = "Климат-контроль: включен, температура " + str(self.temperature) + "°C"
        else:
            result = "Климат-контроль: выключен"
        if self.special_mode:
            result = result + "\nОсобый климат-режим активирован"
        return result

class SecuritySystem:
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        return "Сигнализация включена"

    def turn_off(self):
        self.is_on = False
        return "Сигнализация выключена"

    def get_status(self):
        if self.is_on:
            return "Сигнализация включена"
        else:
            return "Сигнализация выключена"

class MultimediaSystem:
    def __init__(self):
        self.is_on = False
        self.music_playing = False

    def turn_on(self):
        self.is_on = True
        return "Мультимедийная система: включена"

    def turn_off(self):
        self.is_on = False
        self.music_playing = False
        return "Мультимедийная система: выключена"

    def play_music(self):
        if self.music_playing:
            return ""
        self.music_playing = True
        return "Музыка включена"

    def stop_music(self):
        if not self.music_playing:
            return ""
        self.music_playing = False
        return "Музыка выключена"

    def get_status(self):
        if self.is_on:
            return "Мультимедийная система: включена"
        else:
            return "Мультимедийная система: выключена"

class SmartHomeFacade:
    def __init__(self):
        self.lighting = LightingSystem()
        self.climate = ClimateControlSystem()
        self.security = SecuritySystem()
        self.multimedia = MultimediaSystem()

    def get_all_systems_status(self):
        status = []
        status.append(self.lighting.get_status())
        status.append(self.climate.get_status())
        status.append(self.security.get_status())
        status.append(self.multimedia.get_status())
        return "\n".join(status)

    def home_mode(self):
        result = []
        result.append(self.lighting.turn_on())
        result.append(self.lighting.set_brightness(100))
        result.append(self.climate.turn_on())
        result.append(self.climate.set_temperature(22))
        result.append(self.security.turn_off())
        result.append(self.climate.turn_off_special_climate_mode())
        return result

    def party_mode(self):
        result = []
        result.append(self.lighting.turn_on())
        result.append(self.lighting.set_brightness(40))
        result.append(self.multimedia.turn_on())
        result.append(self.multimedia.play_music())
        result.append(self.climate.turn_on_special_climate_mode())
        return result

    def night_mode(self):
        result = []
        result.append(self.lighting.turn_off())
        result.append(self.climate.turn_on())
        result.append(self.climate.set_temperature(18))
        result.append(self.security.turn_on())
        result.append(self.multimedia.turn_off())
        result.append(self.climate.turn_off_special_climate_mode())
        return result

    def away_mode(self):
        result = []
        result.append(self.lighting.turn_off())
        result.append(self.climate.turn_off())
        result.append(self.multimedia.turn_off())
        result.append(self.security.turn_on())
        result.append(self.climate.turn_off_special_climate_mode())
        return result