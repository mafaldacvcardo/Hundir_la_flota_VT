

# 🛳️ Batalla Naval en Python

Un juego clásico de **Batalla Naval (Hundir la flota)** implementado completamente en **Python** usando la librería `NumPy`.  
Compite contra la máquina, dispara, acierta y hunde todos sus barcos antes de que ella hunda los tuyos.

---

## 📜 Descripción

Este proyecto recrea el juego de **Batalla Naval** (o *Battleship*) en modo consola.  
El jugador y la máquina tienen tableros de 10x10 donde se colocan barcos de diferentes tamaños (*esloras*) de forma aleatoria.  

Durante el juego, ambos turnos se alternan:
- El jugador elige una casilla para disparar (por coordenadas).
- La máquina realiza disparos aleatorios evitando repetir casillas.
- El primero en hundir todos los barcos del oponente gana.

---

## 🧩 Características principales

- ✅ Tablero de tamaño configurable (por defecto 10x10).  
- 🚢 Colocación aleatoria de barcos sin superposición.  
- 💥 Detección de impactos, hundimientos y disparos repetidos.  
- 🧠 IA básica para la máquina (disparos aleatorios sin repetir).  
- 🖥️ Interfaz de texto simple y clara en consola.  

---

## ⚙️ Requisitos

Asegúrate de tener instalado **Python 3.8+** y la librería **NumPy**:

```bash
pip install numpy
