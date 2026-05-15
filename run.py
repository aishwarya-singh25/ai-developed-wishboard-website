#!/usr/bin/env python3

import uvicorn
from backend.src.main import app

if __name__ == "__main__":
    uvicorn.run(
        "backend.src.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )