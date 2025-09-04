import sys
from typing import List, Optional, Tuple

import pygame


class player:
    def __init__(
        self,
        HP: int,
        ataque: int,
        defensa: int,
        inventario: Optional[List[str]] = None,
        hechizos: Optional[List[str]] = None,
        posicion: Tuple[int, int] = (0, 0),
        velocidad: int = 5,
    ) -> None:
        self.HP = HP
        self.ataque = ataque
        self.defensa = defensa
        self.inventario = list(inventario) if inventario is not None else []
        self.hechizos = list(hechizos) if hechizos is not None else []
        self.x, self.y = posicion
        self.velocidad = velocidad

    def mover(self, dx: int, dy: int) -> None:
        self.x += dx * self.velocidad
        self.y += dy * self.velocidad


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Mi ventana Pygame 800x600")
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((30, 30, 30))
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()

