class CalculadoraImpuestos:
    """Módulo base para cálculo de impuestos."""

    def calcular_isr(self, salario_base: float) -> float:
        if salario_base <= 10000:
            return salario_base * 0.05
        elif salario_base <= 20000:
            return salario_base * 0.10
        else:
            return salario_base * 0.15

    def calcular_seguro_social(self, salario_base: float) -> float:
        return salario_base * 0.0625
