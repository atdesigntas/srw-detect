from ultralytics import YOLO

model = YOLO("yolo-top-down.pt")

model.train(data="srwdetect.yaml", imgsz=640, batch=8, epochs=100, workers=0, device=0)
