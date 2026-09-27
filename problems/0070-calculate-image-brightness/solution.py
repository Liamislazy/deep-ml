import numpy as np

def calculate_brightness(img):
	# Write your code here
	try:
		image = np.array(img)
		if image.ndim != 2 or image.size == 0 or np.any(image < 0) or np.any(image > 255):
			return -1
		return float(np.mean(image))
	except Exception:
		return -1