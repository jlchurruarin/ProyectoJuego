from animacion import Animacion

shoot_r = Animacion(
            path="Proyecto de Juego (Clase 19)/images/caracters/stink/jump.png",
            columnas=33,
            filas=1,
            flip=False,
            start_frame=12,
            end_frame=14,
            normal_loop=False,
            scale= 100
        )

print(shoot_r.next_frame())
print(shoot_r.next_frame())
print(shoot_r.next_frame())