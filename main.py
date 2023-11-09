from fastapi import FastAPI
import uvicorn

import routers

host = "127.0.0.1"
port = 8000
url = f"http://{host}:{str(port)}/"

if __name__ == "__main__":
    app = FastAPI()
    app.include_router(routers.router)
    uvicorn.run(app, host=host, port=port)
