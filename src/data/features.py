import pandas as pd

def create_features(input_path='data/processed/nba_games_preprocessed.csv', output_path='data/processed/nba_games_features.csv'):
    df = pd.read_csv(input_path)
    df['point_diff'] = df['HomeTeamScore'] - df['AwayTeamScore']
    # Example: Create moving average of last 5 games
    df['home_team_ma'] = df.groupby('HomeTeam')['HomeTeamScore'].rolling(window=5).mean().reset_index(0, drop=True)
    df.to_csv(output_path, index=False)
    return df

if __name__ == "__main__":
    create_features()
