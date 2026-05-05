import numpy as np
from PIL import Image 
def ft_load(path: str)-> np.ndarray:
    try:
        img = Image.open(path)
        arr = np.array(img)
        # print(f'The shape of image is: {arr.shape}')
        return(arr)
    except Exception:
        return("Could not open file")