from fastapi import FastAPI
import requestModel

app = FastAPI()

@app.post("/v1/displayMessage", tags=["Test"], summary="Function to display message")
async def displayMessage(request:requestModel.displayMessage):
    resultStatus =  "success"
    message = "Message successfully displayed"
    try:
        data = f"Hi {request.message}"
        return {"status":resultStatus, "message":message,"data":data}
    except Exception as e:
        resultStatus = "error"
        message = f"Error in function display message {e}"
        return {"status":resultStatus, "message":message,"data":data}