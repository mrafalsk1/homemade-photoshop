import pygame
import os
import utils


class App:
    def __init__(self):
        pygame.init()
        self.colors = {
            "white": (255, 255, 255),
            "black": (0, 0, 0),
            "gray": (220, 220, 220),
            "green": (0, 255, 0),
            "red": (255, 0, 0),
            "blue": (0, 0, 255),
            "yellow": (255, 255, 0),
            "purple": (128, 0, 128),
        }
        self.WIDTH = 1200
        self.HEIGHT = 800
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Manipulacao de Imagens")
        self.font = pygame.font.SysFont("Arial", 30, bold=True)

        self.image_paths = self._get_image_paths()
        self.current_image_index = 0
        print(self.image_paths)
        # TO-DO
        self.original_image = utils.load_image(
            self.image_paths[self.current_image_index]
        )
        self.processed_image = self.original_image.copy()

        print(self.original_image)
        # TO-DO
        # Interface botoes sliders etc

        # TO-DO
        # filtros >:)

        self.running = True

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        keys = pygame.key.get_pressed()

    def _render(self):
        """
        Renderiza os elementos na tela
        """
        self.screen.fill(self.colors["white"])
        self._display_images()
        pygame.display.update()

    def _get_image_paths(self):
        images_dir = "images"
        image_files = [
            f for f in os.listdir(images_dir) if f.endswith((".png", ".jpg", ".jpeg"))
        ]
        return [os.path.join(images_dir, img) for img in image_files]

    def _display_images(self):
        original_surface = utils.array_to_surface(self.original_image)
        processed_surface = utils.array_to_surface(self.processed_image)

        display_width = (self.WIDTH - 100) // 2
        aspect_ratio = original_surface.get_width() / original_surface.get_height()
        display_height = int(display_width * aspect_ratio)

        original_surface = pygame.transform.scale(
            original_surface, (display_width, display_height)
        )
        processed_surface = pygame.transform.scale(
            processed_surface, (display_width, display_height)
        )

        original_x = 50
        processed_x = self.WIDTH - 50 - display_width
        y_pos = 50
        self.screen.blit(original_surface, (original_x, y_pos))
        self.screen.blit(processed_surface, (processed_x, y_pos))

        original_label = self.font.render("Imagem Original", True, self.colors["black"])
        processed_label = self.font.render(
            "Imagem Processada", True, self.colors["black"]
        )

        self.screen.blit(original_label, (original_x, y_pos - 30))
        self.screen.blit(processed_label, (processed_x, y_pos - 30))

    def run(self):
        while self.running:
            self._render()
            self._handle_events()
            pygame.time.Clock().tick(30)
        pygame.quit()


if __name__ == "__main__":
    app = App()
    app.run()
