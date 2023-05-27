import psutil
import time


def get_CPU_Time_use(tiempo_captura, intervalo_captura) -> list:

    '''Devuelve el tiempo de captura (por defecto 10 seg en inmtervalos de 1 s) y el uso porcentual de CPU'''
    time_list = []
    cpu_percent_list = []
    start_time = time.monotonic()

    while time.monotonic() - start_time <= tiempo_captura:
        cpu_percent = psutil.cpu_percent()

        elapsed_time = round(time.monotonic() - start_time, 4)

        time_list.append(elapsed_time)
        cpu_percent_list.append(cpu_percent)

        time.sleep(intervalo_captura)

    return time_list, cpu_percent_list
