import matplotlib.pyplot as plt
import pandas as pd    

if __name__ == "__main__":
    # Replace 'data.csv' with the path to your CSV file
    file_name = 'aggBBS1'

    csv_file_name = f'csv/{file_name}.csv'
    
    # Specify which lines to plot, e.g., [1, 2, 3] for the first three lines
    lines = None  # None will plot all lines
    
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file_name)
    
    # If lines parameter is not provided, plot all lines
    if lines is None:
        lines = range(1, len(df.columns))
    
    # Plot each selected line
    for line in lines:
        if line >= len(df.columns):
            print(f"Line {line} does not exist in the CSV file.")
            continue
        plt.plot(df.iloc[:, 0], df.iloc[:, line], label=f'Line {line}')
        
    # Add labels and title
    plt.xlabel('Iterations')
    plt.ylabel('Values')
    plt.title(file_name + " plot")
    plt.legend()
    
    # Display the plot
    plt.show()