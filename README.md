# Обрезка ссылок с помощью Битли

CCProj - маленькая, но крайне полезная утилита, позволяющая быстро получить битлинк вашей ссылки с помощью сервиса Битли или получить количество кликов по вашей уже готовой битлинку


### Как установить

Вам необходимо получить GA токен Bitly на сайте Bitly, после чего создать файл `.env` рядом с main.py и поместить свой токен в переменную `BITLY_GA_TOKEN`:
```
BITLY_GA_TOKEN="d370afd481925fb2a5bd7606ba08cce5408b3524"
```

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```


### Примеры запуска

Запускается скрипт с одним обязательным аргументом - ссылкой.

Если в качестве аргумента при запуске указывается обычная ссылка, скрипт вернет ее битлиинк
```
$ python main.py https://guides.github.com/features/mastering-markdown/
Битлинк:  https://bit.ly/3w8BMqK
```
Если же в качестве аргумента указывается битлинк, скрипт вернет количество кликов по нему
```
$ python main.py  https://bit.ly/3w8BMqK
Кол-во кликов:  1
```



### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).