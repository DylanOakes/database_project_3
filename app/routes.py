from flask import Blueprint, render_template

from .models import (
    users,
    a_details,
    a_status,
    team_det,
    team_mem
)

main = Blueprint("main", __name__)



## @main.route("/")
## def index():
##    records = ExampleRecord.query.order_by(ExampleRecord.id.desc()).all()
##    return render_template("index.html", records=records)

