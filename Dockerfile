FROM public.ecr.aws/lambda/python:3.11

# Copy the project files into the Lambda task root
COPY . ${LAMBDA_TASK_ROOT}

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the handler
CMD ["lambda_handler.lambda_handler"]
