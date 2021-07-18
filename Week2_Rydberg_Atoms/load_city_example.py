import pickle

if __name__ == "__main__":
    p = "./simulations/city_example_QA.txt"
    with open(p, 'rb') as of:
        data = pickle.load(of)
    for name in data:
        for dt in data[name]:
            print(name, dt, data[name][dt]['time_elapsed'])
