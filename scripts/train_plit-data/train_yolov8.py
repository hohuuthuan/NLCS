from ultralytics import YOLO

def train_model():
    # Build a new model from YAML and load weights
    model = YOLO('E:/NIÊN LUẬN CƠ SỞ/code backup/NIEN_LUAN_CO_SO/models/yolov8.yaml').load('E:/NIÊN LUẬN CƠ SỞ/code backup/NIEN_LUAN_CO_SO/models/yolov8n.pt')
    
    # Train the model
    results = model.train(data='E:/NIÊN LUẬN CƠ SỞ/code backup/NIEN_LUAN_CO_SO/data/data.yaml', epochs=30, imgsz=640)

if __name__ == "__main__":
    train_model()
