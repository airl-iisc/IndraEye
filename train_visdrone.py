from ultralytics import YOLO

# Load a model
model = YOLO("/home/user/ultralytics/yolov8x.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="/home/user/ultralytics/ultralytics/cfg/datasets/commontest_Indra_hit.yaml", epochs=100, imgsz=640, device="0")
