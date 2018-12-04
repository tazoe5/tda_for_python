# import module
import pyper
import matplotlib.pyplot as plt
import numpy as np

from chaos import embedding_phase_space

def tda(data, is_df=False):
    r = pyper.R()
    r("library(TDA)")
    r.assign("data", data)
    print(r("Diag_Cir <- ripsDiag(X = data, maxdimension =1, maxscale = 5)"))
    print(r("summary(Diag_Cir)"))
    r("dimension_Cir <- Diag_Cir$diagram[, 1]")
    r("birth_Cir <- Diag_Cir$diagram[, 2]")
    r("death_Cir <- Diag_Cir$diagram[, 3]")
    r("Diag_Cir_DF <- data.frame(cbind(Dimension = dimension_Cir, Birth = birth_Cir, Death = death_Cir))")
    print(r("summary(Diag_Cir_DF)"))
    res = r.get("Diag_Cir_DF")
    if not is_df:
        res = np.array(res)
    return res

def plot_persistent_homology(ph, name, size, is_save=False):
    dimension, birth, death = ph[:, 0], ph[:, 1], ph[:, 2]
    plt.title("{}: PH size:{}".format(name, size))
    plt.xlim(-0.5, 5.5)
    plt.ylim(-0.5, 5.5)
    plt.plot([-0.5, 5.5], [-0.5, 5.5], color='black')

    dim_0 = np.where(dimension == 0)
    dim_1 = np.where(dimension == 1)
    birth_0, birth_1 = birth[dim_0], birth[dim_1]
    death_0, death_1 = death[dim_0], death[dim_1]
    plt.scatter(birth_0, death_0, label="0")
    plt.scatter(birth_1, death_1, label="1")
    plt.legend()
    if is_save:
        plt.savefig("name_{}.png".format(size))
        plt.clf()
    else:
        plt.show()

if __name__ == "__main__":
    # define variables
    FILE = "../samplevoice/arigato_yama-rei16k.wav"
    # SIZE = 256
    OUT = "./vis_tda/"
    DIM = 2


    for i in np.arange(50, 1000, 50):
        embedding, name = embedding_phase_space(FILE, i, DIM)
        ph = tda(embedding)
        print(ph.shape)
        plot_persistent_homology(ph, name, size=i, is_save=True)
