import pandas as pd

def preprocess_data(input_path='data/raw/nba_games_2023.csv', output_path='data/processed/nba_games_preprocessed.csv'):
    df = pd.read_csv(input_path)
    df = df.dropna()  # Example preprocessing step
    df['home_win'] = (df['HomeTeamScore'] > df['AwayTeamScore']).astype(int)
    df.to_csv(output_path, index=False)
    return df

if __name__ == "__main__":
    preprocess_data()
