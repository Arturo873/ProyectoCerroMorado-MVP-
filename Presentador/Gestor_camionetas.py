# Gestor_camionetas.py
from Modelo.Camionetas_data import Camionetas_Data

class Gestor_Camionetas:
    def __init__(self, model):
        self.model = model
        self.camionetas_data = self.model.get_camionetas_data()

    def listar_camionetas_act(self):
        """
        Devuelve una lista de camionetas activas.
        """
        return self.camionetas_data.listar_camionetas_act()

    def listar_camionetas_ina(self):
        """
        Devuelve una lista de camionetas inactivas.
        """
        return self.camionetas_data.listar_camionetas_ina()

    def obtener_marcas(self):
        """
        Llama al método obtener_marcas en camionetas_data para devolver las marcas disponibles.
        """
        return self.camionetas_data.obtener_marcas()

    def agregar_camioneta(self, camioneta):
        """
        Registra una nueva camioneta en la base de datos.
        """
        try:
            patente = camioneta['patente']
            if self.verificar_patente_existente(patente):
                print(f"Error: La patente {patente} ya está registrada.")
                return False

            marca = camioneta['marca']
            modelo = camioneta['modelo']
            estado = camioneta['estado'] == "Activo"
            kilometraje = camioneta['kilometraje']
            ano_fabrica = camioneta['ano_fabrica']
            ano_registro = camioneta['ano_registro']

            return self.camionetas_data.camionetas_DAO.registrar_camioneta(
                patente, marca, modelo, estado, kilometraje, ano_fabrica, ano_registro
            )
        except Exception as e:
            print(f"Error en agregar_camioneta: {e}")
            return False

    def verificar_patente_existente(self, patente):
        """
        Verifica si la patente ya está registrada en la base de datos.
        """
        sql = "SELECT 1 FROM camionetas WHERE patente = %s"
        estado, datos = self.camionetas_data.conectorBD.ejecutarSelectOne(sql, (patente,))
        return estado == 0 and datos
