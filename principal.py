class produtos:
    def __init__(self, frances, pao_doce, pao_caseiro):
        self._frances = frances
        self._pao_doce = pao_doce
        self._pao_caseiro = pao_caseiro

    def adiciona_frances(self, kg_frances):
        return self._frances + kg_frances

    def perca_frances(self, perca):
        self._frances -= perca

    @property
    def frances(self):
        return self._frances


dia1 = produtos(12, 10, 2)
dia1.perca_frances(3)

print(dia1.frances)

