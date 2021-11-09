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

toyapis = []
toyapi_list = [
    "https://i5.walmartimages.com/asr/35e46d6a-118d-4f93-bbdc-1afa719ae006_1.87845513c6d388ab4f25ad5db150fcd7.jpeg?odnHeight=612&odnWidth=612&odnBg=FFFFFF",
    "https://i5.walmartimages.com/asr/1184195e-de3c-47f1-b48b-7bc7763e042f.192ec508863ae402296fcbaa025368f1.jpeg?odnHeight=612&odnWidth=612&odnBg=FFFFFF",
    "https://i5.walmartimages.com/asr/3c58b072-80c6-4fe4-bd77-a3b8023a733a_3.d88f70ff6884621607fa48df1cda78b0.jpeg?odnHeight=612&odnWidth=612&odnBg=FFFFFF",
    "https://i5.walmartimages.com/asr/89df7e3c-0ca8-46b7-bd9b-70a6633ef0c6.cfaa19f8d7d2ceeed6acde845c85f420.jpeg?odnHeight=612&odnWidth=612&odnBg=FFFFFF",
    "https://i5.walmartimages.com/asr/66b1fdc9-f788-445e-9d3c-cbe5ccac3cc1.3a73b81800c180962abdb630c2f5ddd9.jpeg?odnHeight=612&odnWidth=612&odnBg=FFFFFF",
    "https://i5.walmartimages.com/asr/d203b6a9-350e-4b65-9bf7-f00848e19c77.07f4e40b3c0244ba6a738bb26342e0a7.jpeg?odnHeight=612&odnWidth=612&odnBg=FFFFFF",
    "https://i5.walmartimages.com/asr/6a6df5d1-c8d1-49c1-bf20-77fe5fd12a5d_1.47cf8ce7577702ae3d9b8f17085df5ee.jpeg?odnHeight=612&odnWidth=612&odnBg=FFFFFF",
    "https://i5.walmartimages.com/asr/4c1030dc-d0e4-4ebb-9417-144a3e16e937_1.b41508d1731e263429a94827969fe15e.jpeg?odnHeight=612&odnWidth=612&odnBg=FFFFFF",
    "https://i5.walmartimages.com/asr/e4b13995-6ab9-444b-944a-68a7e71627f3.70a027398be757f85d2e42e3558c7fe9.jpeg?odnHeight=612&odnWidth=612&odnBg=FFFFFF"
]

def _find_next_id():
    return max(toyapis["id"] for toyapi in toyapis) + 1


def _init_toyapis():
    id = 1
    for toyapi in toyapi_list:
        toyapis.append({"id": id, "toyapi": toyapi, "haha": 0, "boohoo": 0})
        id += 1


@api_bp.route('/toyapi')
def get_toyapi():
    if len(toyapis) == 0:
        _init_toyapis()
        print(toyapis)
    return jsonify(random.choice(toyapis))


@api_bp.route('/toyapis')
def get_toyapis():
    if len(toyapis) == 0:
        _init_toyapis()
    return jsonify(toyapis)


if __name__ == "__main__":
    print(random.choice(toyapi_list))

eq1 = (1,6)
eq2 = (4,5)
eq3 = (2,3)
eq4 = (3,1)
eq5 = (7,2)

additions = []
addition_list = [
    eq1,
    eq2,
    eq3,
    eq4,
    eq5,
]

def _find_next_id():
    return max(additions["id"] for addition in additions) + 1


def _init_additions():
    id = 1
    for addition in addition_list:
        additions.append({"id": id, "addition": addition, "haha": 0, "boohoo": 0})
        id += 1


@api_bp.route('/addition')
def get_addition():
    if len(additions) == 0:
        _init_additions()
    return jsonify(random.choice(additions))


@api_bp.route('/additions')
def get_additions():
    if len(additions) == 0:
        _init_additions()
    return jsonify(additions)


if __name__ == "__main__":
    print(random.choice(addition_list))

    [{'id': 1, 'toyapi': 'https://i5.walmartimages.com/asr/50250727-4357-441d-9b85-f251b0036cec.5800e03cef5137ac7a5233862da3fa22.jpeg?odnHeight=612&odnWidth=612&odnBg=FFFFFFg', 'haha': 0, 'boohoo': 0},
     {'id': 2, 'toyapi': 'https://www.lego.com/cdn/cs/set/assets/blt892f38a4fd55edeb/75257.jpg?fit=bounds&format=jpg&quality=80&width=1500&height=1500&dpr=1', 'haha': 0, 'boohoo': 0},
     {'id': 3, 'toyapi': 'https://m.media-amazon.com/images/I/81dIEAgoytL._AC_SL1500_.jpg', 'haha': 0, 'boohoo': 0}]

