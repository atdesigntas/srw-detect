from ultralytics import YOLO

# Load a model
model = YOLO("/root/srw/runs/detect/train4/weights/last.pt")  # load a partially trained model

# Resume training
results = model.train(resume=True)
