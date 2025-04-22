import numpy as np
import pygame
from PIL import Image


def array_to_surface(array: np.ndarray):
    return pygame.transform.rotate(pygame.surfarray.make_surface(array[:, :, :3]), -90)


def load_image(path: str):
    with Image.open(path) as img:
        return np.array(img)
