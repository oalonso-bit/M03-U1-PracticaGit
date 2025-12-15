# security.py
def validar_password(password):
    # La contrasenya ha de tenir més de 8 caràcters 
    return len(password) > 8