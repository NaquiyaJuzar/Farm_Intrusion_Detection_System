import sys,os
from signLanguage.utils.main_utils import decodeImage, encodeImageIntoBase64
from flask import Flask, request, jsonify, render_template,Response
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"


    

@app.route("/")
def home():
    return render_template("index.html")



@app.route("/predict", methods=['POST', 'GET'])
@cross_origin()
def predictRoute():
    try:
        # Step 1: Get the image from request
        image = request.json['image']
        
        # Step 2: Decode and save the image to a fixed filename
        decodeImage(image, clApp.filename)  # clApp.filename = 'inputImage.jpg'

        # Step 3: Run YOLOv5 detection
        os.system(
            "cd yolov5/ && python detect.py "
            "--weights best.pt "
            "--img 416 --conf 0.5 "
            "--source ../data/inputImage.jpg "
            "--data data/coco128.yaml "
            "--project runs/detect --name predict --exist-ok"
        )


        # Step 4: Read the output image as Base64 to send back to frontend
        output_path = "yolov5/runs/detect/predict/inputImage.jpg"
        opencodedbase64 = encodeImageIntoBase64(output_path)

        # Step 5: Return the Base64 image string
        result = {"image": opencodedbase64.decode('utf-8')}

        # Step 6: (Optional) Clean up the runs folder to avoid storage buildup
        os.system("rm -rf yolov5/runs")

    except ValueError as val:
        print("ValueError:", val)
        return Response("Value not found inside JSON data", status=400)

    except KeyError:
        print("KeyError: 'image' key is missing in request")
        return Response("Key value error: incorrect key passed", status=400)

    except Exception as e:
        print("Unexpected Error:", e)
        return jsonify({"error": "Invalid input or internal error"}), 500

    return jsonify(result)



@app.route("/live", methods=['GET'])
@cross_origin()
def predictLive():
    try:
        os.system("cd yolov5/ && python detect.py --weights best.pt --img 416 --conf 0.5 --source 0")
        os.system("rm -rf yolov5/runs")
        return "Camera starting!!" 

    except ValueError as val:
        print(val)
        return Response("Value not found inside  json data")
    





if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host="0.0.0.0", port=5050)
