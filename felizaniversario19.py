import webbrowser

html = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Amor Infinito</title>
    <style>
        html, body {
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100%;
            background: #000000;
            overflow: hidden;
            font-family: 'Garamond', serif;
            font-style: italic;
        }

        .frase {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            color: #ff99cc;
            font-size: 4.5em;
            text-align: center;
            padding: 0 30px;
            z-index: 2;
            text-shadow: 0 0 40px #ff66cc, 0 0 15px #ff99cc;
            line-height: 1.2;
        }

        .corazon {
            position: absolute;
            animation: caer linear forwards;
            user-select: none;
            pointer-events: none;
        }

        @keyframes caer {
            0% {
                transform: translateY(-40px) scale(1);
                opacity: 1;
            }
            100% {
                transform: translateY(100vh) scale(0.8);
                opacity: 0;
            }
        }
    </style>
</head>
<body onclick="multiplicarCorazones(event)">
    <div class="frase">Un día como hoy me enamoré de ti,<br>y créeme, nunca me arrepentiré de haberlo hecho❤️19❤️ </div>

    <script>
        const emojis = ['❤️','💖','💕','💘','💗','💞','🩷','🌸'];

        function crearCorazon(event = null) {
            const corazon = document.createElement('div');
            corazon.classList.add('corazon');
            corazon.innerHTML = emojis[Math.floor(Math.random() * emojis.length)];

            const size = Math.random() * 20 + 25;
            corazon.style.fontSize = size + 'px';

            const posX = event ? event.clientX : Math.random() * window.innerWidth;
            corazon.style.left = posX + 'px';
            corazon.style.top = '-30px';

            const duracion = Math.random() * 3 + 2;
            corazon.style.animationDuration = duracion + 's';

            corazon.style.color = ['#ff3366', '#ff6699', '#ff99cc', '#ff66cc'][Math.floor(Math.random() * 4)];

            document.body.appendChild(corazon);

            setTimeout(() => {
                corazon.remove();
            }, duracion * 1000);
        }

        function multiplicarCorazones(event) {
            for (let i = 0; i < 10; i++) {
                setTimeout(() => crearCorazon(event), i * 50);
            }
        }

        setInterval(() => {
            for (let i = 0; i < 3; i++) {
                crearCorazon();
            }
        }, 200);
    </script>
</body>
</html>
"""

# Guardar HTML y abrir en navegador
archivo = "amor_sin_musica.html"
with open(archivo, "w", encoding="utf-8") as f:
    f.write(html)

webbrowser.open(archivo)