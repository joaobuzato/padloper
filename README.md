# Padloper - Projetando uma game engine por subtração

  

Este repositório foi criado para o meu projeto de conclusão de curso pelo CEFET/RJ, no curso de Sistemas de Informação.

  

# O que é o Padloper?

  

Padloper é uma ferramenta que visa ser uma game engine para a construção de jogos arcades simples, com foco total no primeiro contato de alguém com a programação de jogos.

# Por que "Game Engine Por Subtração" ?

O termo 'por subtração' surge de 'design por subtração', atribuído ao game designer Fumito Ueda, diretor dos jogos Ico e Shadow of The Colossus, e se refere à retirada de tudo que não for essencial à forma, tornando o produto final mais enxuto, simples e de escopo bem reduzido. 

Tal filosofia se encaixa perfeitamente na proposta do Padloper, que foi pensada com foco total no primeiro contato de alguém com a construção de jogos, e por isso muitas das funcionalidades mais "comuns" de game engines mais tradicionais são removidas - subtraídas - para que a linha de aprendizado seja a mais suave possível. 

Uma pergunta importante a se fazer para garantir que um elemento é subtraível é: "Caso um jogo não possua tal elemento, ele ainda é um jogo?". Em casos como a interação do usuário, a resposta é certamente não. Um jogo sem interação do usuário é uma outra coisa, mas não um jogo. Já em casos como o áudio, no entanto, a resposta pode ser sim. Um jogo sem som ainda é um jogo. E é aqui que a subtração age. 

  

# Como o Padloper é construído?

  

A ferramenta é construída em algumas partes, que compõem o todo do software. Abaixo estão descritas as ferramentas e suas funções:

  

## Game Map (Mapa de Jogo):

  

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

Cada um dos elementos do mapa possui em si uma série de outros elementos, e além do "name", que é o título do jogo, são eles:


### Screen 

O Objeto de Tela de um jogo executado com Turtle é o espaço no qual os objetos são desenhados, ou seja, é o espaço onde o jogo realmente acontece. Um elemento de tela num mapa de jogo construído pelo Padloper é como descrito abaixo:

```
"screen" : {
	"width" : 1000,
	"height" : 1000,
	"color" : "green"
}
```


*Elementos*:

Width: Largura da tela;

Height: Altura da tela;

Color: Cor do backgroud;

  <hr>

### Scoreboard

O Objeto de Scoreboard é um ator que faz o papel de placar.

Atualmente há alguns métodos pré-definidos para este ator que não são comandados pelo mapa, mas já estão imbutidos no framework para auxiliar na construção do jogo. São eles:

  

- point() : concede mais um ponto para o jogador e atualiza o placar na tela.

- game_over() : finaliza o ciclo de jogo e mostra a pontuação final no centro da tela.

  

Um elemento de Scoreboard no mapa de jogo Padloper é como disposto abaixo:

```
"scoreboard": {
	"position" : "top"
	"color" : "black"
	"font" : "Courier"
	"size" : "18"
}
```
*Elementos*:

Position: Posição do placar na tela;
Color: Cor das letras do placar;
Font: Fonte da escrita do placar;
Size: Tamanho da escrita do placar;

### Actors

  O array 'Actors' do jogo é uma lista dos atores que estarão presentes na execução do jogo, incluindo tanto atores que o jogador controla quanto os inimigos ou outros assets não controlados pelo jogador. 

Um ator é possui dentro de si alguns objetos, como descrito abaixo: 
```
{
      "name" : "player",
      "components" : {
	      "speed" : 8
      },
      "spawn" : 
      {
        "type" : "unique",
        "positions" : [
          {"x" :0, "y" : 470}
        ],
        "colors" : [
          "red"
        ]
      },
      "behaviors" :
        {
          "inputs" : [
            {"key" :  "w", "action" : "forward", "param" :  "10"},
            {"key" :  "s", "action" :  "backward", "param" :  "10"},
            {"key" :  "a", "action" :  "strife_left", "param" :  "10"},
            {"key" :  "d", "action" :  "strife_right", "param" :  "10"}
          ]
        },
        {
          "updates": [
            { "action" : "strife_left", "param" :  "10"}

          ]
      },
    }
```

*Elementos*:

Name: Nome do ator;

Components: Atributos estáticos do ator; 
* Speed: Atributo de velocidade do ator na tela **( 1 - 10 )**;

Spawn: Objeto com os parâmetros de geração do ator na tela;
* Type: Tipo de geração **( unique | multiple )**;
* Positions : Array de posições que o ator pode assumir ao ser gerado. Caso o tipo de geração seja **multiple**, o ator será gerado numa destas coordenadas, aleatoriamente. 
	* x: Posição x onde o ator será gerado;
	* y: Posição y onde o ator seŕa gerado;
* Colors : Array de cores que o ator pode assumir ao ser gerado. Caso o tipo de geração seja **multiple**, o ator escolherá uma cor aleatoriamente.

Behaviors: Comportamentos que o ator pode possuir. Há dois tipos de ações que se encaixam dentro de "Behaviors": os inputs e os updates, e geralmente um mesmo ator não possui os dois simultaneamente. 
* Inputs: lista de ações que o ator tomará ao pressionar de uma tecla. Um input possui:
	* Key: Tecla que, quando pressionada, executará a ação definida;
	* Action: Ação executada ao pressionar a tecla (O que o ator fará com este comando é definido pelo software);
	* Param: Parâmetro com o qual a ação será executada, que pode ser, por exemplo, o número de pixels que um ator andará, quantos graus ele se voltará, etc; 

* Updates: lista de ações que serão executadas pelo ator a cada novo frame, sem necessidade de uma interação do usuário.
	* Action: Ação executada ao pressionar a tecla (O que o ator fará com este comando é definido pelo software);
	* Param:  Parâmetro com o qual a ação será executada, que pode ser, por exemplo, o número de pixels que um ator andará, quantos graus ele se voltará, etc; 



### Rules

Em construção

## Game Builder 

Em construção
