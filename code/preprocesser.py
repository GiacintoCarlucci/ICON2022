import pandas as pd

DATASET_PATH = '../dataset/movies.csv'
DATASET_COLUMNS = ['filmtv_id','title','year','genre','duration','country', 'directors', 'avg_vote', 'total_votes']
MULTI_COLUMNS = ['country','directors']


def clean_dataset(dataset):
    for column in MULTI_COLUMNS:
        for row_index in range(len(dataset[column])):
            value = str(dataset[column][row_index]) 
            value = value.split(',')[0]
            value = value.strip()
            dataset[column][row_index] = value
    return dataset


dataset = pd.read_csv(DATASET_PATH, usecols = DATASET_COLUMNS)
dataset = clean_dataset(dataset)
dataframe = pd.DataFrame(dataset)
dataframe.to_csv('../dataset/preprocessed_movies.csv', index=False)
