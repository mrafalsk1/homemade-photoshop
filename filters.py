import numpy as np
from scipy import ndimage


def gaussian_filter(image, sigma=1.0):
    """Apply Gaussian filter to an image"""
    # If image is color (3D array), apply to each channel
    if len(image.shape) == 3:
        result = np.zeros_like(image)
        for i in range(image.shape[2]):
            result[:, :, i] = ndimage.gaussian_filter(image[:, :, i], sigma=sigma)
        return result
    else:
        # For grayscale image
        return ndimage.gaussian_filter(image, sigma=sigma)


def laplacian_filter(image):
    """Apply Laplacian filter to detect edges"""
    # Convert to grayscale if color image
    if len(image.shape) == 3:
        gray = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])
    else:
        gray = image.copy()

    # Define Laplacian kernel
    kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])

    # Apply convolution
    result = ndimage.convolve(gray, kernel)

    # Normalize to 0-255 range
    result = result - np.min(result)
    if np.max(result) > 0:
        result = (result / np.max(result)) * 255

    # Convert back to uint8
    result = result.astype(np.uint8)

    # If original was color, create a 3-channel output
    if len(image.shape) == 3:
        return np.stack([result, result, result], axis=2)
    return result
