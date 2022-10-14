from typing import List

from fastapi import FastAPI, status

from models import User, Tweet

app = FastAPI()


# Path operations

# Users
@app.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register new User",
    tags=["Users"]
)
def signup():
    """
    Signup

    This path operation register a user in the app

    Parameters:
        - Request body parameter
            - user: UserRegister

    Returns a json with user's basic information:
        - user_id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        - birth_date: datetime.date
    """
    pass


@app.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="User login",
    tags=["Users"]
)
def login():
    pass


@app.get(
    path="/users",
    response_model=List[User],  # Con esto le decimos que el json de respuesta va a contener una lista
    status_code=status.HTTP_200_OK,
    summary="Show all users",
    tags=["Users"]
)
def show_all_users():
    pass


@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show User",
    tags=["Users"]
)
def show_user():
    pass


@app.delete(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a User",
    tags=["Users"]
)
def delete_user():
    pass


@app.put(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update User",
    tags=["Users"]
)
def update_user():
    pass


# Tweets
@app.get(
    path="/",
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary="Shows all tweets",
    tags=["Tweets"]
)
def home():
    return {"Twitter API": "Working!"}


@app.post(
    path="/tweet",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Post a tweet",
    tags=["Tweets"]
)
def post():
    pass


@app.get(
    path="/tweet/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Get a tweet",
    tags=["Tweets"]
)
def get_tweet():
    pass


@app.delete(
    path="/tweet/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Delete a tweet",
    tags=["Tweets"]
)
def delete_tweet():
    pass


@app.put(
    path="/tweet/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Update a tweet",
    tags=["Tweets"]
)
def update_tweet():
    pass
