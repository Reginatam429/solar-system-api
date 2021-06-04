from app import db
from app.models.planet import Planet
from flask import request, Blueprint, make_response, jsonify

hello_world_bp = Blueprint("hello_world", __name__)
planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


@hello_world_bp.route("/hello-world", methods=["GET"])
def endpoint_name():
    my_beautiful_response_body = "Hello, World!"
    return my_beautiful_response_body

@planets_bp.route("", methods=["GET","POST"])
def handle_planets():
    if request.method == "GET":
        planets = Planet.query.all()
        planets_response = []
        for planet in planets:
            planets_response.append({
                "id": planet.id,
                "planet_name": planet.planet_name,
                "description": planet.description
            })
        return jsonify(planets_response)
    elif request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(planet_name=request_body["planet_name"],
                        description=request_body["description"])

        db.session.add(new_planet)
        db.session.commit()

    return make_response(f"Planet {new_planet.planet_name} successfully created", 201)