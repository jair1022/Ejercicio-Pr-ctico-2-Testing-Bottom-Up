class TestDriver:
    """Driver para pruebas unitarias de módulos."""

    def __init__(self, modulo):
        self.modulo = modulo
        self.resultados = []

    def ejecutar_prueba_unitaria(self, metodo: str, parametros: list, esperado: float, tol: float = 0.01):
        resultado = getattr(self.modulo, metodo)(*parametros)
        exito = abs(resultado - esperado) <= tol
        self.resultados.append({
            "metodo": metodo,
            "parametros": parametros,
            "resultado": resultado,
            "esperado": esperado,
            "exito": exito,
        })
        assert exito, f"Fallo en {metodo}: {resultado} != {esperado}"
        return f"✓ {metodo}: OK"
