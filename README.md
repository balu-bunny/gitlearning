# Salesforce-Like Platform (AWS)

This repo is an MVP **platform** (not a CRM app) that lets tenants define:
- Custom objects and fields
- Layouts and UI pages
- Permissions
- Automation rules

It includes:
- Python FastAPI backend
- React frontend
- CloudFormation infrastructure

## Quick Start (Local)

Backend:
```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Frontend:
```bash
cd frontend
npm install
npm run dev
```

## Deployment (AWS)

Use CloudFormation template in `infra/template.yaml`.

## Notes
This is a minimal MVP meant for iteration. See `docs/ARCHITECTURE.md` for the platform model.
