from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from jinja2 import Environment, FileSystemLoader

app = FastAPI()
templater = Environment(loader=FileSystemLoader("templates"))


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def read_root():
    return templater.get_template("index.html").render()


app.mount("/", StaticFiles(directory="static"), name="static")
