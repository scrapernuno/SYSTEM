rms-previsoes - Ready to deploy bundle (final)

Instructions:
1. Extract and push this repo to GitHub (branch main).
2. On DigitalOcean App Platform, Add Component from Code:
   - Select your GitHub repo and branch=main
   - In 'Source directories' enter: backend
   - Next -> select Dockerfile (not buildpack)
   - Dockerfile path should be backend/Dockerfile
3. (Optional) Create persistent volumes for /app/uploads and /app/output
4. Deploy. App listens on port defined by PORT (default 8000).

Local test with Docker:
docker build -t rms-backend ./backend
docker run --rm -p 8000:8000 -v $(pwd)/backend/uploads:/app/uploads -v $(pwd)/backend/output:/app/output rms-backend
