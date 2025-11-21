# rms-previsoes (entrega automática)

Repositório gerado automaticamente contendo um backend simples (Flask) e um frontend minimal
para processar ficheiros Excel com previsões por tipologia.

## Estrutura
- `backend/` - Flask app, processor, Dockerfile and requirements
- `frontend/` - index.html com uploader simples
- `docker-compose.yml` - arranque local with volumes for uploads/output
- `.github/workflows` - workflow example for build/push

## Example files available in this environment (paths):
- /mnt/data/Previsõespool.xlsx
- /mnt/data/PrevisõesATTIC.xls
- /mnt/data/PrevisõesJardim.xls
- /mnt/data/PrevisõesJSUITE.xls
- /mnt/data/PrevisõesTWSUP.xls
- /mnt/data/Previsõesvistamar.xls

## How to test locally (without Docker)
1. Create venv and activate
2. cd backend && pip install -r requirements.txt
3. copy example files to backend/uploads/
4. python backend/app.py
5. open http://localhost:8000
