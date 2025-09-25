import pytest
from modulos.calculadora_impuestos import CalculadoraImpuestos
from modulos.calculadora_bonos import CalculadoraBonos
from modulos.calculadora_deducciones import CalculadoraDeducciones
from drivers.test_driver import TestDriver
from nomina_sistema import NominaSistema

# ========== Nivel 1 ==========
class TestNivelBase:
    def test_impuestos_con_driver(self):
        calc = CalculadoraImpuestos()
        driver = TestDriver(calc)
        assert "OK" in driver.ejecutar_prueba_unitaria("calcular_isr", [8000], 400.0)
        assert "OK" in driver.ejecutar_prueba_unitaria("calcular_seguro_social", [10000], 625.0)

    def test_bonos_unitarios(self):
        calc = CalculadoraBonos()
        empleado = {"salario_base": 10000, "desempeno": 1.0, "antiguedad_anios": 5}
        assert calc.calcular_bonos(empleado) == 2500.0

    def test_deducciones_unitarias(self):
        calc = CalculadoraDeducciones()
        empleado = {"adelantos": 200, "cuota_prestamo": 300, "otras_deducciones": 50}
        assert calc.total_deducciones(empleado) == 550.0

# ========== Nivel 2 ==========
class TestIntegracionParcial:
    def test_bonos_e_impuestos(self):
        imp = CalculadoraImpuestos()
        bon = CalculadoraBonos()
        empleado = {"salario_base": 12000, "desempeno": 0.5, "antiguedad_anios": 2}
        assert imp.calcular_isr(12000) == 1200.0
        assert bon.calcular_bonos(empleado) == 1440.0

# ========== Nivel 3 ==========
class TestIntegracion:
    def test_nomina_completa(self):
        sistema = NominaSistema()
        empleado = {
            "salario_base": 10000,
            "desempeno": 0.5,
            "antiguedad_anios": 1,
            "adelantos": 0,
            "cuota_prestamo": 0,
            "otras_deducciones": 0,
        }
        assert sistema.calcular_nomina_neta(empleado) == 9975.0
