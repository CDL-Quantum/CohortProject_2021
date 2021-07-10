import imageio as imageio

import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib_inline.backend_inline import FigureCanvas
from tqdm import tqdm
import io

from Week1_Trapped_Ions.src.julia_run_random_circuit import run_random_circuit
from Week1_Trapped_Ions.src.pastaq_gates_to_qasm import pastaq_gates_to_qiskit
from Week1_Trapped_Ions.src.utils import get_histogram_from_outcomes_small, draw_circles


def fig2img(fig) -> Image:
    """Convert a Matplotlib figure to a PIL Image and return it"""
    buf = io.BytesIO()
    fig.savefig(buf)
    buf.seek(0)
    img = Image.open(buf)
    return img


if __name__ == "__main__":
    N = 4
    D = 10
    shots = 10000
    tmp_dir = './temp/'
    output_gif = './animation_taskA1/taskA1_pretty.gif'

    if not os.path.isdir(tmp_dir):
        os.mkdir(tmp_dir)

    orig_result, r_params, m_params = \
        run_random_circuit(N, D, shots,
                           rand_x=False,
                           ret_params=True)
    orig_hist = get_histogram_from_outcomes_small(orig_result)

    num_trials = 10
    fig, ax = None, None

    print("Generating images...")
    for i in tqdm(range(num_trials)):
        noisy_result, gates = \
            run_random_circuit(N, D, shots,
                               rand_x=True,
                               ret_gates=True,
                               in_r_param=r_params,
                               in_m_param=m_params)
        noisy_hist = get_histogram_from_outcomes_small(noisy_result)
        fig_circle, ax_circle = draw_circles(noisy_hist)
        img_circle = fig2img(fig_circle)

        qc = pastaq_gates_to_qiskit(gates, N)
        fig_qc = qc.draw(output='mpl')
        img_qc = fig2img(fig_qc)

        if img_circle.width > img_qc.width:
            total_width = img_circle.width
            total_height = img_circle.height + img_qc.height

            new_img = Image.new('RGB', (total_width, total_height), (255, 255, 255))
            new_img.paste(img_qc, (abs(img_circle.width - img_qc.width)//2, 0))
            new_img.paste(img_circle, (0, img_qc.height))
        else:
            total_width = img_qc.width
            total_height = img_circle.height + img_qc.height

            new_img = Image.new('RGB', (total_width, total_height), (255, 255, 255))
            new_img.paste(img_qc, (0, 0))
            new_img.paste(img_circle, (abs(img_circle.width - img_qc.width)//2, img_qc.height))
        new_img.save(os.path.join(tmp_dir, f"{i}.png"))

    with imageio.get_writer(output_gif, mode='I', duration=1) as writer:
        for filename in os.listdir(tmp_dir):
            im_path = os.path.join(tmp_dir, filename)
            image = imageio.imread(im_path)
            writer.append_data(image)
            os.remove(im_path)
    os.rmdir(tmp_dir)
    print("Done!")
