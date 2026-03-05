FROM python:3.11-slim

EXPOSE 8080

WORKDIR /app

COPY . ./

RUN pip install -r requirements.txt

ENTRYPOINT ["streamlit", "run", "portfolio_website.py", \
            "--server.port=8080", \
            "--server.address=0.0.0.0", \
            "--server.enableCORS=false", \
            "--browser.gatherUsageStats=false"]
```

**`requirements.txt`** (if you don't already have one)
```
streamlit
