def slice_simple():
    texto="Awesome"
    print(texto[0:3].lower()) # awe
    print(texto[2:5].lower()) # eso
    print(texto[:4].lower() + texto[4:].lower()) # awesome
slice_simple()
