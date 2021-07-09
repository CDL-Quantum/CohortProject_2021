import imageio as imageio

import os

from tqdm import tqdm

from Week1_Trapped_Ions.julia_run_random_circuit import run_random_circuit
from Week1_Trapped_Ions.utils import get_histogram_from_outcomes_small, draw_circles

if __name__ == "__main__":
    N = 4
    D = 512
    shots = 10000
    tmp_dir = './temp/'
    output_gif = './taskA1_new.gif'

    if not os.path.isdir(tmp_dir):
        os.mkdir(tmp_dir)

    orig_result, r_params, m_params =\
        run_random_circuit(N, D, shots,
                           rand_x=False,
                           ret_params=True)
    orig_hist = get_histogram_from_outcomes_small(orig_result)

    num_trials = 10
    fig, ax = None, None

    print("Generating images...")
    for i in tqdm(range(num_trials)):
        noisy_result, pos_x, qubit_x =\
            run_random_circuit(N, D, shots,
                               rand_x=True,
                               ret_x_pos=True,
                               in_r_param=r_params,
                               in_m_param=m_params)
        noisy_hist = get_histogram_from_outcomes_small(noisy_result)
        fig, ax = draw_circles(noisy_hist, fig, ax)
        fig.suptitle(f"random x gate at the depth/qubit of {pos_x}/{qubit_x}")
        fig.savefig(os.path.join(tmp_dir, f"{i}.png"))
        fig, ax = None, None

    with imageio.get_writer(output_gif, mode='I', duration=1) as writer:
        for filename in os.listdir(tmp_dir):
            im_path = os.path.join(tmp_dir, filename)
            image = imageio.imread(im_path)
            writer.append_data(image)
            os.remove(im_path)
    os.rmdir(tmp_dir)
    print("Done!")
