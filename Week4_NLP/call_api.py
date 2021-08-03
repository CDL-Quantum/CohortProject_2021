import os
from typing import List
import pickle as pkl
import requests
from discopy import *

URL = 'https://cqc.pythonanywhere.com/discocat/code?sentence={input_str}'


def get_objects(sentence: str):
    full_URL = URL.format(input_str=sentence.replace(' ', '%20'))
    response = requests.get(full_URL)
    if response.status_code == 200:
        full_ex = response.text
        return eval(full_ex)
    else:
        raise RuntimeError


def save_dataset(sentence_list: List[str], pkl_path="./dataset.pkl"):
    dataset = [(s, get_objects(s)) for s in sentence_list]
    with open(pkl_path, 'wb') as of:
        pkl.dump(dataset, of)


if __name__ == '__main__':
    get_objects("Alice loves Bob.").draw()

    tmp_path = './tmp.pkl'
    save_dataset(["Alice loves Bob.", "Hanna hates Cheol-hee.", "I don't know."], pkl_path=tmp_path)
    with open(tmp_path, 'rb') as of:
        lst = pkl.load(of)
    for s, ob in lst:
        print(s)
        ob.draw()
    os.remove(tmp_path)
