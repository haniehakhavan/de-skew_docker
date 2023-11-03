import cv2
from flask import Flask, request


import skew_orient_est
import rotate

app = Flask(__name)


@app.route('/deskew', methods=['POST'])
def deskew():
    # Ensure the request contains an image file
    if 'image' not in request.files:
        return {"status": "No image provided."}

    # Read the image from the request
    image_file = request.files['image']
    original_filename = image_file.filename

    org_image = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_COLOR)
    # org_image = cv2.imread(image_path)
    image = cv2.cvtColor(org_image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, (224, 224))
    orientation = skew_orient_est.orientation_estimate(image)
    orientation_degree_dict = {"down": 180,
                               "left": 90,
                               "right": -90,
                               "up": 0}
    degree = orientation_degree_dict[orientation]
    if degree != 0:
        image = rotate.rotate_image(image, degree)

    skew = skew_orient_est.skew_estimate(image)
    final_skew = degree + (-skew)
    deskewed_image = rotate.rotate_image(org_image, final_skew)
    save_path = os.path.join("/data", original_filename)
    cv2.imwrite(save_path, deskewed_image)
    return {"status": "success."}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6060)
