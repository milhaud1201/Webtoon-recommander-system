from load_img import image_loader
from extract_style import extract_style_loss
from extract_style import pca
from average_style import avgList

import pandas as pd

def extract_loss_and_save(no):
    style_dir = f'/file_path/image{no}/'
    data = image_loader(style_dir)
    total_arr, label_arr = extract_style_loss(data)
    result = pca(total_arr)
    avglist = avgList(result, label_arr)

    df = pd.DataFrame(avglist, index=data.class_to_idx)
    file_name = f"nw{no}.csv"
    df.to_csv(f'/file_path/losses/{file_name}')
