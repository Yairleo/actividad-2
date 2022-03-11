from api.library import *

def main():
# #aplicacion de los diccionarios
#     persona = {
#         "nombre": "Yair",
#         "apellidos": "Quintana",
#         "Edad": 23
    
#     }
    persona ={
        "datospersonales":{
            "nombre": "Yair",
            "apellido": "Quintana",
            "edad": 23
        },
            
        "salarial": {
            "salario": 3000000,
            "subtransporte": 40000,
            "subalimentacion": 30000
        }
    }    
    # print(persona["nombre"]+ " "+ persona)["apellidos"]
    
    #print(f"{persona['nombre']} {persona['apellidos']}")
    print(f"nombre: {persona['datospersonales']['nombre']} {persona['datospersonales']['apellido']}")
    

if __name__ == "__main__":
    main()