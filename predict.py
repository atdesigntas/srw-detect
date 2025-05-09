from ultralytics import YOLO

model = YOLO("/root/srw/runs/train/weights/best.pt")

model.predict(source="161087.jpg", show=True, save=True, conf=0.6, save_txt=True)
