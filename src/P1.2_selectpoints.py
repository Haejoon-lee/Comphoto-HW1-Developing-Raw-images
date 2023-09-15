# white_balance_selector.py

import numpy as np
import matplotlib.pyplot as plt

def select_white_point(image_path):
    # Load the image
    img = np.load(image_path)

    # Display the image
    plt.imshow(img)
    plt.title("Click on two points to define a rectangular patch")
    
    # Use ginput to select points
    coords = plt.ginput(4)
    plt.close()

    # Save the coordinates to a numpy array file
    np.save('selected_coords.npy', coords)

if __name__ == "__main__":
    select_white_point('img_ge.npy')
