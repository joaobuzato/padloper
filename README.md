# Padloper - Projetando uma game engine por subtração

Este repositório foi criado para o meu projeto de conclusão de curso pelo CEFET/RJ, no curso de Sistemas de Informação. 

### O que é o Padloper? 

Padloper é uma ferramenta que visa ser uma game engine para a construção de jogos arcades simples, com foco total no primeiro contato de alguém com a programação de jogos. 

### Como o Padloper é construído? 

A ferramenta é construída em algumas partes, que compõem o todo do software. Abaixo estão descritas as ferramentas e suas funções:

#### Game Map (Mapa de Jogo): 
    O mapa de jogo é um arquivo JSON que será o guia, ou a planta do jogo. O software está preparado para ler o arquivo e usar as informações nele contidas para construir o jogo. 

    Um mapa de jogo típico do Padloper é assim construído:

    ``
    {
        "name" : "Padloper Game",
        "screen" : {},
        "scoreboard" : {},
        "rules" : [
            {
                "trigger" : "collision"
            }
        ],
        "actors" : [
            {
                "name": "jogador"
            }
        ]
    }
    ``

    ##### Cada um dos elementos do mapa possui em si uma série de outros elementos, e além do name, que é o título do jogo, são eles:

    ###### Screen
        O Objeto de Tela de um jogo executado com Turtle é o espaço no qual os objetos são desenhados, ou seja, é o espaço onde o jogo realmente acontece. Um elemento de tela num mapa de jogo construído pelo Padloper é como descrito abaixo:

        ``
        "screen" : {
            "width" : 1000,
            "height" : 1000,
            "color" : "green"
        }
        ``

        *Elementos*
        Width: Largura da tela;
        Height: Altura da tela;
        Color: Cor do backgroud;

    ###### Scoreboard 
        O Objeto de Scoreboard é um ator que faz o papel de placar. Atualmente há alguns métodos pré-definidos para este ator que não são comandados pelo mapa, mas já estão imbutidos no framework para auxiliar na construção do jogo. São eles:

        - point() : concede mais um ponto para o jogador e atualiza o placar na tela.
        - game_over() : finaliza o ciclo de jogo e mostra a pontuação final no centro da tela.

        Um elemento de Scoreboard no mapa de jogo Padloper é como disposto abaixo: 
        ``
        "scoreboard": {
            "position" : "top"
            "color" : "black"
            "font" : "Courier"
            "size" : "18"
        }
        ``

        *Elementos*
        Position: Posição do placar na tela;
        Color: Cor das letras do placar;
        Font: Fonte da escrita do placar;
        Size: Tamanho da escrita do placar;

    ##### Actors

    ##### Rules
    
