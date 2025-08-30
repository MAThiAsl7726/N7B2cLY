# 代码生成时间: 2025-08-30 18:08:59
import gr
import numpy as np

# Test Data Generator using Graviti SDK and Gr

def generate_test_data(num_samples, num_features):
    """Generates a specified number of test data samples.

    Args:
        num_samples (int): The number of samples to generate.
        num_features (int): The number of features for each sample.

    Returns:
        numpy.ndarray: An array of generated test data samples.
    """
    try:
        # Generate random test data using NumPy
        test_data = np.random.rand(num_samples, num_features)
        return test_data
    except Exception as e:
        # Handle any exceptions that occur during data generation
        print(f"Error generating test data: {e}")
        return None


def main():
    # Set the number of samples and features
    num_samples = 100
    num_features = 5

    # Generate test data
    test_data = generate_test_data(num_samples, num_features)

    # Check if test data was generated successfully
    if test_data is not None:
        # Create a Gr dataset
        dataset = gr.Dataset()
        
        # Add a table to the dataset
        table = gr.Table(name="test_data")
        for i, sample in enumerate(test_data):
            # Add each sample as a row in the table
            table.add_row(sample.tolist())
        
        # Add the table to the dataset
        dataset.add_table(table)
        
        # Save the dataset to a Gr file
        dataset.save("test_data.gr""
    else:
        print("Failed to generate test data."

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()