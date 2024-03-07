# Use Chainguard Python dev image as base for 1st stage of multi-stage build
FROM cgr.dev/chainguard/python:latest-dev as builder

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies in user's home directory instead of the system directory
RUN pip install -r requirements.txt --user

# Use Chainguard Python distroless image as base for 2nd stage of multi-stage build
FROM cgr.dev/chainguard/python:latest

# Set the working directory
WORKDIR /app

# Make sure you update Python version in path
COPY --from=builder /home/nonroot/.local/lib/python3.12/site-packages /home/nonroot/.local/lib/python3.12/site-packages

# Copy the code
COPY app.py .

# Set the entrypoint
ENTRYPOINT [ "python", "/app/app.py" ]
