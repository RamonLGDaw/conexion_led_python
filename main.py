from fastapi import FastAPI

app = FastAPI()

# Endpoint para controlar el LED
@app.get("/led")
def control_led():
    return 'ON'
#def control_led(state: str = "off"):
    # """
    # Controla el estado de un LED.
    # state puede ser 'on' o 'off' para encender o apagar el LED
    # """
    # if state == "on":
    #     return {"message": "LED encendido"}
    # elif state == "off":
    #     return {"message": "LED apagado"}
    # else:
    #     return {"message": "Estado no válido. Usa 'on' o 'off'."}

@app.get('/')
def inicio():
    return 'FastApi funciona correctamente'