from ultralytics import YOLO

model = YOLO("yolov8n.pt")
results = model("photo.jpg")

results[0].show()

for box in results[0].boxes:
    objet = results[0].names[int(box.cls)]
    confiance = float(box.conf)
    print(f"{objet} ({confiance:.2%})")
