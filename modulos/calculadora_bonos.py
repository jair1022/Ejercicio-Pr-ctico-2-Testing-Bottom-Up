class CalculadoraBonos:
    """Cálculo de bonos por desempeño y antigüedad."""

    def calcular_bonos(self, empleado: dict) -> float:
        salario = empleado.get("salario_base", 0.0)
        desempeno = max(0.0, min(1.0, empleado.get("desempeno", 0.0)))
        años = max(0, int(empleado.get("antiguedad_anios", 0)))

        bono_desempeno = salario * (0.20 * desempeno)
        bono_antiguedad = salario * (0.01 * min(años, 10))
        return round(bono_desempeno + bono_antiguedad, 2)
