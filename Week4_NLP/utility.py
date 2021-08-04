import os
from typing import List
import pickle as pkl
import requests
from discopy import *
from sklearn.model_selection import train_test_split
from tqdm import tqdm
import numpy as np


def pretty(diag):
    return "Diagram(\n" \
           + "    dom={},\n".format(repr(diag.dom)) \
           + "    cod={},\n".format(repr(diag.cod)) \
           + "    boxes=[{}],\n".format(',\n           '.join(map(repr, diag.boxes))) \
           + "    offsets={})".format(diag.offsets)


URL = 'https://cqc.pythonanywhere.com/discocat/code?sentence={input_str}'


def get_objects(sentence: str):
    full_URL = URL.format(input_str=sentence.replace(' ', '%20'))
    response = requests.get(full_URL)
    if response.status_code == 200:
        full_ex = response.text
        return eval(full_ex)
    else:
        raise RuntimeError


def txt_file_to_diagram(input_file: str, storage='./dataset.pkl'):
    with open(input_file, 'r') as of:
        data = of.readlines()
    labels = list()
    sentences = list()
    for d in data:
        d = d.replace('\n', '')
        s = d.split('->')[0]
        str_ans = d.split('->')[-1].replace(' ', '')
        if str_ans == 'True':
            l = [1, 0]
        elif str_ans == 'False':
            l = [0, 1]
        else:
            raise ValueError(d, s, str_ans)
        labels.append(l)
        sentences.append(s)

    sentences = [s.replace('.', '') for s in sentences]

    if storage is not None and os.path.isfile(storage):
        with open(storage, 'rb') as of:
            prev_data = pkl.load(of)
    else:
        prev_data = dict()
    for s in tqdm(sentences):
        if s in prev_data:
            print("continued")
            continue
        prev_data[s] = get_objects(s)
    if storage is not None:
        with open(storage, 'wb') as of:
            pkl.dump(prev_data, of)

    return [prev_data[s] for s in sentences], labels


def divide_three_dataset(data, label, train_size, validate_size):
    X_train, X_test, y_train, y_test = train_test_split(data, label, test_size=1-train_size, random_state=1)
    X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=validate_size, random_state=1)
    return X_train, X_val, X_test, y_train, y_val, y_test


if __name__ == '__main__':
    _ob = get_objects("if Alice loves Bob, Bob loves Alice.")
    print(pretty(_ob))
    _ob.draw()
    _d, _l = txt_file_to_diagram('./sentence.txt')
    for _x, _y in zip(_d, _l):
        print(pretty(_x))
        print(_y)
