Para o presente cogido utilizou-se as bibliotecas pygame, time e pygame_menu, que podem ser baixadas
pelo serguinte processo:
no prompt de comando:
pip install pygame (*para a biblioteca pygame*)

pip install pygame-menu -U (instruções retiradas do seguinte link:https://github.com/ppizarror/pygame-menu)

o jogo se baseia no jogo classico bomberman, o menu principal mostra as opcoes de 1, 2 jogadores ou sair.
o jogo se inicia com os jogadores+ alien+fantasma+ 1 outro inimigo, os outros inimigos aparecem a cada 2 segundos,
de uma nave que e seu quartel general.
Quando mortos nao voltam a vida.

O jogo foi desenvolvido com as classes separade de inimigos, alien, fantasma, mapa, jogo, menu, quartel, personagem, projetil, explosao, config, bomba.

O menu executa as funcoes principais, como mostra o menu e "decorar", e tambem chamar a funcao jogo da classe jogo.

A classe jogo realiza as principais funcoes do programa, como gerar o mapa com uma base de lista de listas, 
realiza as configuraçoes iniciais como carregar  as imagens e ultiliza a escala "tile_size" que é uma proporcao do tamanho da tela
do dispositivo que esta rodando, cada "tile_size" representa a largura e altura de cada bloco desenhado na superficie.

As classes quartel, personagem, fantasma, inimigos, alienigena tem praticamente as mesmas funcoes, com algumas alteraç~eos chaves,


