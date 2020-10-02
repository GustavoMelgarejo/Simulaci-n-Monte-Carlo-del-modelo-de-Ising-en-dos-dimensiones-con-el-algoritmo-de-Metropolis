## Simulación Monte Carlo del modelo de Ising con el algoritmo de Metropolis

El código de la simulación lo puede encontrar en el archivo **Modelo_Ising2D**, dicho programa le permitirá realizar una simulación Monte Carlo del modelo de Ising en dos dimensiones usando el algoritmo de Metropolis, el lenguaje de programación usado fue python. Los resultados que se muestran son los gráficos de energía en función del tiempo de simulación, y de magnetización en función de la temperatura. El código que se usó es una modificación de un programa crado por _PMC Computational Applications_ de la _Universidad Nacional de Colombia_, y se puede consultar en el siguiente enlace: https://pcm-ca.github.io/tutorials/MonteCarloSimulation/.

Las dimensiones de la red simulada son _NXN=16X16_, la temperatura inicial del sistema fue de 0.01K, y estudiamos como este evolucionaba a medida que la temperatutura se incrementaba hasta llegar a un valor de 15K.

Los pasos de Monte Carlo usados para usados para dejar estabilizar el sistema fueron de 1025 al igual que los usados para calcular los promedios.

Con esta especificaciones el programa se tarda al rededor de 30 minutos en arrojar los gráficos, para obtener graficos en menor tiempo, se pueden disminuir las dimensiones de la red y el número de pasos de Monte Carlo.
