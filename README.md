# Padloper - Projetando uma game engine por subtração

Este repositório foi criado para o meu projeto de conclusão de curso pelo CEFET/RJ, no curso de Sistemas de Informação. 

### O que é o Padloper? 

Padloper é uma ferramenta que visa ser uma game engine para a construção de jogos arcades simples, com foco total no primeiro contato de alguém com a programação de jogos. 

### Como o Padloper é construído? 

A ferramenta é construída em algumas partes, que compõem o todo do software. Abaixo estão descritas as ferramentas e suas funções:

#### Game Map (Mapa de Jogo): 
    O mapa de jogo é um arquivo JSON que será o guia, ou a planta do jogo. O software está preparado para ler o arquivo e usar as informações nele contidas para construir o jogo. 

    Um mapa de jogo típico do Padloper é assim construído:

    ```
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

    ```
