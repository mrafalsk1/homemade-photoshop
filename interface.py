import pygame
import pygame_gui
from filters import gaussian_filter, laplacian_filter
from transformations import contrast, isolate_color, binarize


class Interface:
    def __init__(
        self, screen_width, screen_height, reset_image, next_image, prev_image
    ):
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.manager = pygame_gui.UIManager((self.screen_width, self.screen_height))
        self.panel_rect = pygame.Rect(0, screen_height - 200, screen_width, 200)

        self.button_widht = 120
        self.button_height = 40
        self.padding = 10
        self.start_y = self.screen_height - 180
        self.start_x = 50

        self._ui_buttons()
        self._filters()
        self._transformations()

        self.button_actions = {
            self.gaussian_button: gaussian_filter,
            self.laplacian_button: laplacian_filter,
            self.contrast_slider: contrast,
            self.binary_slider: binarize,
            self.isolate_color_slider: isolate_color,
        }
        self.interface_actions = {
            self.reset_button: reset_image,
            self.next_button: next_image,
            self.prev_button: prev_image,
        }

    def _filters(self):
        gaussian_rect = (
            pygame.Rect(
                self.start_x,
                self.screen_height - 180,
                self.button_widht,
                self.button_height,
            ),
        )[0]

        self.gaussian_button = pygame_gui.elements.UIButton(
            relative_rect=gaussian_rect,
            text="Gaussiano",
            manager=self.manager,
        )

        laplacian_rect = pygame.Rect(
            gaussian_rect[0] + self.padding + self.button_widht,
            gaussian_rect[1],
            self.button_widht,
            self.button_height,
        )

        self.laplacian_button = pygame_gui.elements.UIButton(
            relative_rect=laplacian_rect, text="Laplaciano", manager=self.manager
        )

    def _transformations(self):
        slider_width = 200
        slider_height = 20
        start_y = self.start_y + self.button_height + self.padding
        binary_label_rect = pygame.Rect(self.start_x, start_y, slider_width, 20)
        slider_start_y = binary_label_rect[1] + self.padding * 2.5
        self.binary_label = pygame_gui.elements.UILabel(
            relative_rect=binary_label_rect,
            text="Binarização",
            manager=self.manager,
        )
        self.binary_slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect(
                self.start_x, slider_start_y, slider_width, slider_height
            ),
            start_value=50,
            value_range=(0, 100),
            manager=self.manager,
        )
        contrast_label_rect = pygame.Rect(
            binary_label_rect[0] + self.padding + slider_width,
            start_y,
            slider_width,
            20,
        )
        self.contrast_label = pygame_gui.elements.UILabel(
            relative_rect=contrast_label_rect,
            text="Contraste",
            manager=self.manager,
        )
        self.contrast_slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect(
                contrast_label_rect[0],
                slider_start_y,
                slider_width,
                slider_height,
            ),
            start_value=1,
            value_range=(1, 100),
            manager=self.manager,
        )
        isolate_color_label_rect = pygame.Rect(
            contrast_label_rect[0] + self.padding + slider_width,
            start_y,
            slider_width,
            20,
        )
        self.isolate_color_label = pygame_gui.elements.UILabel(
            relative_rect=isolate_color_label_rect,
            text="Isolar Cor",
            manager=self.manager,
        )
        self.isolate_color_slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect(
                isolate_color_label_rect[0],
                slider_start_y,
                slider_width,
                slider_height,
            ),
            start_value=50,
            value_range=(0, 100),
            manager=self.manager,
        )
        pass

    def _ui_buttons(self):

        print(self.screen_width)
        self.reset_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                self.screen_width - self.start_x - self.button_widht,
                self.start_y,
                self.button_widht,
                self.button_height,
            ),
            text="Resetar",
            manager=self.manager,
        )
        self.next_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                self.screen_width - self.start_x - self.button_widht,
                self.start_y + self.padding + self.button_height,
                self.button_widht,
                self.button_height,
            ),
            text="Próxima",
            manager=self.manager,
        )
        self.prev_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                self.screen_width - self.start_x - self.button_widht * 2 - self.padding,
                self.start_y + self.padding + self.button_height,
                self.button_widht,
                self.button_height,
            ),
            text="Anterior",
            manager=self.manager,
        )
