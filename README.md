# Snake Game

## Visão Geral

Snake Game é uma implementação simples e divertida do clássico jogo da cobrinha, desenvolvida em Python usando a biblioteca Pygame para a matéria de `Linguagem de programação aplicada` de minha faculdade. O jogo inclui um sistema de pontuação que rastreia e salva as maiores pontuações do jogador em um banco de dados SQLite. Ele é projetado para jogadores casuais que desejam reviver a nostalgia desse clássico enquanto acompanham suas conquistas.

## Recursos

- **Jogabilidade Clássica**: Controle a cobrinha, coma frutas para crescer e evite colisões.
- **Pontuação Dinâmica**: Rastreia a pontuação do jogador durante o jogo.
- **Armazenamento Persistente**: Salva as pontuações do jogador em um banco de dados SQLite.
- **Controles Intuitivos**: Jogue usando as setas do teclado para uma navegação suave.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Pygame**: Biblioteca para desenvolvimento de jogos e gráficos.
- **SQLite**: Banco de dados leve para armazenamento de pontuações.

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/gustaoliveira1/SnakeGame.git
cd SnakeGame
```

2. Crie um ambiente virtual:

```bash
# cria o venv
python -m venv .venv

# ativação do venv
# windows
.\.venv\Scripts\activate

# linux
source ./.venv/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute o jogo:

```bash
python run.py
```

## Como Jogar

1. Inicie o jogo.
2. Use as setas do teclado para mover a cobrinha.
3. Coma frutas para crescer e aumentar sua pontuação.
4. Evite colidir com o próprio corpo da cobrinha.
5. Sua pontuação é salva automaticamente ao final do jogo.

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para enviar um pull request ou abrir uma issue para sugerir melhorias.