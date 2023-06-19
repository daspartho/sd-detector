from urllib.request import urlretrieve
import shutil
import os

base_dir = 'images/ai/'
os.makedirs(f'{base_dir}')

for part_id in range(1, 6):
    part_url = f'https://huggingface.co/datasets/poloclub/diffusiondb/resolve/main/images/part-{part_id:06}.zip'
    urlretrieve(part_url, f'{base_dir}part-{part_id:06}.zip')
    shutil.unpack_archive(f'{base_dir}part-{part_id:06}.zip', f'{base_dir}part-{part_id:06}')
    os.remove(f'{base_dir}part-{part_id:06}.zip')