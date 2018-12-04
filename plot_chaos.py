import os
from argparse import ArgumentParser
from chaos import embedding_phase_space, plot_embedding_points

def arguments():
    parser = ArgumentParser()
    parser.add_argument("--input", type=str)
    parser.add_argument("--dim", type=int, default=2)
    parser.add_argument("--delay_time", type=int, default=1)
    parser.add_argument("--size", type=int, default=1024)
    parser.add_argument("--is_save", type=str, default=False)
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = arguments()
    pos, name = embedding_phase_space(args.input, args.size, args.delay_time, args.dim)
    plot_embedding_points(pos, name, is_save=args.is_save)

