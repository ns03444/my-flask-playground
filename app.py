from flask import Flask, request

app = Flask(__name__)

teams=[
    {
        "name": "Rams"
    }
]

@app.get("/teams")
def get_teams():
    return {"teams":teams}

# @app.post("/teams")
# def create_team():
#     request_data = request.get_json()
#     new_team = {"name": request_data['name']}
#     teams.append(new_team)
#     return new_team, 201