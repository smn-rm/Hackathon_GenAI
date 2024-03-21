#!/bin/sh

# Start the frontend
npm run start &

# Start the backend
flask run --host 0.0.0.0