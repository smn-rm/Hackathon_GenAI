# BACKEND
FROM python:3.11.7
WORKDIR /usr/src/app

# Copy .env file
COPY .env ./

# Install backend dependencies
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
# Bundle backend source
COPY . ./

# expose port
EXPOSE 5000

CMD ["flask", "run", "--host", "0.0.0.0"]