# Se declara la clase Validacion donde se guarda una validación por cada campo
# Si no se cumple la condición se lanza una excepción del tipo Value error

class Validacion:

    def __init__(self) -> None:
        pass

    def validateCodigoProducto(self, codigoProducto):
        if len(codigoProducto) < 0 or len(codigoProducto) > 5:
            raise ValueError(f'El código del producto debe tener como mínimo 1 caracter y un máximo de 50 caracteres, tamaño actual: {len(codigoProducto)}')
        return True

    def validateNombreProducto(self, nombreProducto):
        if len(nombreProducto) < 3 or len(nombreProducto) > 100:
            raise ValueError(f'El nombre del producto debe tener como mínimo 3 caracteres y un máximo de 100 caracteres, tamaño actual: {len(nombreProducto)}')
        return True

    def validateDescripcionProducto(self, descripcionProducto):
        if len(descripcionProducto) < 20 or len(descripcionProducto) > 250:
            raise ValueError(f'La descripción del producto debe tener como mínimo 20 caracteres y un máximo de 250 cafracteres, tamaño actual: {len(descripcionProducto)}')
        return True

    def ValidateTipoProducto(self, tipoProducto):
        if len(tipoProducto) < 0 or len(tipoProducto) > 50:
            raise ValueError(f'El tipo de producto debe tener como mínimo de 1 caracter y 20 caracteres como máximo, tamaño actual: {len(tipoProducto)}')
        return True

    def validateSaborProducto(self, saborProducto):
        if len(saborProducto) < 4 or len(saborProducto) > 20:
            raise ValueError(f'El sabor del producto debe tener como mínimo de 4 caracteres y 20 caracteres como máximo, tamaño actual: {len(saborProducto)}')
        return True

    def ValidateMarca(self, marca):
        if len(marca) < 3 or len(marca) > 20:
            raise ValueError(f'La marca debe tener como mínimo 3 caracteres y como máximo 20 caracteres, tamaño actual: {len(marca)}')
        return True

    def ValidatePresentacion(self, presentacion):
        if len(presentacion) < 8 or len(presentacion) >20:
            raise ValueError(f'La descripción de la presentación debe tener como mínimo 8 caracteres y como máximo 20 caracteres, tamaño actual: {len(presentacion)}')
        return True

    def validateGramaje(self, gramaje):
        if len(gramaje) < 0 or len(gramaje) > 1000:
            raise ValueError(f'El gramaje del producto debe tener como mínimo 1 gramo y como máximo 1000 gramos, tamaño actual: {len(gramaje)}')
        return True

    def ValidateValor(self, valor):
        if len(valor) < 100 or len(valor) > 50000:
            raise ValueError(f'El valor del producto debe ser como mínimo de $100 pesos y como máximo de $50.000 pesos, valor actual: {len(valor)}')
        return True