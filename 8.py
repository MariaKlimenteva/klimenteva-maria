import matplotlib.pyplot as plt # импортируем библитеки
import numpy as np

def read_settings(f_name): # функция чтения данных из файла и возврачения их в нужном типе
    with open(f_name, 'r') as settings_f:
        return [float(i) for i in settings_f.read().split('\n')]
    

voltstep, period = read_settings("settings.txt")

data_ar = np.loadtxt("data.txt", dtype = float) # чтение данных из файла и запись их в массив
data_ar = data_ar * voltstep # приводим массив данных к нужной величине
dur_time = len(data_ar) * period # полное время эксперимента

t = np.linspace(0, dur_time, len(data_ar))# создаем массив данных времени с нужным шагом параметры - начало, конец интервала
print(len(t), len(data_ar))

charge_time = np.argmax(data_ar) * period # время зарядки конденсатора
discharge_time = dur_time - charge_time # время разрядки конденсатора
max_volt = 3.5


fig, ax = plt.subplots(figsize = (15, 10), dpi = 200) # создаем пространство для графика
ax.plot(t, data_ar, marker = "o", markersize = 5, markevery = 100, markerfacecolor = "red", label = 'V(t)', color = 'blue') # устанавливаем основные параметры графика

ax.set_title('Зависимость напряжения на конденсаторе от времени по мере его зарядки и разрядки', fontsize = 17, wrap = True)
ax.set_xlabel('Время, с') 
ax.set_ylabel('Напряжение, В')

ax.set_xlim(0, round(dur_time))
ax.set_ylim(0, max_volt)

ax.text(60, 2.34, 'Время зарядки: {:.2f} c'.format(charge_time), bbox = dict(facecolor = 'red', alpha = 0.5)) # добавляем данные о времени зарядки и разрядки конденсатора, указываем им позицию и их размер, цвет
ax.text(60, 2, 'Время разрядки: {:.2f} c'.format(discharge_time), bbox = dict(facecolor = 'red', alpha = 0.5))

ax.minorticks_on() # включаем метки
ax.grid(which = 'major', linewidth = 2) # делаем основные и второстепенные линии сетки, устанавливаем ширину линий
ax.grid(which = 'minor', linestyle = ':') # пунктирные линии

ax.legend()

fig.savefig('graph.svg')
plt.show()