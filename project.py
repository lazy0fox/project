class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[-1] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 0
        self.top = 0
        self.cell_size = 20

        self.a = -1

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(screen, pygame.Color('white'), [(self.left + j * self.cell_size, self.top + \
                                                                  i * self.cell_size),
                                                                 (self.cell_size, self.cell_size)], 1)
        if self.a != -1:
            for i in range(self.height):
                for j in range(self.width):
                    if self.board[i][j] % 2 == 0 and self.board[i][j] >= 0:
                        pygame.draw.line(screen, pygame.Color('green'), (j * self.cell_size + 2, i * self.cell_size + 2) \
                                         , (j * self.cell_size + self.cell_size - 4,
                                            i * self.cell_size + self.cell_size - 4))
                        pygame.draw.line(screen, pygame.Color('green'), (j * self.cell_size + self.cell_size - 4, \
                                                                         i * self.cell_size + 2),
                                         (j * self.cell_size + 2, i * self.cell_size + self.cell_size - 4))
                    elif self.board[i][j] >= 0:
                        pygame.draw.circle(screen, pygame.Color('red'), (j * self.cell_size + self.cell_size // 2, i \
                                                                         * self.cell_size + self.cell_size // 2),
                                           self.cell_size // 2 - 2)
        for i in range(self.height):  # по горизонтали
            for j in range(self.width - 5):
                check = self.board[i][j:j + 5]
                numbers = set(check)
                if -1 not in numbers and len(numbers) == 1:
                    if 1 in numbers:
                        pygame.draw.circle(screen, pygame.Color('red'), (350, 250), 249)
                        break
                    else:
                        pygame.draw.line(screen, pygame.Color('green'), (0, 0), (700, 500), 5)
                        pygame.draw.line(screen, pygame.Color('green'), (700, 0), (0, 500), 5)
                        break

        for i in range(self.height - 5):  # по вертикали
            for j in range(self.width):
                check = []
                for h in range(5):
                    check.append(self.board[i + h][j])
                numbers = set(check)
                if -1 not in numbers and len(numbers) == 1:
                    if 1 in numbers:
                        pygame.draw.circle(screen, pygame.Color('red'), (350, 250), 249)
                        break
                    else:
                        pygame.draw.line(screen, pygame.Color('green'), (0, 0), (700, 500), 5)
                        pygame.draw.line(screen, pygame.Color('green'), (700, 0), (0, 500), 5)
                        break

        for i in range(self.height - 5):  # по диагонали слева направо
            for j in range(self.width - 5):
                check = []
                for h in range(5):
                    check.append(self.board[i + h][j + h])
                numbers = set(check)
                if -1 not in numbers and len(numbers) == 1:
                    if 1 in numbers:
                        pygame.draw.circle(screen, pygame.Color('red'), (350, 250), 249)
                        break
                    else:
                        pygame.draw.line(screen, pygame.Color('green'), (0, 0), (700, 500), 5)
                        pygame.draw.line(screen, pygame.Color('green'), (700, 0), (0, 500), 5)
                        break

        for i in range(4, self.height):  # по диагонали справа налево
            for j in range(self.width - 5):
                check = []
                for h in range(5):
                    check.append(self.board[i - h][j + h])
                numbers = set(check)
                if -1 not in numbers and len(numbers) == 1:
                    if 1 in numbers:
                        pygame.draw.circle(screen, pygame.Color('red'), (350, 250), 249)
                        break
                    else:
                        pygame.draw.line(screen, pygame.Color('green'), (0, 0), (700, 500), 5)
                        pygame.draw.line(screen, pygame.Color('green'), (700, 0), (0, 500), 5)
                        break

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def get_cell(self, mouse_pos):
        return mouse_pos[0] // self.cell_size, mouse_pos[1] // self.cell_size

    def on_click(self, cell_coords):
        if cell_coords != None:
            self.y = cell_coords[0]
            self.x = cell_coords[1]
            if self.board[self.x][self.y] == -1:
                self.a += 1
                self.a %= 2
                self.board[self.x][self.y] = self.a


import pygame

pygame.init()
size = width, height = 700, 500
screen = pygame.display.set_mode(size)

board = Board(35, 25)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            board.get_click(mouse_pos)
    screen.fill((0, 0, 0))
    board.render()
    pygame.display.flip()
