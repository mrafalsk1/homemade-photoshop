import numpy as np


def binarize(image, factor):
    """Convert image to binary based on threshold"""
    # Convert to grayscale if it's a color image
    if len(image.shape) == 3:
        gray = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])
    else:
        gray = image.copy()

    # Apply threshold
    binary = np.where(gray >= factor, 255, 0).astype(np.uint8)

    # If the original image was color, convert back to 3 channels
    if len(image.shape) == 3:
        return np.stack([binary, binary, binary], axis=2)
    return binary


def contrast(image, factor):
    """Adjust image contrast"""
    # Create a copy to avoid modifying the original
    result = image.copy().astype(np.float32)

    # Calculate the mean brightness
    if len(image.shape) == 3:
        mean = np.mean(image, axis=(0, 1))
    else:
        mean = np.mean(image)

    # Apply contrast adjustment
    result = (result - mean) * factor + mean

    # Clip values to valid range [0, 255]
    result = np.clip(result, 0, 255).astype(np.uint8)

    return result


def _to_grayscale(image):
    """Convert color image to grayscale"""
    # If already grayscale, return as is
    if len(image.shape) == 2:
        return image

    # Convert to grayscale using weighted method
    gray = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)

    # Return as 3-channel grayscale
    return np.stack([gray, gray, gray], axis=2)


def isolate_color(image, tolerance, target_color=[255, 0, 0]):
    """Isolate a specific color, turning the rest to grayscale"""
    # Ensure image is color
    if len(image.shape) < 3:
        return image

    gray_image = _to_grayscale(image)

    target = np.array(target_color)
    print(target)
    distances = np.sqrt(np.sum((image[:, :, :3] - target) ** 2, axis=2))

    mask = distances <= tolerance

    result = gray_image.copy()

    for i in range(3):
        channel = result[:, :, i]
        channel[mask] = image[:, :, i][mask]
        result[:, :, i] = channel

    return result
