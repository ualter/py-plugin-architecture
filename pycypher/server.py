from .plugin_loader import load_plugins
from .plugin_factory import instantiate as plugin_instantiate
from .templates import list_cyphers
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


plugins_list = load_plugins()

app = FastAPI()

@app.get("/")
def read_root():
  html_content = list_cyphers.render(plugins_list)
  return HTMLResponse(content=html_content, status_code=200)