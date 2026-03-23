# Lisa Interviewer — Python Backend

A lightweight Flask service that extracts text from uploaded PDF resumes and generates CSV reports from interview data.

## Tech Stack

- **Framework:** Flask
- **PDF Parsing:** pypdf
- **CORS:** flask-cors
- **Deployment:** Vercel (Python Serverless Functions)

## API Endpoints

| Method | Route | Description |
|--------|-------|-------------|
| `GET`  | `/` | Health check |
| `POST` | `/extract-text` | Upload a PDF and extract text content |
| `POST` | `/generate_csv` | Generate a CSV file from Q&A data |

## Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
echo 'FLASK_RUN_HOST="0.0.0.0"' > .env
echo 'PORT="5000"' >> .env

# Run locally
python server.py
```

## Environment Variables

| Variable | Description |
|----------|-------------|
| `FLASK_RUN_HOST` | Server host (default: `0.0.0.0`) |
| `PORT` | Server port (default: `5000`) |

## Deployment (Vercel)

1. Push to GitHub
2. Import repo in [Vercel](https://vercel.com)
3. Deploy — Vercel auto-detects the `@vercel/python` builder from `vercel.json`
