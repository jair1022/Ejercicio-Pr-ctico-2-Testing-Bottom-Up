class CalculadoraDeducciones:
    """Deducciones adicionales."""

    def calcular_adelantos(self, empleado: dict) -> float:
        return float(empleado.get("adelantos", 0.0))

    def calcular_prestamos(self, empleado: dict) -> float:
        return float(empleado.get("cuota_prestamo", 0.0))

    def calcular_otras(self, empleado: dict) -> float:
        return float(empleado.get("otras_deducciones", 0.0))

    def total_deducciones(self, empleado: dict) -> float:
        return round(
            self.calcular_adelantos(empleado)
            + self.calcular_prestamos(empleado)
            + self.calcular_otras(empleado),
            2,
        )
