# Используем образ LaTeX, который уже содержит необходимые зависимости
FROM blang/latex:ubuntu

# Установка зависимостей LaTeX
RUN apt-get update && apt-get install -y \
    texlive-latex-base \
    texlive-fonts-recommended \
    texlive-fonts-extra \
    texlive-latex-extra \
    python3 && \
    python3-pip && \
    
# Копируем все файлы из текущего каталога в /usr/src/app внутри контейнера
COPY . /usr/src/app

# Устанавливаем рабочую директорию
WORKDIR /usr/src/app

# Запускаем код для генерации .tex файла
RUN python latex_test.py

# Генерируем PDF из .tex файла
RUN pdflatex output.tex

# Экспортируем PDF из контейнера в хост-систему
CMD ["cp", "output.pdf", "/usr/src/app/output.pdf"]