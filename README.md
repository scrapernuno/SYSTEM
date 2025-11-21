# rms-previsoes - Ready to deploy bundle

## How to use
1. Extract the ZIP and push to your GitHub repo (or use the files locally).
2. Ensure the repo structure contains `backend/Dockerfile`.
3. On DigitalOcean App Platform, when adding a component from code:
   - Choose GitHub provider, repository `scrapernuno/SYSTEM` (or your repo)
   - Branch: main
   - In 'Source directories' enter: backend
   - Next → select **Dockerfile** (not buildpack)
   - Dockerfile path: backend/Dockerfile
4. Optionally create persistent Volumes mounted to:
   - /app/uploads
   - /app/output
5. Build/Deploy. App listens on port 8000.

## Test locally with Docker
```
docker build -t rms-previsoes-backend ./backend
docker run --rm -p 8000:8000 -v $(pwd)/backend/uploads:/app/uploads -v $(pwd)/backend/output:/app/output rms-previsoes-backend
```

## Included example file (for testing)
The file you sent is included at backend/uploads/Previsõespool.xlsx
