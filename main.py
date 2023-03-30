class Ator:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return self.name


class Filme:
    def __init__(self, titulo, diretor, ano, atores):
        self.titulo = titulo
        self.diretor = diretor
        self.ano = ano
        self.atores = atores
        
    def __str__(self):
        return "{} ({})".format(self.titulo, self.ano)

def ler_dados(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        
    filmes = []
    atores = {}
    
    for line in lines[1:]:
        line = line.strip()
        fields = line.split(",")
        
        titulo = fields[0]
        diretor = fields[1]
        ano = int(fields[2])
        nomes_atores = fields[3].split(",")
        
        # Cria instâncias de ator, se necessário
        ator_instancias = []
        for name in nomes_atores:
            if name not in atores:
                atores[name] = Ator(name)
            ator_instancias.append(atores[name])
        
        filme = Filme(titulo, diretor, ano, ator_instancias)
        filmes.append(filme)
        
    return filmes

def informa_elenco(filme):
    print("Elenco de {}:".format(filme))
    for ator in filme.atores:
        print("- {}".format(ator))


def informa_direcao_filmes(diretor, filmes):
    print("Filmes dirigidos por {}:".format(diretor))
    for filme in filmes:
        if filme.diretor == diretor:
            print("- {} ({})".format(filme.titulo, filme.ano))

filmes = ler_dados("movies.csv")

# Informa o elenco de cada filme
for filme in filmes:
    informa_elenco(filme)
    print()

# Reporta os filmes dirigidos por Peter Jackson
informa_direcao_filmes("Peter Jackson", filmes)
