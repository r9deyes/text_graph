# text_graph

Библиотека и реализация на Python для создания графовой модели представления текста (graph-based model). Представляет текст как граф, где слова являются вершинами, а пары слов следующих друг за другом являются дугами. 

* Для работы библиотеки требуется **Python 2.7** и дополнительный пакет **NetworkX v. 1.11** (только первой версии)
* и пакет **chardet** 
* Для полноценной работы графического интерфейса, также может потребоваться пакет **matplotlib**. (если нужно строить графики распределения частот слов и пар слов)

#### Установить пакеты можно
> pip install networkx==1.11, chardet, matplotlib

Основным файлом библиотеки является ***text_graph.py***. 

Для графического интерфейса использовалась разработка TextStat. Для запуска GUI достаточно запустить ***TextStat.pyw***. 
