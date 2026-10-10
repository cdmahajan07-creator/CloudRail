from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="CloudRail API",
    description="Backend API for Railway Management System",
    version="1.0.0"
)

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "CloudRail Backend API is operational", "status": "healthy"}

@app.get("/health")
def health_check():
    return {"status": "UP", "service": "CloudRail Core"}