<<<<<<< HEAD
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():

    return {"message": "Hello ,fastapi"}
=======
def main():
    print("Hello from fast-api!")


if __name__ == "__main__":
    main()
>>>>>>> 197cbd6fb45eea24fdd20c91eba594eb3507e4f6
