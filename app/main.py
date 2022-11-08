from fastapi import FastAPI

app = FastAPI(root_path="/alfredo")

@app.get("/")
def root():
    return {"message": "Hello world"}

@app.post('/webhook')
def webhook():
  return {
        "fulfillmentText": 'This is from the replit webhook',
        "source": 'webhook'
    }