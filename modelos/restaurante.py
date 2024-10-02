from avaliacao import Avaliacao


class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        # a propriedade .title deixa a primeira letra maiuscula
        self.nome = nome.title()
        # a propriedade upper deixa todas as letras maiusculas
        self.categoria = categoria.upper()
        # atributo protegido,não deixa com que ocorra modificação
        self._ativo = False
        self._avaliacao = []
        # self->Referência da instância que esta sendo referenciada
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"{self.nome}  |  {self.categoria}"
    # trata-se de um metodo da classe

    @classmethod
    def listar_restaurantes(cls):
        print(f"{'Nome do Restaurante'.ljust(20)} | {
              'Categoria'.ljust(10)} | {'Avaliação'.ljust(10)} | {'Ativo'}")
        for restaurante in cls.restaurantes:
            print(f"{restaurante.nome.ljust(20)} | {restaurante.categoria.ljust(10)} | "
                  f"{str(restaurante.media_avaliacoes).ljust(10)} | {restaurante.ativo}")

    # Vamos alterar a forma como ele será lido:
    @property
    def ativo(self):
        return "✔️" if self._ativo else "❌"

    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota < 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    # Precisa ser capaz de ler essas informações

    @property
    def media_avaliacoes(self):
        # se não tiver nenhuma avaliação retorna 0
        if not self._avaliacao:
            return "-"
        # Pega todas as notas em avaliação mas a unica coisa que eu quero que some é a nota
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        # arredondas o número de casas decimais
        media = round(soma_das_notas/quantidade_de_notas, 1)
        return media
# instância->Será definida no programa principal app.py
# restaurante_praca = Restaurante("praça", "Gourmet")
# restaurante_praca.alternar_estado()
# restaurante_pizza = Restaurante("pizza Express", "Italiano")
# Atributos da instância
# restaurante_praca.nome = "Praça"
# restaurante_praca.categoria = "Gourmet"


# restaurantes = [restaurante_praca, restaurante_pizza]

# Vars->Acessar informações de um atributo
# Dirs->tudo o que vem dentro da classe
# print(restaurante_praca)

# Restaurante.listar_restaurantes()
