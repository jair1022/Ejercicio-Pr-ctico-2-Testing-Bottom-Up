from modulos.calculadora_impuestos import CalculadoraImpuestos
from modulos.calculadora_bonos import CalculadoraBonos
from modulos.calculadora_deducciones import CalculadoraDeducciones

class NominaSistema:
    """Sistema integrado usando los módulos."""

    def __init__(self):
        self.calc_impuestos = CalculadoraImpuestos()
        self.calc_bonos = CalculadoraBonos()
        self.calc_deducciones = CalculadoraDeducciones()

    def calcular_nomina_neta(self, empleado: dict) -> float:
        salario = float(empleado["salario_base"])
        isr = self.calc_impuestos.calcular_isr(salario)
        seguro = self.calc_impuestos.calcular_seguro_social(salario)
        bonos = self.calc_bonos.calcular_bonos(empleado)
        deducciones = self.calc_deducciones.total_deducciones(empleado)
        neto = salario + bonos - isr - seguro - deducciones
        return round(neto, 2)

    def detalle_nomina(self, empleado: dict) -> dict:
        salario = float(empleado["salario_base"])
        isr = self.calc_impuestos.calcular_isr(salario)
        seguro = self.calc_impuestos.calcular_seguro_social(salario)
        bonos = self.calc_bonos.calcular_bonos(empleado)
        deducciones = self.calc_deducciones.total_deducciones(empleado)
        neto = round(salario + bonos - isr - seguro - deducciones, 2)
        return {
            "bruto": salario,
            "isr": isr,
            "seguro": seguro,
            "bonos": bonos,
            "deducciones": deducciones,
            "neto": neto,
        }
