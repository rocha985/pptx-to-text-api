from fastapi import FastAPI, File, UploadFile
from pptx_processor import extract_text_from_pptx
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/upload_pptx/")
async def upload_pptx(file: UploadFile = File(...)):
    try:
        file_content = await file.read()
        
        slides_text = extract_text_from_pptx(file_content)
        
        return JSONResponse(content=slides_text)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
