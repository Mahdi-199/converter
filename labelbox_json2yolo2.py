import json
import os
from pathlib import Path

import requests
import yaml
from PIL import Image
from tqdm import tqdm

# from utils import make_dirs
# import utils
from os import makedirs


def convert(file, zip=True):
    # Convert Labelbox JSON labels to YOLO labels
    names = []  # class names
    file = Path(file)
    save_dir = makedirs(file.stem)
    with open(file) as f:
        data = json.load(f)  # load JSON
    #for img in tqdm(data, desc=f'Converting {file}'):
        im_path = data['imagePath']
        
        img_name=im_path.split("\\")
        img_name=img_name[1]
        
        im = Image.open(im_path)  # open
        width, height = im.size  # image size
        image_path = save_dir / 'images' / img_name
        im.save(image_path, quality=95, subsampling=0)
        aa=((data['shapes'])[0])["points"]
        xy=''
        for i in aa:
            xy=xy+' '+str(i[0]/width)+' '+str(i[1]/height)+' '
        # class
        xy='0'+' '+xy
        dir_path=r"/home/muhammad/pipe/gray_scale/1-50/annotations/new"
        aaa=((str(Path(img_name))).split('.'))[0]+'.txt' 
        with open(os.path.join(dir_path,aaa), 'w') as f:
            f.write(xy)
            f.close()

    # # Save dataset.yaml
    # d = {'path': f"../datasets/{file.stem}  # dataset root dir",
    #      'train': "images/train  # train images (relative to path) 128 images",
    #      'val': "images/val  # val images (relative to path) 128 images",
    #      'test': " # test images (optional)",
    #      'nc': len(names),
    #      'names': names}  # dictionary

    # with open(save_dir / file.with_suffix('.yaml').name, 'w') as f:
    #     yaml.dump(d, f, sort_keys=False)

    # # Zip
    # if zip:
    #     print(f'Zipping as {save_dir}.zip...')
    #     os.system(f'zip -qr {save_dir}.zip {save_dir}')

    # print('Conversion completed successfully!')


if __name__ == '__main__':
    dir_path=r"/home/muhammad/pipe/gray_scale/1-50/annotations"
    for path in os.listdir(dir_path):
        file_path = os.path.join(dir_path,path)
        print('file_path=',file_path)
        convert(file_path)
        
