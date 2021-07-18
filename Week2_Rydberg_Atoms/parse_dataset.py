import csv
from typing import TypedDict, List, Optional, Dict, Union, Tuple

path_to_worldcities = './simplemaps_worldcities_basicv1.73/worldcities.csv'


class CityData(TypedDict):
    city_name: str
    lat: float
    lng: float
    country: str
    population: int


class CityDataset(object):
    def __init__(self, path_to_csv: str = path_to_worldcities):
        self.data_by_country: Dict[str, List[CityData]] = {}
        with open(path_to_csv, 'r') as of:
            csv_reader = csv.reader(of, delimiter=',')
            num_loaded, num_skipped = 0, 0
            for i, r in enumerate(csv_reader):
                if i == 0:
                    continue
                try:
                    city_name, lat, lng, country, population = \
                        [x.replace('"', '') for x in [r[1], r[2], r[3], r[4], r[-2]]]
                    lat, lng, population = float(lat), float(lng), int(population)
                except ValueError:
                    num_skipped += 1
                    continue
                city: CityData = {
                    "city_name": city_name,
                    "lat": lat,
                    "lng": lng,
                    "country": country,
                    "population": population
                }
                if country in self.data_by_country:
                    self.data_by_country[country].append(city)
                else:
                    self.data_by_country.update({country: [city]})
                num_loaded += 1
        # print(f"{num_loaded} cities loaded, {num_skipped} are skipped among {num_loaded + num_skipped} cities.")
        self.num_cities_by_country = {
            city_name: len(self.data_by_country[city_name]) for city_name in self.data_by_country
        }

    def filter(self, country: str,
               population: Optional[int] = None,
               lat_minmax: Optional[Tuple[float, float]] = None,
               lng_minmax: Optional[Tuple[float, float]] = None,
               ret_coord: bool = False
               ) -> Union[List[CityData], Tuple[List[str], List[Tuple[float, float]]]]:
        filtered_cities = [c for c in self.data_by_country[country]
                           if (population is None or c["population"] >= population)
                           and (lat_minmax is None or lat_minmax[0] < c['lat'] < lat_minmax[1])
                           and (lng_minmax is None or lng_minmax[0] < c['lng'] < lng_minmax[1])]
        if not ret_coord:
            return filtered_cities
        names = [x['city_name'] for x in filtered_cities]
        coords = [(x['lng'], x['lat']) for x in filtered_cities]
        return names, coords


class ExampleGraph(TypedDict):
    name: str
    city_name: List[str]
    coordinate: List[Tuple[float, float]]
    radius: float
    normalized_coord: List[Tuple[float, float]]


if __name__ == "__main__":
    dataset = CityDataset()
    print(dataset.num_cities_by_country)
    print([(c, dataset.num_cities_by_country[c]) for c in sorted([_c for _c in dataset.num_cities_by_country],
                                                                 key=lambda x: dataset.num_cities_by_country[x],
                                                                 reverse=True)])
    from draw_graph import draw_graph
    '''
    korea_city_name, korea_city_coords = dataset.filter('Korea, South',
                                                        ret_coord=True,
                                                        population=100_000,
                                                        lat_minmax=(36.9, 37.82),
                                                        lng_minmax=(126.5, 127.24))
    draw_graph(korea_city_coords, radius=0.09, texts=['' if t != 'Seoul' else t for t in korea_city_name])
    print(f"Korea near Seoul : {len(korea_city_coords)} cities")  # 21
    '''
    us_city_name, us_city_coords = dataset.filter('United States',
                                                  ret_coord=True,
                                                  population=200_000,
                                                  lat_minmax=(40.4, 40.9),
                                                  lng_minmax=(-75, -73.6)
                                                  )
    draw_graph(us_city_coords, radius=0.075, texts=['' if t != 'New York' else t for t in us_city_name])
    print(f"US near New York : {len(us_city_coords)} cities")  # 10
    '''
    canada_city_name, canada_city_coords = dataset.filter('Canada',
                                                          ret_coord=True,
                                                          population=50_000,
                                                          lat_minmax=(43.2, 44),
                                                          lng_minmax=(-80, -78),
                                                          )
    draw_graph(canada_city_coords, radius=0.14, texts=['' if t != 'Toronto' else t for t in canada_city_name])
    print(f"Canada : {len(canada_city_coords)} cities")  # 17

    japan_city_name, japan_city_coords = dataset.filter('Japan',
                                                        ret_coord=True,
                                                        population=400_000,
                                                        lat_minmax=(35, 36),
                                                        lng_minmax=(139, 141)
                                                        )
    draw_graph(japan_city_coords, radius=0.12, texts=['' if t != 'Tokyo' else t for t in japan_city_name])
    print(f"Japan : {len(japan_city_coords)} cities")  # 13

    south_africa_city_name, south_africa_city_coords = dataset.filter('South Africa',
                                                                      ret_coord=True,
                                                                      population=None,
                                                                      lat_minmax=(-34, -33),
                                                                      lng_minmax=(18, 19)
                                                                      )
    draw_graph(south_africa_city_coords, radius=0.3,
               texts=['' if t != 'Cape Town' else t for t in south_africa_city_name])
    print(f"South Africa : {len(south_africa_city_coords)} cities")  # 6
    '''
