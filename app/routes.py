from flask import Blueprint
from app import db
from app.models.planet import Planet
from flask import request, Blueprint, make_response

hello_world_bp = Blueprint("hello_world", __name__)
planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


@hello_world_bp.route("/hello-world", methods=["GET"])
def endpoint_name():
    my_beautiful_response_body = "Hello, World!"
    return my_beautiful_response_body

@planets_bp.route("", methods=["POST"])
def handle_planets():
    request_body = request.get_json()
    new_planet = Planet(planet_name=request_body["planet_name"],
                    description=request_body["description"])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.planet_name} successfully created", 201)