import pickle

from Week2_Rydberg_Atoms.simulations.parse_dataset import CityDataset

if __name__ == "__main__":
    city_pkl_path = 'city_example_dataset.txt'
    dataset = CityDataset()
    korea_city_name, korea_city_coords = dataset.filter('Korea, South',
                                                        ret_coord=True,
                                                        population=100_000,
                                                        lat_minmax=(36.9, 37.82),
                                                        lng_minmax=(126.5, 127.24))
    # draw_graph(korea_city_coords, radius=0.09, texts=['' if t != 'Seoul' else t for t in korea_city_name])

    us_city_name, us_city_coords = dataset.filter('United States',
                                                  ret_coord=True,
                                                  population=200_000,
                                                  lat_minmax=(40.4, 40.9),
                                                  lng_minmax=(-75, -73.6)
                                                  )
    # draw_graph(us_city_coords, radius=0.075, texts=['' if t != 'New York' else t for t in us_city_name])

    canada_city_name, canada_city_coords = dataset.filter('Canada',
                                                          ret_coord=True,
                                                          population=50_000,
                                                          lat_minmax=(43.2, 44),
                                                          lng_minmax=(-80, -78),
                                                          )
    # draw_graph(canada_city_coords, radius=0.14, texts=['' if t != 'Toronto' else t for t in canada_city_name])

    japan_city_name, japan_city_coords = dataset.filter('Japan',
                                                        ret_coord=True,
                                                        population=400_000,
                                                        lat_minmax=(35, 36),
                                                        lng_minmax=(139, 141)
                                                        )
    # draw_graph(japan_city_coords, radius=0.12, texts=['' if t != 'Tokyo' else t for t in japan_city_name])

    south_africa_city_name, south_africa_city_coords = dataset.filter('South Africa',
                                                                      ret_coord=True,
                                                                      population=None,
                                                                      lat_minmax=(-34, -33),
                                                                      lng_minmax=(18, 19)
                                                                      )
    # draw_graph(south_africa_city_coords, radius=0.3,
    #            texts=['' if t != 'Cape Town' else t for t in south_africa_city_name])

    germany_city_name, germany_city_coords = dataset.filter('Germany',
                                                            ret_coord=True,
                                                            population=None,
                                                            lat_minmax=(51.95, 52.9),
                                                            lng_minmax=(13, 14)
                                                            )
    # draw_graph(germany_city_coords, radius=0.12,
    #           texts=['' if t != 'Berlin' else t for t in germany_city_name])

    coordinate_dict = {
        'Germany, Near Berlin > 1,000': {'graph': germany_city_coords, 'radius': 0.12, 'names': germany_city_name},  # 24
        'South Korea, Near Seoul > 100,000': {'graph': korea_city_coords, 'radius': 0.09, 'names': korea_city_name},  # 21
        'Canada, Near Toronto > 50,000': {'graph': canada_city_coords, 'radius': 0.14, 'names': canada_city_name},  # 17
        'Japan, Near Tokyo > 400,000': {'graph': japan_city_coords, 'radius': 0.12, 'names': japan_city_name},  # 13
        'United States, Near New York > 200,000': {'graph': us_city_coords, 'radius': 0.075, 'names': us_city_name},  # 10
        'South Africa Near Cape Town > 1,000': {'graph': south_africa_city_coords, 'radius': 0.3, 'names':south_africa_city_name}  # 6
    }

    with open(city_pkl_path, 'wb') as of:
        pickle.dump(coordinate_dict, of)
