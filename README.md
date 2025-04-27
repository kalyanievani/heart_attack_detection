# Heart Attack Detection Project

This project is a web application that predicts the survival of patients with heart failure based on their clinical records. It utilizes a trained XGBoost model and provides a user-friendly interface using Gradio.

## Project Structure

```
heart_attack_detection
├── app
│   ├── app.py                # Main application code
│   └── trained_model
│       └── xgboost-model.pkl # Trained XGBoost model
├── Dockerfile                 # Dockerfile for building the application image
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd heart_attack_detection
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the application, execute the following command:
```
python app/app.py
```

Alternatively, you can build and run the application using Docker:

1. Build the Docker image:
   ```
   docker build -t heart_attack_detection .
   ```

2. Run the Docker container:
   ```
   docker run -p 7860:7860 heart_attack_detection
   ```

After running the application, you can access it in your web browser at `http://localhost:7860`.

## Usage

Once the application is running, you can input the patient's clinical data through the Gradio interface. The model will predict the likelihood of a death event based on the provided information.

## License

This project is licensed under the MIT License.