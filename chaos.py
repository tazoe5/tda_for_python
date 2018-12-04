#coding:utf-8
import wave
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import random
import os
import scandir
from argparse import ArgumentParser

def wave_load(filename):
    # open wave file
    wf = wave.open(filename,'r')
    channels = wf.getnchannels()

    # load wave data
    chunk_size = wf.getnframes()
    amp  = (2**8) ** wf.getsampwidth() / 2
    data = wf.readframes(chunk_size)   # バイナリ読み込み
    data = np.frombuffer(data,'int16') # intに変換
    data = data / amp                  # 振幅正規化
    data = data[::channels]

    return data

def embedding_phase_space(input_path,size, delay_time, dim=2):
    '''
    input_path = 入力信号のパス 
    size = FFTのサンプル数（２＊＊ｎ）
    '''
    _, name = os.path.split(input_path)
    name, _ = os.path.splitext(name)
    st = 10000   # サンプリングする開始位置
    hammingWindow = np.hamming(size)    # ハミング窓
    fs = 44100 #サンプリングレート
    d = 1.0 / fs #サンプリングレートの逆数
    freqList = np.fft.fftfreq(size, d)
   
    wave = wave_load(input_path)
    windowedData = hammingWindow * wave[st:st+size]  # 切り出した波形データ（窓関数あり）
    data = np.fft.fft(windowedData)
    data /= max(abs(data))

    chaos_vectors = []
    for time in np.arange(dim-1, len(data)):
        p = [data[time - delay_time*i] for i in np.arange(dim)]
        chaos_vectors.append(p)
    chaos_vectors = np.array(chaos_vectors).real
    print("file name: {}".format(name))
    print("delay time: {}".format(delay_time))
    print("embedding shape: {}".format(chaos_vectors.shape))
    
    return chaos_vectors, name

def plot_embedding_points(position, delay_time, name="", is_save=False):
    
    if position.ndim == 3:
        _, _ , dim = position.shape
        if dim == 2:
            plot_2ds(position, delay_time, name, is_save)
        elif dim == 3:
            plot_3ds(position, delay_time, name, is_save)
    elif position.ndim == 2:
        _, dim = position.shape
        if dim == 2:
            plot_2d(position, delay_time, name, is_save)
        
        elif dim == 3:
            plot_3d(position, delay_time, name, is_save)

    plt.clf()

def plot_2d(position, delay_time, name="", is_save=False):
    print("plot_2d")
    plt.xlabel("p(t)")
    plt.ylabel("p(t-{})".format(delay_time))
    plt.title("Delay Coordinate Embedding 2D")

    X, Y = position[:, 0], position[:, 1]
    plt.scatter(X, Y, label=name)


    plt.legend()
    if is_save:
        dir_path = "./result_dce/2D/"
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        name = dir_path + "dce{}_{}.png".format(delay_time, name)
        plt.savefig(name)
        plt.clf()
    else:
        plt.show()

def plot_3d(position, delay_time, name="", is_save=False):
    from mpl_toolkits.mplot3d import Axes3D
    X, Y, Z = position[:, 0], position[:, 1], position[:, 2]

    fig = plt.figure()
    ax = Axes3D(fig)

    ax.set_xlabel("p(t)")
    ax.set_ylabel("p(t-1)")
    ax.set_zlabel("p(t-2)")
    ax.plot(X, Y, Z, "o", label=name)
    plt.title("Delay Coordinate Embedding 3D")
    plt.legend()
    plt.show()

def plot_2ds(positions, delay_time, names="", is_save=False): #, fig=None):
    print("plot_2ds")
    plt.xlabel("p(t) {} delay time:{}".format(" "*30, delay_time))
    plt.ylabel("p(t-{})".format(delay_time))
    plt.title("Delay Coordinate Embedding 2D")

    for position, name in zip(positions, names):
        X, Y = position[:, 0], position[:, 1]
        plt.scatter(X, Y, label=name)

    plt.legend()
    if is_save:
        dir_path = "./result_dce/2D/"
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        name = dir_path + "dce{}.png".format(delay_time)
        plt.savefig(name)
        plt.clf()
    else:
        plt.show()

def plot_3ds(positions, delay_time, names="", is_save=False):
    from mpl_toolkits.mplot3d import Axes3D

    fig = plt.figure()
    ax = Axes3D(fig)
    plt.title("Delay Coordinate Embedding 3D")
    ax.set_xlabel("p(t)")
    ax.set_ylabel("p(t-1)")
    ax.set_zlabel("p(t-2)")
    for position, name in zip(positions, names):
        X, Y, Z = position[:, 0], position[:, 1], position[:, 2]
        ax.plot(X, Y, Z, "o", label=name)
    plt.legend()
    plt.show()
