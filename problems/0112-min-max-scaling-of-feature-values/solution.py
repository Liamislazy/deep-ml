def min_max(x: list[float]) -> list[float]:
    """
    Perform Min-Max normalization to scale values to [0, 1].
    
    Args:
        x: A list of numerical values
    
    Returns:
        A new list with values normalized to [0, 1]
    """
    x_max = max(x)
    x_min = min(x)
    scaled_list = []
    for value in x:
        scaled_list.append((value - x_min)/(x_max-x_min))
    return scaled_list