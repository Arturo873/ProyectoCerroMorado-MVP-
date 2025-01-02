from Modelo.Camionetas_DAO import Camionetas_DAO
from Modelo.ConectorBD import ConectorBD

class Camionetas_Data:
    def __init__(self):
        self.conectorBD = ConectorBD(hostdb="localhost", userdb="root", passwordb="root", basedatosdb="dbminera")
        estado, mensaje = self.conectorBD.activarConexion()
        if estado != 0:
            print(f"Error al conectar: {mensaje}")
        self.camionetas_DAO = Camionetas_DAO(self.conectorBD)

    def listar_camionetas_act(self):
        """
        Devuelve las camionetas activas.
        """
        return self.camionetas_DAO.recupera_camionetas_act()

    def listar_camionetas_ina(self):
        """
        Devuelve las camionetas inactivas.
        """
        return self.camionetas_DAO.recupera_camionetas_ina()

    def obtener_marcas(self):
        """
        Devuelve una lista de marcas disponibles.
        """
        try:
            cursor = self.conectorBD.conexion.cursor()
            cursor.execute("SELECT id, nombre FROM marcas")
            marcas = cursor.fetchall()
            return [marca[1] for marca in marcas]
        except Exception as err:
            print(f"Error al obtener marcas: {err}")
            return []
