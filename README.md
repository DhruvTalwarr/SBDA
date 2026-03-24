# Smart Business Decision Assistant (SBDA)

A Competitor & Market Intelligence Assistant.

## Overview
This application uses a multi-agent orchestration architecture driven by LangGraph, wrapped around a FastAPI backend, with a user-friendly Streamlit frontend. It generates SWOT analyses, Competitor Comparisons, Risk Analyses, and Strategic Recommendations.

## Prerequisites
- Python 3.10+
- OpenAI API Key

## Setup & Running Locally (Without Docker)

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set Environment Variables**
   Fill in your `OPENAI_API_KEY` in the `.env` file.

3. **Start the Backend**
   ```bash
   uvicorn backend.main:app --reload --port 8000
   ```

4. **Start the Frontend** (In a new terminal)
   ```bash
   streamlit run frontend/app.py --server.port 8501
   ```

## Setup & Running with Docker

1. **Set Environment Variables**
   Fill in your `OPENAI_API_KEY` in the `.env` file at the root.

2. **Run Docker Compose**
   ```bash
   docker-compose up --build
   ```

3. **Access the App**
   Open your browser and navigate to `http://localhost:8501`.
