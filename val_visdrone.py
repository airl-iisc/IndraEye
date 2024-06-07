from ultralytics import YOLO

# Load a model
model = YOLO("/home/user/ultralytics/runs/detect/IR2IR_mainrun/weights/best.pt")

# Customize validation settings
validation_results = model.val(data="indraeye_ir.yaml", imgsz=640, batch=16, conf=0.25, iou=0.6, device="0")