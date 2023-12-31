from fastapi import FastAPI
from ultralytics import YOLO
import uvicorn
import requests
from PIL import Image
import io

# model = YOLO('captcha_model.pt')

github_raw_file_url = 'https://github.com/MehulKhanna/PokeGrinder/releases/download/v2.3/Solver1850.pt'
local_file_path = 'Solver1850.pt'

print("Getting the model from github...")
response = requests.get(github_raw_file_url)
with open(local_file_path, 'wb') as file:
  file.write(response.content)
print("Model loaded successfully!")

model = YOLO(local_file_path)
app = FastAPI()

@app.get("/")
async def read_root():
    return {"Status": 200}

@app.get("/solve/{url:path}")
async def read_item(url: str) -> dict[str, str]:
    try:
        # Fetch the image content from the URL
        response = requests.get(url)
        response.raise_for_status()

        # Open the image using PIL
        pil_image = Image.open(io.BytesIO(response.content))

        # Use the image content directly instead of downloading
        result = model.predict(
            pil_image,
            imgsz=320,
            save=False,
            agnostic_nms=True
        )[0]

        classes, boxes = list(map(int, result.boxes.cls)), list(result.boxes.xyxy)
        detections = [(name, float(boxes[index][0])) for index, name in enumerate(classes)]
        detections.sort(key=lambda v: v[1])

        answer = "".join([str(detection[0]) for detection in detections])
        return {"answer": answer}
    except Exception as e:
        print(f"Error: {e}")
        return {"answer": f"Error: {e}"}

if __name__ == "__main__":
    print("Starting the application...")
    uvicorn.run(app, port=8000, host="0.0.0.0")
