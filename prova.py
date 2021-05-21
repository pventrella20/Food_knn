import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import MinMaxScaler


def parseCSV(path):
    '''
    Legge un file .csv e lo incapsula in un dataframe
    :param path: percorso file .csv
    :return: dataframe con i dati estratti
    '''
    column_names = [
        "Food Name",
        "Food Number",
        "Filter group",
        "Energy (kcal)",
        "Energy (kJ)",
        "Carbohydrates (g)",
        "Fat (g)",
        "Protein (g)",
        "Fibre (g)",
        "Water (g)",
        "Alcohol (g)",
        "Ash (g)",
        "Monosaccharides (g)",
        "Disaccharides (g)",
        "Sucrose (g)",
        "Wholegrain total (g)",
        "Sugar total (g)",
        "Sum of saturated fatty acids (g)",
        "Fatty acids 4:0-10:0 (g)",
        "Fatty acid 12:0 (g)",
        "Fatty acid 14:0 (g)",
        "Fatty acid 16:0 (g)",
        "Fatty acid 18:0 (g)",
        "Fatty acid 20:0 (g)",
        "Sum of monounsaturated fatty acids (g)",
        "Fatty acid 16:1 (g)",
        "Fatty acid 18:1 (g)",
        "Sum of polyunsaturated fatty acids (g)",
        "Fatty acids 18:2 (g)",
        "Fatty acid 18:3 (g)",
        "Fatty acid 20:4 (g)",
        "EPA (Fatty acid 20:5) (g)",
        "DPA (Fatty acid 22:5) (g)",
        "DHA (Fatty acid 22:6) (g)",
        "Cholesterol (mg)",
        "Retinol (µg)",
        "Retinolequivalents (RE)",
        "Beta-carotene (µg)",
        "Vitamin D (µg)",
        "Vitamin E (mg)",
        "Vitamin K (µg)",
        "Thiamin (mg)",
        "Riboflavin (mg)",
        "Vitamin C (mg)",
        "Niacin (mg)",
        "Niacin equivalents (NE)",
        "Vitamin B-6 (mg)",
        "Vitamin B-12 (µg)",
        "Folate (µg)",
        "Phosphorus (mg)",
        "Iodide (µg)",
        "Iron (mg)",
        "Calcium (mg)",
        "Potassium (mg)",
        "Magnesium (mg)",
        "Sodium (mg)",
        "Salt (g)",
        "Selenium (µg)",
        "Zinc (mg)",
        "Waste (e.g. peel) (%)"
    ]
    food = pd.read_csv(path, header=None, sep='\t', error_bad_lines=False, names=column_names)
    return food

def eliminateGrams(df):
    '''
    Elimina grammi, milligrammi e microgrammi dal dataset, convertendo milligrammi e microgrammi in grammi
    :param df: dataframe su cui effettuare la conversione
    :return: nuovo dataframe
    '''
    for name in df.columns:
        if name not in accepted:
            df = df.drop(name, axis=1)
    for col in convert:
        df[col] = df[col].astype(str)
        df[col] = df[col].map(lambda x: x.rstrip('IU'))
        df[col] = df[col].map(lambda x: x.rstrip('mcg'))
        df[col] = df[col].map(lambda x: x.rstrip('mg'))
        df[col] = df[col].map(lambda x: x.rstrip('g'))
    return df

def splittingAndEval(df):
    food_features = ["Carbohydrates (g)", "Protein (g)", "Fat (g)"]
    X_food = df[food_features]
    y_food = df['Energy (kcal)']
    print(df.head(10))
    # preprocessing
    X_train, X_test, y_train, y_test = train_test_split(X_food, y_food, random_state=0)

    scaler = MinMaxScaler()
    X_train_scaled = scaler.fit_transform(X_train)  # features normalization (train set)
    X_test_scaled = scaler.transform(X_test)        # features normalization (test set)
    knn = KNeighborsRegressor(n_neighbors=5)        # creo un knnRegressor
    knn.fit(X_train_scaled, y_train)                # fit del knn

    # Checking performance on the training set
    print('Accuracy of K-NN regressor on training set: {:.2f}'
          .format(knn.score(X_train_scaled, y_train)))
    # Checking performance on the test set
    print('Accuracy of K-NN regressor on test set: {:.2f}'
          .format(knn.score(X_test_scaled, y_test)))
    example_food = [[4.97, 1.92, 0.3]]  # inserire qui i valori di carboidrati, proteine e grassi per la predizione
    example_food_scaled = scaler.transform(example_food)
    # Making an prediction based on x values
    print('Predicted food calories for ', example_food, ' is ',
          knn.predict(example_food_scaled)[0] - 1)


#accepted = ["name", "calories", "carbohydrate", "protein", "total_fat"]
#convert = ["carbohydrate", "protein", "total_fat"]
f_r = parseCSV("LivsmedelsDB.csv")
#f_r = eliminateGrams(f_r)
splittingAndEval(f_r)
