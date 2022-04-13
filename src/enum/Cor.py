from enum import Enum

class Cor(Enum):
    BRANCO = "branco",
    CINZA = "cinza",
    PRETO = "preto"

    def __eq__(self, obj):
        return self.value == obj.value


