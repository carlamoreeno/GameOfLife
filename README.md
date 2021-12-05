# Game Of Life
Implementação do jogo "Game of Life" em Python.


## Regras
As regras do jogo "Game of Life" podem ser encontradas a partir do minuto 1:03 do vídeo "Math Has a Fatal Flaw" usado como material do curso (https://www.youtube.com/watch?v=HeQX2HjkcNo)

Em resumo (segundo https://pt.wikipedia.org/wiki/Jogo_da_vida):
> As regras são simples e elegantes:
> 
> 1 . Qualquer célula viva com menos de dois vizinhos vivos morre de solidão.
> 
> 2 . Qualquer célula viva com mais de três vizinhos vivos morre de superpopulação.
> 
> 3 . Qualquer célula morta com exatamente três vizinhos vivos se torna uma célula viva.
> 
> 4 . Qualquer célula viva com dois ou três vizinhos vivos continua no mesmo estado para a próxima geração.
> 
> É importante entender que todos os nascimentos e mortes ocorrem simultaneamente. Juntos eles constituem uma geração ou, como podemos chamá-los, um "instante" na história da vida completa da configuração inicial.


## Como Inicializar o Jogo
1. Abrir o arquivo .py usando a IDLE do Python:
![alt text](https://github.com/carlamoreeno/GameOfLife/blob/main/imagensTutorial/imagem1.png?raw=true)

2. Clicar em "Run" na barra superior e em seguida "Run... Customized" para configurar os parâmetros do programa:
![alt text](https://github.com/carlamoreeno/GameOfLife/blob/main/imagensTutorial/imagem2.png?raw=true)

3. Inserir o tamanho desejado para a grid do jogo da seguinte forma: insira 2 valores inteiros como parâmetro, altura e largura da grid, respectivamente:
![alt text](https://github.com/carlamoreeno/GameOfLife/blob/main/imagensTutorial/imagem3.png?raw=true)

4. A tela do jogo será aberta com os valores de grid escolhidos e será possível iniciar o jogo com as instruções em tela:
![alt text](https://github.com/carlamoreeno/GameOfLife/blob/main/imagensTutorial/imagem4.png?raw=true)


## Comandos
| Comando | Descrição |
| ------- | ------------- |
| i       | Inicializar o jogo aleatoriamente |
| space   | Rodar jogo / Pausar jogo |
| esc     | Sair  |
