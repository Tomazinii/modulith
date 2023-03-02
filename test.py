


class MeuErro(BaseException):
    def __init__(self, message,*args: object) -> None:
        self.message = message
        super().__init__(*args)
    
    def message(self):
        return self.message




try:
    # Se a operação não levantou o erro, levantamos o nosso erro personalizado
    raise MeuErro("Ocorreu um erro personalizado!")

except MeuErro as erro:
    print(f"Erro personalizadosssssssssssss: {erro.message}")
