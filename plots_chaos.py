import os
from scandir import scandir
from argparse import ArgumentParser
from chaos import embedding_phase_space, plot_embedding_points
from matplotlib import pyplot as plt
import numpy as np

def arguments():
    parser = ArgumentParser()
    parser.add_argument("--input_dir", type=str)
    parser.add_argument("--dim", type=int, default=2)
    parser.add_argument("--delay_time", type=int, default=1)
    parser.add_argument("--size", type=int, default=1024)
    parser.add_argument("--is_save", type=bool, default=False)

    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = arguments()
    files = [args.input_dir + file.name for file in scandir(args.input_dir) if file.name.endswith(".wav")]
    poss = []
    names = []
    for file in files:
        pos, name = embedding_phase_space(file, args.size, args.delay_time, args.dim)
        poss.append(pos)
        names.append(name)
    poss = np.array(poss)
    plot_embedding_points(poss, args.delay_time, names, is_save=args.is_save)

