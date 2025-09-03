#!/bin/bash

# Run database migrations if any (optional)
# python manage.py migrate

# Start the Uvicorn server.
# The --host 0.0.0.0 binds to all network interfaces, allowing external connections.
# The --port $PORT variable is set by Render.
# The `app.main:app` part should match your main FastAPI instance.
uvicorn app.main:app --host 0.0.0.0 --port $PORT