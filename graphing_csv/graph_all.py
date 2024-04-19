import os
import matplotlib.pyplot as plt
import pandas as pd

def plot_csv_files(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Get all CSV files in the input folder
    csv_files = [f for f in os.listdir(input_folder) if f.endswith('.csv')]
    
    # Loop through each CSV file
    for csv_file in csv_files:
        try:
            print("Processing file", csv_file)
            # Read the CSV file into a pandas DataFrame
            df = pd.read_csv(os.path.join(input_folder, csv_file))
            
            # Plot each column as a separate line
            for i, col in enumerate(df.columns):
                if col != df.columns[0]:  # Skip the first column (index)
                    plt.plot(df.iloc[:, 0], df[col], label=f'Variable {i}')
            
            # Add labels and title
            plt.xlabel('Iterations')
            plt.ylabel('Values')
            plt.title(os.path.splitext(csv_file)[0])
            plt.legend()
            
            # Save the plot in the output folder with the same name as the CSV file
            plot_filename = os.path.splitext(csv_file)[0] + '.png'
            plt.savefig(os.path.join(output_folder, plot_filename))
            
            # Clear the current plot to start fresh for the next CSV file
            plt.clf()
            
            print(f"Plot saved for {csv_file}")
        except Exception as e:
            print(f"Error processing {csv_file}: {e}")

if __name__ == "__main__":
    # Replace 'input_folder' and 'output_folder' with your desired folder paths
    input_folder = 'csv'
    output_folder = 'graphs'
    
    plot_csv_files(input_folder, output_folder)