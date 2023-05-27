import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox
import numpy as np
import pandas as pd
from sympy import symbols, Poly, latex
from get_data_CPU import get_CPU_Time_use


def obtener_configuraciones():
    """
    Solicita al usuario que ingrese los datos de tiempo de captura y uso de CPU.
    Retorna una tupla con los datos ingresados por el usuario.
    """
    try:
        tiempo_captura = int(input('Introduzca el tiempo total de captura del uso del CPU, sino ENTER: '))
        intervalo_captura = float(input('Introduzca el intervalo de captura del uso del CPU, sino ENTER: '))
        tiempo_captura, uso_CPU = get_CPU_Time_use(tiempo_captura, intervalo_captura)
    except Exception:
        tiempo_captura = 2
        intervalo_captura = 0.2
        intervalo_captura, uso_CPU = get_CPU_Time_use(tiempo_captura, intervalo_captura)
    return tiempo_captura, uso_CPU


def obtener_datos_manuales():
    """
    Solicita al usuario que ingrese las listas de tiempo_captura y uso_CPU manualmente.
    Retorna las listas ingresadas por el usuario.
    """
    try:
        tiempo_captura = input('Introduzca la lista de tiempo_captura separada por espacios: ').split()
        uso_CPU = input('Introduzca la lista de uso_CPU separada por espacios: ').split()
        tiempo_captura = list(map(float, tiempo_captura))
        uso_CPU = list(map(float, uso_CPU))
    except Exception:
        tiempo_captura = [1, 2, 3, 4, 5]
        uso_CPU = [10, 20, 15, 25, 30]
    return tiempo_captura, uso_CPU


def obtener_tabla_de_diferencias(X, Y):
    """
    Obtenga la tabla de diferencias
    """
    n = len(X)
    A = np.zeros([n, n])

    for i in range(n):
        A[i][0] = Y[i]

    for j in range(1, n):
        for i in range(j, n):
            A[i][j] = (A[i][j-1] - A[i-1][j-1]) / (X[i] - X[i-j])

    return A


def calcular_interpolacion_puntos(X, Y, x):
    """
    Calcular la interpolación en x puntos
    """
    n = len(X)
    temp = np.zeros((n, n))
    temp[:, 0] = Y

    for j in range(1, n):
        for i in range(j, n):
            temp[i, j] = (temp[i, j-1] - temp[i-1, j-1]) / (X[i] - X[i-j])

    sum = temp[0, 0]
    temp_sum = 1.0

    for i in range(1, n):
        temp_sum *= (x - X[i-1])
        sum += temp_sum * temp[i, i]

    return sum


def interpolacion_newton():
    configuracion = input('¿Desea ingresar la lista de tiempo_captura y uso_CPU manualmente? (s/n): ')
    if configuracion.lower() == 's':
        tiempo_captura, uso_CPU = obtener_datos_manuales()
    else:
        tiempo_captura, uso_CPU = obtener_configuraciones()

    tiempo_interpolado = [None]
    valor_interpolado = [None]

    A = obtener_tabla_de_diferencias(tiempo_captura, uso_CPU)
    df = pd.DataFrame(A)
    df = df.applymap(lambda x: f'{x:.4f}')  # Aproximar valores a 4 decimales

    x = symbols('x')
    polynomial_coeffs = np.flip(A[-1, :])
    polynomial = Poly(polynomial_coeffs, x)
    polynomial_str = latex(polynomial.as_expr())

    xs = np.linspace(np.min(tiempo_captura), np.max(tiempo_captura), 1000)
    ys = [calcular_interpolacion_puntos(tiempo_captura, uso_CPU, x) for x in xs]

    fig, ax = plt.subplots(figsize=(12, 6))
    fig.canvas.manager.full_screen_toggle()

    views = ['graph', 'table', 'polynomial']
    current_view_index = 0

    def update_view():
        ax.clear()
        if views[current_view_index] == 'graph':
            ax.plot(tiempo_captura, uso_CPU, 's', label="valores originales")
            ax.plot(xs, ys, 'r', label='valores de interpolación')
            ax.set_title("Uso de CPU por unidad de tiempo")
            ax.set_xlabel('Tiempo (S)')
            ax.set_ylabel('Porcentaje de uso de CPU (%)')
            ax.legend(loc='best')
            if tiempo_interpolado[0] is not None:
                ax.plot(tiempo_interpolado[0], valor_interpolado[0], 'bo', markersize=8, label='valor interpolado')
                ax.annotate(f'Tiempo: {tiempo_interpolado[0]}\nValor interpolado: {valor_interpolado[0]}',
                            (tiempo_interpolado[0], valor_interpolado[0]), textcoords='offset points', xytext=(0, 10),
                            ha='center', fontsize=10, color='b')
        elif views[current_view_index] == 'table':
            ax.axis('off')
            ax.table(cellText=df.values, colLabels=df.columns, loc='center')
        elif views[current_view_index] == 'polynomial':
            ax.axis('off')
            ax.text(0.5, 0.5, f'$P(x) = {polynomial_str}$', fontsize=12, ha='center', va='center')

        fig.canvas.draw()

    def on_submit(text):
        try:
            tiempo = float(text)
            valor_interpolado[0] = calcular_interpolacion_puntos(tiempo_captura, uso_CPU, tiempo)
            tiempo_interpolado[0] = tiempo
            update_view()
        except ValueError:
            print('Error: Ingrese un valor numérico válido para el tiempo.')

    def on_key_press(event):
        nonlocal current_view_index
        if event.key == 'right':
            current_view_index = (current_view_index + 1) % 3
        elif event.key == 'left':
            current_view_index = (current_view_index - 1) % 3
        update_view()

    fig.canvas.mpl_connect('key_press_event', on_key_press)
    update_view()

    axbox = plt.axes([0.2, 0.9, 0.2, 0.05])
    text_box = TextBox(axbox, 'Tiempo:')
    text_box.on_submit(on_submit)

    plt.show()


interpolacion_newton()
