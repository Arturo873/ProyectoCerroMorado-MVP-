# 🏔️ Proyecto Cerro Morado - MVP  
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-brightgreen?logo=python&logoColor=white)](#)  
[![Language](https://img.shields.io/badge/Language-Python-blue?logo=python&logoColor=white)](#)  
[![Status](https://img.shields.io/badge/Project%20Status-In%20Development-yellow)]()  
[![License](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)  

---

### 🇪🇸 Descripción  
**ProyectoCerroMorado** es un sistema automatizado para la gestión de la flota de camionetas de la minera Cerro Morado. Permite:  

- Registrar y actualizar información de camionetas.  
- Controlar el kilometraje diario de unidades activas.  
- Gestionar cuentas de usuario con **roles y permisos** (Administrador del Sistema, Jefe de Flota, Supervisor de Flota).  
- Eliminar camionetas inactivas de manera masiva.  
- Generar reportes de uso y supervisión de la flota.  

**Objetivo:** Mejorar la eficiencia en la gestión de la flota, reducir errores en los registros manuales y sentar las bases para futuras mejoras del sistema.

---

### Tecnologías y arquitectura  
- **Lenguaje:** Python  
- **Librería:** Tkinter (interfaz gráfica)  
- **Base de Datos:** MySQL  
- **Patrón de Arquitectura:** **MVP (Modelo-Vista-Presentador)**  
- **Metodología de Gestión:** Ágil (Scrum) con Azure DevOps  

#### Explicación del patrón MVP:  
1. **Modelo (Model):** Gestiona los datos y la lógica de negocio.  
2. **Vista (View):** Interfaz gráfica que muestra datos y recibe acciones del usuario.  
3. **Presentador (Presenter):** Intermediario que recibe eventos de la Vista, solicita datos al Modelo y actualiza la Vista.  

Este patrón permite separar claramente la **interfaz de usuario de la lógica de negocio**, facilitando mantenimiento, pruebas y escalabilidad del sistema.

---

### Funcionalidades principales  
- Registro y control de kilometraje de camionetas activas.  
- Gestión masiva de registros de la flota.  
- Administración de cuentas de usuario con roles y permisos.  
- Eliminación masiva de camionetas inactivas.  
- Generación de reportes de kilometraje y supervisión de la flota.  
- Interfaz gráfica funcional .

---


