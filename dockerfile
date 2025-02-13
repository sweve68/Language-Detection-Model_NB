# Use an official Python image as the base image
FROM python:3.9-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements.txt file into the container at /app
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI and Streamlit app code into the container
COPY . /app/

# Expose FastAPI port and the Streamlit port
EXPOSE 8000 8501

# Start FastAPI and Streamlit in parallel using a shell script
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port 8000 & streamlit run streamlit_app.py --server.port 8501"]
