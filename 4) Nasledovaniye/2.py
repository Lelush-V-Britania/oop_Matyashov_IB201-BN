# Живые существа
class EntiaViventia:
    pass

# Бесклеточные
class Acellularia(EntiaViventia):
    pass

# Вирусы
class Virus(Acellularia):
    pass

# Клеточные
class Cellularia(EntiaViventia):
    pass

# Прокариоты
class Prokaryota(Cellularia):
    pass

# Бактерии
class Bacteria(Prokaryota):
    pass

# Эукариоты
class Eukaryota(Cellularia):
    pass

# Одноклеточные
class Unicellularia(Eukaryota):
    pass

# Грибы
class Fungi(Eukaryota):
    pass

# Растения
class Plantae(Eukaryota):
    pass

# Животные
class Animalia(Eukaryota):
    pass