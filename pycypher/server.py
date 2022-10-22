import os
from typing import Dict, Any
from .plugin_manager import uninstall as plugin_uninstall
from .plugin_manager import load_plugins as plugin_load
from .plugin_manager import install_plugin as plugin_install
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory=f"{__package__}/static"), name="static")
templates = Jinja2Templates(directory=f"{__package__}/templates")

app.plugin_list = plugin_load()

@app.get("/")
def read_root(request: Request):
  return templates.TemplateResponse("index.html", 
        {
          "request": request, 
          "cyphers": app.plugin_list["plugins"]
        }
  )

@app.get("/uninstall/{plugin}")
def uninstall(request: Request, plugin: str):
  plugin_uninstall(app.plugin_list, plugin)
  app.plugin_list = plugin_load()
  redirect_url = request.url_for('read_root')
  return RedirectResponse(redirect_url, status_code=303)

@app.post("/uploadfiles/")
async def create_upload_file(request: Request, file: UploadFile):
    if not file:
        return {"message": "No file sent"}
    else:
      try:
          plugin_install(file)
      except Exception:
          raise Exception
      finally:
          file.file.close()
      app.plugin_list = plugin_load()    
      redirect_url = request.url_for('read_root')
      return RedirectResponse(redirect_url, status_code=303)


@app.get("/reload")
def read_root(request: Request):
  app.plugin_list = plugin_load()
  redirect_url = request.url_for('read_root')
  return RedirectResponse(redirect_url, status_code=303)
  

