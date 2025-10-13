# 代码生成时间: 2025-10-13 21:43:16
import gradio as gr
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import os

# Define a function to load the dataset
def load_dataset(file_path):
    """Loads the dataset from a CSV file."""
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print("The file was not found.")
        raise
    except Exception as e:
        print(f"An error occurred: {e}")
        raise

# Define a function to preprocess the data
def preprocess_data(df):
    """Preprocesses the dataset by imputing missing values and encoding categorical features."""
    # Define the categorical features
    categorical_features = df.select_dtypes(include=["object", "category"]).columns
    
    # Define the numerical features
    numerical_features = df.select_dtypes(include=["int64", "float64"]).columns
    
    # Create the preprocessing pipeline
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", SimpleImputer(strategy="mean"), numerical_features),
            ("cat", Pipeline(steps=[
                ("imputer", SimpleImputer(strategy="most_frequent")),
                ("encoder", LabelEncoder())
            ]), categorical_features)
        ], remainder="passthrough")
    
    # Fit and transform the data
    return preprocessor.fit_transform(df)

# Define a function to train the model
def train_model(X_train, y_train):
    """Trains a Random Forest Classifier model."""
    # Define the model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    
    # Train the model
    model.fit(X_train, y_train)
    return model

# Define a function to evaluate the model
def evaluate_model(model, X_test, y_test):
    """Evaluates the model's performance."""
    # Make predictions
    predictions = model.predict(X_test)
    
    # Calculate accuracy
    accuracy = accuracy_score(y_test, predictions)
    return accuracy

# Define a function to save the model
def save_model(model, file_path):
    """Saves the trained model to a file."""
    try:
        joblib.dump(model, file_path)
    except Exception as e:
        print(f"An error occurred: {e}")
        raise

# Define a function to load the model
def load_model(file_path):
    """Loads a trained model from a file."""
    try:
        return joblib.load(file_path)
    except Exception as e:
        print(f"An error occurred: {e}")
        raise

# Create a Gradio interface
def etl_pipeline_interface():
    with gr.Blocks() as demo: # Gradio demo interface
        # Input file selector
        file_selector = gr.File(label="Select a CSV file")
        # Output file selector
        output_file_selector = gr.File(label="Select an output file")
        # Run button
        run_button = gr.Button("Run ETL Pipeline")
        # Output label
        output_label = gr.Textbox(label="Output")
        
        # Define the function to be executed when the run button is clicked
        def run_etl_pipeline(file_selector, output_file_selector, run_button):
            """Runs the ETL pipeline and saves the trained model."""
            # Load the dataset
            df = load_dataset(file_selector)
            
            # Split the data into features and target variable
            X = df.drop("target", axis=1)
            y = df["target"]
            
            # Split the data into training and testing sets
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            
            # Preprocess the data
            X_train_preprocessed = preprocess_data(X_train)
            X_test_preprocessed = preprocess_data(X_test)
            
            # Train the model
            model = train_model(X_train_preprocessed, y_train)
            
            # Evaluate the model
            accuracy = evaluate_model(model, X_test_preprocessed, y_test)
            
            # Save the model
            save_model(model, output_file_selector)
            
            # Return the output
            return f"Model trained and saved with accuracy: {accuracy:.4f}"
        
        run_button.click(run_etl_pipeline, inputs=[file_selector, output_file_selector, run_button], outputs=output_label)

    demo.launch()

# Run the Gradio interface
if __name__ == "__main__":
    etl_pipeline_interface()