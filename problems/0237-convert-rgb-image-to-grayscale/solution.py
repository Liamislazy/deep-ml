import numpy as np

def rgb_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminosity method.
    
    Args:
        image: RGB image as list or numpy array of shape (H, W, 3)
               with values in range [0, 255]
    
    Returns:
        Grayscale image as 2D list with integer values,
        or -1 if input is invalid
    """
    try:
        img = np.array(image)

        if img.ndim != 3 or img.shape[2] != 3 or img.size == 0:
            return -1
        if np.any(img < 0) or np.any(img > 255):
            return -1
        gray_image = img[:, :, 0] * 0.299 + img[:, :, 1] * 0.587 + img[:, :, 2] * 0.114
        return np.round(gray_image).astype(int)
    except Exception:
        return -1