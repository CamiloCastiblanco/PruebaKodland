# Pygame Proyecto - Juego de Esquivar Enemigos

Bienvenido al Juego de Esquivar Enemigos, un proyecto desarrollado con Pygame. Este juego te desafía a esquivar enemigos que caen desde la parte superior de la pantalla mientras intentas obtener la mayor puntuación posible.

## Descripción del Proyecto

Este proyecto implementa un juego sencillo utilizando Pygame, una biblioteca de juegos en Python. El objetivo del juego es esquivar enemigos que se mueven en la pantalla mientras controlas un jugador con las teclas de dirección.

### Requisitos

Asegúrate de tener instalado lo siguiente:

- [Python 3.x](https://www.python.org/)
- [Pygame](https://www.pygame.org/)
### Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/CamiloCastiblanco/PruebaKodland.git
    ```

2. Navega al directorio del proyecto:

    ```bash
    cd PruebaKodland
    ```

3. Instala las dependencias:

    ```bash
    pip install pygame
    ```
### Ejecución

- Para iniciar el juego, ejecuta el siguiente comando:

    ```bash
    python main.py
    ```
## Juego

El juego incluye:
- **Menú de inicio:**  Para iniciar el juego te aparecerá un menú en dónde debes presionar la tecla "S" para poder comenzar a esquivar enemigos.
- **Menú de pausa:**  Durante el juego puedes presionar la letra "P" si quieres tomarte un descanso.
- **Menú de reinicio:**  Cuando pierdas puedes darte otra oportunidad y presionar la tecla "R" y así intentar romper tu récord.
- **Jugador:** Representado por un rectángulo blanco que se mueve horizontalmente.
- **Enemigos:** Pueden ser verticales y diagonales, representados por rectángulos y triángulos, respectivamente. ¡Evitalos!
- **Puntaje:** Aumenta constantemente mientras juegas. 

## Controles del Juego

- **Izquierda:** Mover el jugador hacia la izquierda.
- **Derecha:** Mover el jugador hacia la derecha.
- **P:** Pausar el juego.

## Personalización del Juego

Puedes personalizar el juego ajustando los siguientes parámetros en el código:

- **Velocidad del jugador y enemigos:** Se puede modificar las velocidades en las funciones `create_object` y `game` según tus preferencias.
- **Umbrales de aparición:** Ajusta los umbrales `vertical_enemy_threshold`, `horizontal_enemy_threshold` y `diagonal_enemy_threshold` para controlar cuándo aparecen diferentes tipos de enemigos.


## Contribuciones

¡Las contribuciones son bienvenidas! Si encuentras problemas o deseas mejorar el juego, no dudes en enviar un _pull request_ o abrir un _issue_.

## Autor

**Brayan Camilo Castiblanco Bernal**  
Correo Electrónico: kmilocastib22@outlook.com

¡Espero que disfrutes del Juego de Esquivar Enemigos y te deseo mucha suerte esquivando esos enemigos que caen implacablemente!

## Licencia

Este proyecto está bajo la [GNU General Public License](LICENSE).

---

