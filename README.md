## Простой парсинг УРЛов через get запросы на Python. ## 
Тестировалось на Python 2.7.15+ и Python 3.6.8  
Ключ '-u' является обязательным параметром, принемает УРЛы в виде аргументов, может обрабатывать несколько УРЛов, перечислять можно через пробел.  

Если дополнительные опции не указывать, а задать только УРЛ, то должно вернуться 2 вида кодов, односимвольные:  
0 - успех, код ответа 200 от севрера, ошибок нет.  
1 - таймаут на коннект к серверу.  
2 - не верный формат либо не существующий урл (урл должен быть формата http://examle.com, перечесляться УРЛы должны через пробел)<br/>
3 - Неизвестная ошибка.  

Либо трехзначный HTTP код, не равный 200.  

Дополнительные ключи:  
-h подсказка по ключам.  
-e вернет код HTTP ответа от сервера.  
-H вернет информацию по заголовкам.  
-с вернет информацию по кукам.  
-t вернет информацию о времени ушедшем на загрузку страницы.  
-a Возвращает информацию о заголовках, куках, времени загрузки и код ответа.  


