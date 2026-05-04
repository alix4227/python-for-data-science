from load_image import ft_load
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image 
def zoom():
    arr = ft_load("animal.jpeg")
    print(arr)
    arr_zoomed = arr[100:500, 400:800]
    grey =  arr_zoomed[: , : , 1]
    img_back = Image.fromarray(grey)
    zoomed = img_back.resize((400, 400))
    zoomed_arr = np.array(zoomed)
    zoomed_arr = zoomed_arr[:, :, np.newaxis]
    print(
        f'New shape after slicing: {zoomed_arr.shape} or '
        f'{zoomed_arr.squeeze().shape}'
    )
    print(zoomed_arr)
    plt.imshow(zoomed_arr, cmap="gray")
    plt.savefig('output.png')


if __name__ == "__main__":
    zoom()