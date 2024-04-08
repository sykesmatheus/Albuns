import pickle
import os
class Album:
    auxid = 1
    albuns = {}

    def __init__(self, nome, artista, genero, ano):
        self.id = Album.auxid
        Album.auxid += 1
        self.nome = nome
        self.artista = artista
        self.genero = genero
        self.ano = ano
        Album.albuns[self.id] = self

    def listar(self, listid):
        for id, album in enumerate(listid):
            print(f"ID: {id +1}\nNome do Álbum: {album.nome}\nArtista: {album.artista}\nGênero: {album.genero}\nAno de Estreia do Álbum: {album.ano}")


    def excluir(self, id, listalb):
        for album in listalb:
            if album.id == id:
                listalb.remove(album)
                print("Álbum excluído com sucesso.")
                return
            
        print("Álbum não encontrado.")

    def alterar(self, id, nome, artista, genero, ano, listalb):
        for album in listalb:
            if album.id == id:
                album.nome = nome
                album.artista = artista
                album.genero = genero
                album.ano = ano
                print("Álbum alterado com sucesso.")
                return
            
               
        print("Álbum não encontrado.")

    def arquivo(self, nomearquivo):
        with open(nomearquivo, "w") as arquivo:
            for id, album in Album.albuns.items():
                arquivo.write(f"ID: {id}\n")
                arquivo.write(f"Nome do Album: {album.nome}\n")
                arquivo.write(f"Artista: {album.artista}\n")
                arquivo.write(f"Genero: {album.genero}\n")
                arquivo.write(f"Ano de Estreia do Album: {album.ano}\n")
                arquivo.write("\n")
        print(f"Dados dos álbuns salvos em arquivo: {nomearquivo}")
    def top(self, listlb):
        rap = 0
        rock = 0
        pop = 0
        outros = 0
        for album in listlb:
            if album.genero == 'Rap':
                rap+=1
            elif album.genero == 'Rock':
                rock+=1
            elif album.genero == "Pop":
                pop+=1
            else:
                outros +=1
        if rock > rap and rock > pop and rock > outros:
            print("\nAQUI É ROCK PORRAAA")

        elif pop > rap and rock < pop and pop > outros:
            print("\nPop é o gênero predominante nos albuns catalogados")
        elif rock < rap and rap > pop and rap > outros:
            print("\nRap é o gênero predominante nos albuns catalogados")
        else:
            print("\n Seu gosto musical n pode ser classificado, então ""outros"" é sua categoria predominante")
    def binario_salvar(self, nomearquivo):
       
        with open(nomearquivo, "wb") as arq:
            pickle.dump(self, arq)
        print("Arquivo salvo com sucesso!")
       
           
            
    def binario_ler(self, nomearquivo):
        if os.path.exists(nomearquivo):
            with open(nomearquivo, "rb") as arq:
                dados = pickle.load(arq)
            print("Dados lidos com sucesso!")

        else:
            print(f"O arquivo {nomearquivo} não existe.")

        


            
        