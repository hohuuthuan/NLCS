from ultralytics import YOLO

def evaluate_model():
    # Load the trained model
    model = YOLO('E:/NLCS/models/best.pt')

    # Evaluate the model on the test dataset
    results = model.val(data='E:/NLCS/data/data.yaml', split='test')

if __name__ == "__main__":
    evaluate_model()

