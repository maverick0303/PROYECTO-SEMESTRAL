def total_carrito(request):
    total = 0
    if request.user.is_authenticated:
        if "carrito" in request.session:
            for key, value in request.session["carrito"].items():
                total += int(value["acumulado"])
    return{"total_carrito": total}

def total_cantidad(request):
    total = 0
    if request.user.is_authenticated:
        if "carrito" in request.session:
            for key, value in request.session["carrito"].items():
                total += int(value["cantidad"])
    return{"total_cantidad": total}

def add_carrito(request):
    if request.user.is_authenticated:
        if "carrito" in request.session:
            x = request.session["carrito"]
            y = len(x)
        else:
            y = 0
    else:
        y = 0   
    return {"total":y}