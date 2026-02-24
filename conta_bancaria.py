class ContaBancaria:

    def __init__(self, titular: str, saldo: float):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    def __str__(self):
        return f"Titular: {self._titular} | Saldo: {self._saldo} | Status: {self.ativo}"

    def ativar_conta(self):
        self._ativo = True

    @property
    def ativo(self):
        return f"{"☑" if self._ativo else "☐"}"


gugu = ContaBancaria("Gugu", 10)
guga = ContaBancaria("Guga", 15)
gugu.ativar_conta()
print(gugu)
print(guga)

print(gugu._titular)