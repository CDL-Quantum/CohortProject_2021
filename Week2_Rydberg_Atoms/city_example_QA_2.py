import os
import pickle
from collections import Counter
from itertools import product
from time import time

from tqdm import tqdm

from Week2_Rydberg_Atoms.draw_graph import draw_graph
from Week2_Rydberg_Atoms.julia_run_quantum_annealing import get_edges, run_annealing, measure
from Week2_Rydberg_Atoms.parse_dataset import CityDataset
from Week2_Rydberg_Atoms.utils import normalize_coordinates

T_list = [0.01, 0.05, 0.1, 0.5, 1.0, 5.0, 10.0]
pkl_file = "./simulations/city_example_QA_2.txt"

dataset = CityDataset()
korea_city_name, korea_city_coords = dataset.filter('Korea, South',
                                                    ret_coord=True,
                                                    population=100_000,
                                                    lat_minmax=(36.9, 37.82),
                                                    lng_minmax=(126.5, 127.24))
draw_graph(korea_city_coords, radius=0.09, texts=['' if t != 'Seoul' else t for t in korea_city_name])

us_city_name, us_city_coords = dataset.filter('United States',
                                              ret_coord=True,
                                              population=200_000,
                                              lat_minmax=(40.4, 40.9),
                                              lng_minmax=(-75, -73.6)
                                              )
draw_graph(us_city_coords, radius=0.075, texts=['' if t != 'New York' else t for t in us_city_name])

canada_city_name, canada_city_coords = dataset.filter('Canada',
                                                      ret_coord=True,
                                                      population=50_000,
                                                      lat_minmax=(43.2, 44),
                                                      lng_minmax=(-80, -78),
                                                      )
draw_graph(canada_city_coords, radius=0.14, texts=['' if t != 'Toronto' else t for t in canada_city_name])

japan_city_name, japan_city_coords = dataset.filter('Japan',
                                                    ret_coord=True,
                                                    population=400_000,
                                                    lat_minmax=(35, 36),
                                                    lng_minmax=(139, 141)
                                                    )
draw_graph(japan_city_coords, radius=0.12, texts=['' if t != 'Tokyo' else t for t in japan_city_name])

south_africa_city_name, south_africa_city_coords = dataset.filter('South Africa',
                                                                  ret_coord=True,
                                                                  population=None,
                                                                  lat_minmax=(-34, -33),
                                                                  lng_minmax=(18, 19)
                                                                  )
draw_graph(south_africa_city_coords, radius=0.3,
           texts=['' if t != 'Cape Town' else t for t in south_africa_city_name])

germany_city_name, germany_city_coords = dataset.filter('Germany',
                                                        ret_coord=True,
                                                        population=None,
                                                        lat_minmax=(51.95, 52.9),
                                                        lng_minmax=(13, 14)
                                                        )
draw_graph(germany_city_coords, radius=0.12,
           texts=['' if t != 'Berlin' else t for t in germany_city_name])

pkl_data = dict()
coordinate_dict = {
    # 'Germany, Near Berlin > 1,000': normalize_coordinates(germany_city_coords, 0.12),  # 24
    # 'South Korea, Near Seoul > 100,000': normalize_coordinates(korea_city_coords, 0.09),  # 21
    'Canada, Near Toronto > 50,000': normalize_coordinates(canada_city_coords, 0.14),  # 17
    'Japan, Near Tokyo > 400,000': normalize_coordinates(japan_city_coords, 0.12),  # 13
    'United States, Near New York > 200,000': normalize_coordinates(us_city_coords, 0.075),  # 10
    'South Africa Near Cape Town > 1,000': normalize_coordinates(south_africa_city_coords, 0.3)  # 6
}

if __name__ == "__main__":
    # print(f"Korea near Seoul : {len(korea_city_coords)} cities")  # 21
    print(f"Canada : {len(canada_city_coords)} cities")  # 17
    print(f"Japan : {len(japan_city_coords)} cities")  # 13
    print(f"US near New York : {len(us_city_coords)} cities")  # 10
    print(f"South Africa : {len(south_africa_city_coords)} cities")  # 6
    # print(f"Germany : {len(germany_city_coords)} cities")  # 24

    for name in coordinate_dict:
        draw_graph(coordinate_dict[name], radius=0.5)

    for name, T in tqdm(list(product(coordinate_dict, T_list))):
        graph = coordinate_dict[name]
        edges = get_edges(graph)
        start = time()
        dt = T/1000
        psi = run_annealing(graph, edges, dt, T)
        end = time()
        samples = [s for s in measure(psi, nshots=10000)]
        occurrence = Counter(samples)
        if name in pkl_data:
            pkl_data[name].update({
                T: {
                    "occurrence": occurrence,
                    "time_elapsed": end - start
                }
            })
        else:
            pkl_data.update({
                name: {
                    T: {
                        "occurrence": occurrence,
                        "time_elapsed": end - start
                    }
                }
            })

        if os.path.isfile(pkl_file):
            with open(pkl_file, 'rb') as of:
                prev_data = pickle.load(of)
        for p_k in prev_data:
            if p_k in pkl_data:
                for p_dt in prev_data[p_k]:
                    if p_dt not in pkl_data[p_k]:
                        pkl_data[p_k].update({
                            p_dt: prev_data[p_k][p_dt]
                        })
            else:
                pkl_data.update({
                    p_k: prev_data[p_k]
                })
        with open(pkl_file, 'wb') as of:
            pickle.dump(pkl_data, of)
