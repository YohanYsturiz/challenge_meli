# Desafio Teorico

1. Procesos o Hilos
    - Cuando usar Procesos
        -R= Cuando se necesita utilizar al maximo los procesadores en una maquina determinada para ejecutar una tarea, ejm: para procesar un gran numero de datos sin esperar por I/O se puede derivar en varios procesos si tenemos N cores disponibles.

    - Cuando usar Hilos o Threads
        -R= Cuando se necesitan ejecutar tareas no tan pesadas y si se hace mucho de data compartida entre hilos entonces es conveniente usar Threads, tambien los puedo implementar parar enviar correos y dar un rapida respuesta mientas se ejecutan todos los hilos.
    
    - Cuando usar corrutinas
        -R= Cuando necesite llamar desde una funcion a otra funcion y esperar el resultado de la misma para continuar con la funcion principal no es paralelismo pero su control es mas optimo.

2. 1000.000 de registros
    - Por lo que he investigado la mejor forma de procesar esa cantidad de registros ya que se debe enviar una peticion por cada uno de ellos, seria usando async o corrutinas + Multiprocessing es un poco mas complejo pero es mas optimo. 

    Un proceso por cada core que mas async puede tener un mejor rendimiento. 

3. Dados 4 algoritmos A, B, C y D que cumplen la misma funcionalidad, con complejidades O(n2), O(n3), O(2n) y O(n log n), respectivamente, ¿Cuál de los algoritmos favorecerías y cuál descartarías en principio? Explicar por qué.
    - 3.1 R= Trabajaria con el algoritmo con menos complijidad algoritmica es decir O(n log n) y al que descartaria de inicio es el O(2n) debido a que tiene mas complejidad algoritmica y por lo tanto no es tan optimo.

    - 3.2 R = Usuario la llamada AlfaDB para en caso de que este trabajando en un algoritmo de busqueda ya su complejidad es 0(1) y usuaria la llamada BetaDB en casos donde necesite almacenar mucha informacion de forma concurrente