from fastapi import FastAPI
import uvicorn
import os
from dotenv import load_dotenv


load_dotenv(".env")

load_dotenv(f".env.{os.getenv('ENV')}", override=True)

app = FastAPI()


# Health Route
@app.get("/health")
def health_check():
    return {"status": "healthy"}


# Process Route
@app.get("/process")
def process():

    key = os.getenv("OPENAI_KEY")
    if key == "Key mathram mathiyo":
        pass
    else:
        raise ValueError("Invalid OPENAI_KEY")

    result="This is coming from the llm by passing the key and repsonse"

    return {"message": result}


if __name__ == "__main__":
    host = os.getenv("HOST")
    port = int(os.getenv("PORT"))

    print(f"HOST: {host}")
    print(f"PORT: {port}")

    uvicorn.run(
        app,
        host=host,
        port=port,
        reload=False
    )