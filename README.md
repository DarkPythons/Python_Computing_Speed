<h1>Скорость вычислений на Python</h1>

<h2>Начало</h2>
<p>Python является медленным языком программирования, по сравнению с другими языками, поэтому любой уважающий себя программист хочет 
увеличить скорость выполнения его кода, или просто повысить скорость вычислений любым способом. Я собрал несколько возможных способов 
сделать увелечение производительности кода. Мы начнем с самого банального и простого способa вычислений, и медленно двигаясь, будем 
продвигаться к более сложным методам (или простым) для того чтобы ускорить выполнение вычислений. Мы возьмем самую лучшую задачу, у 
которой очень большой потенциал увеличения скорости выполнения - "Вычисление чисел Фибоначчи". У каждого на компьютере предложенные 
способы будут работать по разному, но тут они расставлены по времени выполнения на моём компьютере.</p>
<h2>Выполнение</h2>

<h2>Иерархия способов и оценки</h2>

<h3>1. Использование обычной рекурсии</h3>
<p>Использование самого обычного способа вычисления множества чисел при помощи рекурсии.</p>
<p>Все вычисления в этом случае заняли: 140.31 секунд</p>
<p>Путь до кода/директории программы: python_files/1_fibbonachi_recursive.py</p> 
<p>Путь до Jupyter программы: jupyter_files/1_fibbonachi_recursive.ipynb</p> 

<h3>2. Один процесс - одно число фибоначчи</h3>
<p>Использование того же алгоритма рекурсии, но теперь вычисление каждого числа фибоначчи будет 
происходить в одном отдельном процессе, то есть процессов у нас будет столько же, сколько и задач. </p>
<p>Все вычисления в этом случае заняли: 103.90 секунды</p>
<p>Путь до кода/директории программы: python_files/2_fibbonachi_process.py</p>
<p>Jupyter программы: jupyter_files/2_fibbonachi_process.ipynb</p>

<h3>3. Одна очередь - несколько процессов</h3>
<p>Использование очереди задач, но теперь процессов у нас ограниченное количество, то есть каждый 
процесс будет брать задачу (число) из очереди,
делать нужные вычисления и помещать число фибоначчи в общий список результатов.</p>
<p>Все вычисления в этом случае заняли: 91.73 секунд</p>
<p>Путь до кода/директории программы: python_files/3_fibbonachi_one_queues.py</p>
<p>Jupyter программы: jupyter_files/3_fibbonachi_one_queues.ipynb</p>

<h3>4. Две очереди - несколько процессов</h3>
<p>Использование двух очередей, одна отвечает за задачи, которые будут брать процессеы и решать 
(вычислять), другая очередь результатов, куда нужно
будет помещать числа фибоначчи.</p>
<p>Все вычисления в этом случае заняли: 89.24 секунд</p>
<p>Путь до кода/директории программы: python_files/4_fibbonachi_two_queues.py</p>
<p>Jupyter программы: jupyter_files/4_fibbonachi_two_queues.ipynb</p>

<h3>5. Пул процессов для вычислений</h3>
<p>Использование специального класса Pool, который делает создание объекта пула, через который можно 
запустить несколько процессов, и дать этим процессам решать некоторые задачи </p>
<p>Все вычисления в этом случае заняли: 70.81 секунд</p>
<p>Путь до кода/директории программы: python_files/5_fibbonachi_pool.py</p>
<p>Jupyter программы: jupyter_files/5_fibbonachi_pool.ipynb</p>

<h3>6. Вычисления на C</h3>
<p>Использование вместо Python языкa программирования C, то есть мы сделали замену высокоуровневого и интерпритируемого языка на низкоуровневый и компилируемый язык</p>
<p>Все вычисления в этом случае заняли: 6.20 секунд</p>
<p>Путь до кода/директории программы: python_files/6_fibbonachi_c_lang</p>
<p>Jupyter программы: Отдельная директория в python_files</p>

<h3>7. Вычисления на C++</h3>
<p>Использование вместо Python языкa программирования C++, то есть мы сделали замену высокоуровневого и интерпритируемого языка на низкоуровневый и компилируемый язык</p>
<p>Все вычисления в этом случае заняли: 5.36 секунд</p>
<p>Путь до кода/директории программы: python_files/7_fibbonachi_cpp_lang</p>
<p>Jupyter программы: Отдельная директория в python_files</p>

<h3>8. *Логика программы - Python, вычисления - С++</h3>
<p>* - Средняя по сложности реализация</p>
<p>Использование Python для основной логики нашей программы, где мы делали инициализацию процессов которые
делали получение чисел фибоначчи при помощи библиотеки, которая была написана на C++.
</p>
<p>Все вычисления в этом случае заняли: 3.09 секунд</p>
<p>Путь до кода/директории программы: python_files/8_fibbonachi_python_and_cpp</p>
<p>Jupyter программы: Отдельная директория в python_files</p>

<h3>9. Использование кэширования</h3>
<p>Использование кэширования. Так как мы используем рекурсию, у нас будет происходить вызов нашей 
функции множество раз с теми же параметрами, поэтому хорошим решением будет кэширование</p>
<p>Все вычисления в этом случае заняли: 0.0 секунд</p>
<p>Путь до кода/директории программы: python_files/9_fibbonachi_cached.py</p>
<p>Jupyter программы: jupyter_files/9_fibbonachi_cached.ipynb</p>

<h3>10. Метод из динамического программирования</h3>
<p>Использование списка результатов (чисел фибоначчи), где мы брали по индексу предыдущее значение и пред-предыдущее, после чего складывали их, получая новое число фибоначчи</p>
<p>Все вычисления в этом случае заняли: 0.0 секунд</p>
<p>Путь до кода/директории программы: python_files/10_fibbonachi_dinam_prog.py</p>
<p>Jupyter программы: jupyter_files/10_fibbonachi_dinam_prog.ipynb</p>