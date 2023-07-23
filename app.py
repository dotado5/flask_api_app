from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS
from flask_session import Session
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager


client = MongoClient(
    "mongodb+srv://oguntolagifted:Ebun777$@cluster0.2qfnfey.mongodb.net/?retryWrites=true&w=majority",
    serverSelectionTimeoutMS=5000,
    connect=False,
)

db = client.FY_project
collection = db["students result"]

resource = {r"/api/*": {"origins": ["http://localhost:3000"]}}

app = Flask(__name__)
Session(app)
jwt = JWTManager(app)
bcrypt = Bcrypt(app)
CORS(app)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"


# function for update of all the results
@app.route("/general-update", methods=["POST"])
def general_update_data():
    data = request.get_json()
    name = data["name"]
    matric = data["matric"]
    # course_code = data["course_code"]
    tutorial_score = int(data["tutorial_score"])
    if int(data["practical_score"]) | int(data["test_score"]) | int(data["exam_score"]):
        practical_score = int(data["practical_score"])
        test_score = int(data["test_score"])
        exam_score = int(data["exam_score"])
    else:
        practical_score = 0
        test_score = 0
        exam_score = 0
    total = int(data["total"])
    # print(tutorial_score, practical_score)
    if total < 100:
        feedback = "Excellent work, Your hard work and effort are evident in your results. welldone"
        if total < 70:
            feedback = "Your score was great, but could be better."
        if total < 60:
            feedback = "Your grade was okay, you should do better next time."
        if total < 50:
            feedback = "Poor grade, try to do better next time"
        if total < 40:
            feedback = "Very poor grade, put in more effort next time."
        if exam_score == 0:
            feedback = "please check with your class rep or your lecturer, to make sure your script was marked"
    else:
        feedback = "het"

    # update data to MongoDB collection
    collection.find_one_and_update(
        {"matric": matric},
        {
            "$set": {
                "name": name,
                "tutorial_score": tutorial_score,
                "practical_score": practical_score,
                "test_score": test_score,
                "exam_score": exam_score,
                "feedback": feedback,
                "total": total,
            }
        },
    )
    # collection.insert_one(data)

    return "Data uploaded successfully"


# function for updata of all results except exam
@app.route("/pratical-test-update", methods=["POST"])
def practical_test_update_data():
    data = request.get_json()
    name = data["name"]
    matric = data["matric"]
    # course_code = data["course_code"]
    tutorial_score = int(data["tutorial_score"])
    if int(data["practical_score"]) | int(data["test_score"]) | int(data["exam_score"]):
        practical_score = int(data["practical_score"])
        test_score = int(data["test_score"])
        exam_score = int(data["exam_score"])
    else:
        practical_score = 0
        test_score = 0
        exam_score = 0
    total = data["total"]
    print(tutorial_score, practical_score)
    if test_score < 20:
        feedback = "Your test score was great, keep up the good work"
        if test_score < 15:
            feedback = "Your test score was okay but you could do better"
        if test_score < 10:
            feedback = "Your test score was poor put more effort into your exams"
        if test_score == 0:
            feedback = "please check with your class rep or your lecturer, to make sure your test score was recorded"
    else:
        feedback = "het"

    # update data to MongoDB collection
    collection.find_one_and_update(
        {"matric": matric},
        {
            "$set": {
                "name": name,
                "tutorial_score": tutorial_score,
                "practical_score": practical_score,
                "test_score": test_score,
                "exam_score": exam_score,
                "feedback": feedback,
                "total": total,
            }
        },
    )
    # collection.insert_one(data)

    return "Data uploaded successfully"


# function for update of tutorial and practical scores
@app.route("/pratical-update", methods=["POST"])
def practical_update_data():
    data = request.get_json()
    name = data["name"]
    matric = data["matric"]
    # course_code = data["course_code"]
    tutorial_score = int(data["tutorial_score"])
    if int(data["practical_score"]) | int(data["test_score"]) | int(data["exam_score"]):
        practical_score = int(data["practical_score"])
        test_score = int(data["test_score"])
        exam_score = int(data["exam_score"])
    else:
        practical_score = 0
        test_score = 0
        exam_score = 0
    total = data["total"]
    print(tutorial_score, practical_score)
    if practical_score < 10:
        feedback = "Your practical score was great, keep up the good work"
        if practical_score < 8:
            feedback = "Your practical score was okay but you could do better"
        if practical_score < 5:
            feedback = (
                "Your practical score was poor put more effort into your test and exams"
            )
        if practical_score == 0:
            feedback = "please check with your class rep or your lecturer, to make sure your practical score was recorded"
    else:
        feedback = "prac"

    # update data to MongoDB collection
    collection.find_one_and_update(
        {"matric": matric},
        {
            "$set": {
                "name": name,
                "tutorial_score": tutorial_score,
                "practical_score": practical_score,
                "test_score": test_score,
                "exam_score": exam_score,
                "feedback": feedback,
                "total": total,
            }
        },
    )
    # collection.insert_one(data)

    return "Data uploaded successfully"


@app.route("/tutorial-update", methods=["POST"])
def tutorial_update_data():
    data = request.get_json()
    name = data["name"]
    matric = data["matric"]
    # course_code = data["course_code"]
    tutorial_score = int(data["tutorial_score"])
    if int(data["practical_score"]) | int(data["test_score"]) | int(data["exam_score"]):
        practical_score = int(data["practical_score"])
        test_score = int(data["test_score"])
        exam_score = int(data["exam_score"])
    else:
        practical_score = None
        test_score = None
        exam_score = None
    total = int(data["total"])
    print(tutorial_score, practical_score)
    if tutorial_score < 10:
        feedback = "You did very well, keep up the good work"
        if tutorial_score < 8:
            feedback = "Your score was okay but you could do better"
        if tutorial_score < 5:
            feedback = "Your tutorial score was poor, put more effort into your practical, test and exams"
        if tutorial_score == 0:
            feedback = "please check with your class rep or your lecturer, to make sure your tutorial score was recorded"
    else:
        feedback = "het"

    # update data to MongoDB collection
    collection.find_one_and_update(
        {"matric": matric},
        {
            "$set": {
                "name": name,
                "tutorial_score": tutorial_score,
                "practical_score": practical_score,
                "test_score": test_score,
                "exam_score": exam_score,
                "feedback": feedback,
                "total": total,
            }
        },
    )
    # collection.insert_one(data)

    return "Data uploaded successfully"


@app.route("/create", methods=["POST"])
def upload_data():
    data = request.get_json()
    name = data["name"]
    matric = data["matric"]
    password = data["password"]

    # Insert data into MongoDB collection
    collection.insert_one(data)

    return "Data uploaded successfully"


@app.route("/signin", methods=["POST"])
def signin():
    data = request.get_json()
    matric = data["matric"]
    password = data["password"]
    user = collection.find_one({"matric": matric})
    if user:
        if user["password"] == password:
            user_matric = user["matric"]
            user_name = user["name"]
            if user["feedback"] == None:
                user_feedback = "--"
            else:
                user_feedback = user["feedback"]
            if user["tutorial_score"] == None:
                user_tut_score = "--"
            else:
                user_tut_score = user["tutorial_score"]
            if user["total"] == None:
                user_total = "--"
            else:
                user_total = user["total"]
            if user["practical_score"] == None:
                user_prac_score = "--"
            else:
                user_prac_score = user["practical_score"]
            if user["test_score"] == None:
                user_test_score = "--"
            else:
                user_test_score = user["test_score"]
            if user["exam_score"] == None:
                user_exam_score = "--"
            else:
                user_exam_score = user["exam_score"]
            # print(
            #     user_matric,
            #     user_name,
            #     user_tut_score,
            #     user_prac_score,
            #     user_test_score,
            #     user_exam_score,
            #     user_feedback,
            #     user_total,
            # )
            return (
                jsonify(
                    {
                        "success": True,
                        "message": "Logged in successfully",
                        "user_matric": user_matric,
                        "user_name": user_name,
                        "user_tut_score": user_tut_score,
                        "user_prac_score": user_prac_score,
                        "user_test_score": user_test_score,
                        "user_exam_score": user_exam_score,
                        "user_feedback": user_feedback,
                        "user_total": user_total,
                    }
                ),
                200,
            )
        else:
            return jsonify({"success": False, "message": "Incorrect Password"}), 480


if __name__ == "__main__":
    app.run(port=5000)

    # if exam_score:
    #     if test_score < 20:
    #         feedback = "Your test score was great, keep up the good work"
    #     if test_score < 15:
    #         feedback = "Your test score was okay but you could do better"
    #     if test_score > 0 < 10:
    #         feedback = "Your test score was poor put more effort into your exams"
    #     if test_score < 0:
    #         feedback = "please check with your class rep or your lecturer, to make sure your script was marked"
