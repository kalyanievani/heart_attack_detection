FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code, including the trained_model directory
COPY app /app/app

# Expose the port for Gradio
EXPOSE 7860

# Command to run the application
CMD ["python", "app/app.py"]