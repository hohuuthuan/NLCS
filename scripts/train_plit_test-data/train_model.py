from ultralytics import YOLO
def train_model():
    # Build a new model from YAML and load weights
    model = YOLO('models/yolov8.yaml').load('E:/NLCS/models/yolov8n.pt')

    # Train the model
    results = model.train(data='E:/NLCS/data/data.yaml', epochs=50, imgsz=640)

if __name__ == "__main__":
    train_model()