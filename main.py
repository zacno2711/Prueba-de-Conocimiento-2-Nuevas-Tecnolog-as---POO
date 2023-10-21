class RegistroProducto:
    def __init__(self):
        self.productos = {}

    def registrar_producto(self):
        id = input("id: ")
        nombre = input("nombre: ")
        descripcion = input("descripcion: ")
        costo = int(input("costo: "))
        cantidad = int(input("cantidad: "))
        margen_de_venta = float(input("margen de venta: "))

        precio_venta = round(costo / (1 - margen_de_venta),2)
        producto = {
            'id': id,
            'nombre': nombre,
            'descripcion': descripcion,
            'costo': costo,
            'cantidad': cantidad,
            'precio_venta': precio_venta
        }
        self.productos[id] = producto

    def imprimir_productos(self):
        print("Listado de productos:")
        for id, producto in self.productos.items():
            print(f"ID: {id}, Nombre: {producto['nombre']}, Descripción: {producto['descripcion']}, "
                  f"Costo: {producto['costo']}, Cantidad: {producto['cantidad']}, Precio de Venta: {producto['precio_venta']}")


registro = RegistroProducto()
registro.registrar_producto()
registro.imprimir_productos()