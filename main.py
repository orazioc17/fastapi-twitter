import json
import uuid
from typing import List
from datetime import datetime

from fastapi import FastAPI, status, Body

from models import User, Tweet, TweetPost, UserRegister

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
def signup(user: UserRegister = Body(...)):  # El Body indica que es un body parameter
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
        - birth_date: datetime
    """
    with open("users.json", "r+", encoding="utf-8") as f:
        results = json.load(f)
        user_dict = user.dict()
        user_dict["user_id"] = str(user_dict["user_id"])
        user_dict["birth_date"] = str(user_dict["birth_date"])
        results.append(user_dict)
        f.seek(0)
        json.dump(results, f)
        return user


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
    """
    This path operation shows all users in the app

    Parameters:
        -

    Returns a json list with all the users in the app, with the following data:
        - user_id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        - birth_date: datetime
    """
    with open("users.json", "r+", encoding="utf-8") as f:
        results = json.load(f)
        return results


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
    """
    This path operation shows all tweets in the app

    Parameters:
        -

    Returns a json list with all the tweets in the app, with the following data:
        - content: str
        - created_at: datetime
        - by: User
        - updated_at: datetime
        - tweet_id: UUID
    """
    with open("tweets.json", "r", encoding="utf-8") as f:
        results = json.load(f)
        return results


@app.post(
    path="/tweet",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Post a tweet",
    tags=["Tweets"]
)
def post(tweet: TweetPost = Body(...)):
    """
    Post a tweet

    This path operation post a tweet in the app

    Parameters:
        - Request body parameter
            - tweet: Tweet

    Returns a json with the basic tweet information:
        - tweet_id: UUID
        - content: str
        - created_at: datetime
        - updated_at: Optional[str]
        - by: User
    """
    with open("tweets.json", "r+", encoding="utf-8") as f:
        results = json.load(f)
        tweet_dict = tweet.dict()
        tweet_dict["tweet_id"] = str(uuid.uuid4())
        tweet_dict["created_at"] = str(datetime.now())
        tweet_dict["by"]["user_id"] = str(tweet_dict["by"]["user_id"])
        results.append(tweet_dict)
        print(results)
        f.seek(0)
        json.dump(results, f)
        tweet = Tweet(
            content=tweet_dict["content"],
            by=tweet_dict["by"],
            tweet_id=tweet_dict["tweet_id"],
            created_at=tweet_dict["created_at"]
        )
        return tweet


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
