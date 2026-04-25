import argparse
import pandas as pd
import matplotlib.pyplot as plt
import os

def main(data_path, report_dir):
    # Read the dataset
    df = pd.read_csv(data_path)

    # Validate required columns
    required_columns = ['gender', 'sleep_duration_hours']
    for column in required_columns:
        if column not in df.columns:
            print(f"Error: Missing required column '{column}' in the dataset.")
            exit(1)

    # Handle missing values
    df = df.dropna(subset=required_columns)

    # Create the boxplot
    plt.figure(figsize=(10, 6))
    df.boxplot(column='sleep_duration_hours', by='gender')
    plt.title('Sleep Duration by Gender')
    plt.suptitle('')
    plt.xlabel('Gender')
    plt.ylabel('Sleep Duration (hours)')
    
    # Save the figure
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)
    plt.savefig(os.path.join(report_dir, 'sleep_duration_by_gender.png'))
    plt.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Analyze sleep duration by gender.')
    parser.add_argument('--data', required=True, help='Path to the input CSV data file.')
    parser.add_argument('--report_dir', required=True, help='Directory to save the report artifacts.')
    args = parser.parse_args()
    
    main(args.data, args.report_dir)