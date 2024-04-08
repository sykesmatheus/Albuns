import time
import os
from catalogo import *
def main():
    op = 0
    cont = 0
    listalb = []
    while op != 9:
        
        print("\n\tCATÁLOGO DE ÁLBUNS\n")
        print("1 - Adicionar um novo álbum")
        print("2 - Listar todos os álbuns")
        print("3 - Atualizar um álbum")
        print("4 - Excluir um álbum")
        print("5 - Salvar dados em arquivo txt")
        print("6 - Classificar gêneros mais ouvidos")
        print("7 - Salvar em arquivo Binário")
        print("8 - Ler arquivo Binário existente")
        print("9 - Sair do programa")
        op = int(input("\nDigite a opção desejada: "))
        os.system("cls")
        if op == 1:
            j = int(input("Quantos álbuns deseja adicionar? "))
            for i in range(j):
                nome = input("\nNome do álbum: ").capitalize()
                artista = input("De qual artista é este album? ").capitalize()
                genero = input("Gênero musical do álbum: ").capitalize()
                
                try:
                    ano = int(input("Ano de lançamento do álbum: "))
                    album = Album(nome, artista, genero, ano)
                    listalb.append(album)
                    cont += 1
                except ValueError:
                    print("Não é possível inserir letras no ano de lançamento!")
                    print("O código será parado em 5 segundos.")
                    for i in range(6):
                        print(i)
                        time.sleep(1)
                    op = 5
                    break
        

        elif op == 2:
            if len(listalb) == 0:
                print("\nimpossivel exibir catalogo vazio")
            else:
                album.listar(listalb)

        elif op == 3:
            if len(listalb) == 0:
                print("impossivel atualizar catalogo vazio")
            else:
                id = int(input("Digite o ID do álbum a ser atualizado: "))
                nome = input("Digite o novo nome do álbum: ").capitalize()
                artista = input("Digite o novo nome do artista: ").capitalize()
                genero = input("Digite o novo gênero do álbum: ").capitalize()
                ano = int(input("Digite o novo ano de lançamento do álbum: "))
                album.alterar(id, nome, artista, genero, ano, listalb) 

        elif op == 4:
            if len(listalb) == 0:
                print("\nimpossivel excluir catalogo vazio")
            else:
                id = int(input("\nDigite o ID do álbum a ser excluído: "))
                album.excluir(id,listalb) 
        elif op == 5:
            if len(listalb) == 0:
                print("\nimpossivel salvar catalogo vazio")
            else:
                nomearquivo = str(input("Digite um nome para o arquivo: ")) + str(cont) + ".txt"
                try:
                    print("\n Aguarde enquanto salvamos em um arquivo txt")
                    time.sleep(2)
                    album.arquivo(nomearquivo)
                except Exception as e:
                    print("Ocorreu algum erro, por favor tente novamente.")

        elif op == 6:
            if len(listalb) == 0:
                print("Impossivel classificar catalogo vazio")
            else:
                print("Espere enquanto analisamos")
                time.sleep(2)
                album.top(listalb)
        elif op == 7:
            if len(listalb) == 0:
                print("\nimpossivel salvar catalogo vazio")
            else:
                nomearquivo = str(input("Digite um nome para o arquivo: ")) + str(cont) + ".bin"
                try:
                    print("\n Aguarde enquanto salvamos em um arquivo binario")
                    time.sleep(2)
                    album.binario_salvar(nomearquivo)
                except Exception as e:
                    print("Ocorreu algum erro, por favor tente novamente.")
        elif op == 8:
            nomearquivo = str(input("Digite o nome do arquivo para ser lido: ")) + ".bin"
            album.binario_ler(nomearquivo)

        elif op == 9:
            time.sleep(3)
            print("\nSaindo do programa.")

        else:
            print("\nOpção inválida. Tente novamente.")

main()