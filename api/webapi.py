import random

from flask import Blueprint, jsonify
# webapi
api_bp = Blueprint('api', __name__,
                   url_prefix='/api',
                   template_folder='templates',
                   static_folder='static', static_url_path='static/api')

cars = []
car_list = [
    "https://store.storeimages.cdn-apple.com/8756/as-images.apple.com/is/HN8R2?wid=1144&hei=1144&fmt=jpeg&qlt=95&op_usm=0.5,0.5&.v=1562949198423",
    "https://i5.walmartimages.com/asr/de64c976-8cd1-4cdf-bda0-30a2384d9d71_1.8278bafec76e3ebc45acc969bdaa2cc0.jpeg",
    "https://i5.walmartimages.com/asr/d9ba5c62-c5fc-4387-8493-867f4f6aed23.6055eb4a5a1a0a0831ca7af409b4c003.jpeg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSkm-Ab4dXJpnJNz7Xd_gSOATYU6pxfrWfxfA&usqp=CAU",
    "https://cdn.motor1.com/images/mgl/RP77r/s1/hot-wheels-ultimate-drive-thru-twin-mill.jpg"

]


def _find_next_id():
    return max(cars["id"] for car in cars) + 1


def _init_cars():
    id = 1
    for car in car_list:
        cars.append({"id": id, "car": car, "haha": 0, "boohoo": 0})
        id += 1


@api_bp.route('/car')
def get_car():
    if len(cars) == 0:
        _init_cars()
    return jsonify(random.choice(cars))


@api_bp.route('/cars')
def get_cars():
    if len(cars) == 0:
        _init_cars()
    return jsonify(cars)


if __name__ == "__main__":
    print(random.choice(car_list))


mcolors = []
mcolor_list = [
    "https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Solid_blue.svg/225px-Solid_blue.svg.png",
    "https://upload.wikimedia.org/wikipedia/en/8/8b/Purplecom.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/8/89/Alizarin_crimson_%28color%29.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/d/d0/Color-yellow.JPG",
    "https://upload.wikimedia.org/wikipedia/commons/e/ee/Flag_Admirals_of_the_Blue_Squadron_Royal_Navy.png",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Flag_of_Libya_%281977%E2%80%932011%29.svg/300px-Flag_of_Libya_%281977%E2%80%932011%29.svg.png",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Solid_green.svg/1024px-Solid_green.svg.png"

]


def _find_next_id():
    return max(mcolors["id"] for mcolor in mcolors) + 1


def _init_mcolors():
    id = 1
    for mcolor in mcolor_list:
        mcolors.append({"id": id, "mcolor": mcolor, "haha": 0, "boohoo": 0})
        id += 1


@api_bp.route('/mcolor')
def get_mcolor():
    if len(mcolors) == 0:
        _init_mcolors()
    return jsonify(random.choice(mcolors))


@api_bp.route('/mcolors')
def get_mcolors():
    if len(mcolors) == 0:
        _init_mcolors()
    return jsonify(mcolors)


if __name__ == "__main__":
    print(random.choice(mcolor_list))
