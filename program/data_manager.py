import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# matplotlib.use('Agg')


def readCSV(path, separ):
    """
    legge un file .csv e lo incapsula in un dataframe pandas
    :param path: percorso file .csv da leggere
    :param separ: separatore (carattere)
    :return: dataframe contenente i dati estratti
    """
    data = pd.read_csv(path, sep=separ, error_bad_lines=False)
    return data


def data_analisys(df, feature):
    """
    permette un'analisi dei dati nel dataframe a video (istogramma + grafico verticale)
    :param df: dataframe
    :param features: nome della feature da analizzare (grafico)
    :return:
    """
    f, axes = plt.subplots(1, 2, figsize=(20, 4))
    sns.histplot(data=df[feature], ax=axes[0])
    sns.boxplot(data=df[feature], ax=axes[1])
    plt.show()


def column_analisys(df, col):
    """
    stampa a video il numero di valari nella feature
    :param df: dataframe
    :param col: nome feature
    :return:
    """
    print(df[col].value_counts())


def correlation_matrix(df):
    """
    stampa la matrice di correlazione di un dataframe
    :param df:
    :return:
    """
    plt.figure(figsize=(15, 6))
    sns.heatmap(df.corr(), annot=True)
    plt.show()


def pair_plot(df):
    """
    stampa il pair plot di un dataframe
    :param df: dataframe in input
    :return:
    """
    sns.pairplot(df)
    plt.show()


def box_plot(df):
    """
    stamoa il box plot di un dataframe
    :param df: dataframe in input
    :return:
    """
    plt.figure(figsize=(15, 4))
    sns.boxplot(data=df, orient="h")
    plt.show()
