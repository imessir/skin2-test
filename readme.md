# Список тест-кейсов

### Проверка содержимого страницы
**Шаги**
1. Открыть вебсайт по [ссылке](https://opm-website.iot-asm-test1.insitech.live/)

**Результат**
- Вебсайт содержит необходимые элементы и соответствует макету

### Выпадающий список в поиске содержит результаты поиска
**Шаги**
1. На основной странице в строке поиска Найти ввести значение "1"

**Результат**
- Появляется индикатор загрузки
- В течение секунды индикатор загрузки сменяется выпадающим списком из смартфонов, планшетов и магазинов
- Список соответствует данным, пришедшим в запросе /api/search?text=1

### Переход на смартфон из списка поиска
**Шаги**
1. На основной странице в строке поиска Найти ввести значение "1"
2. Кликнуть на любой из смартфонов в появившемся выпадающем списке

**Результат**
- Открывается страница выбранного смартфона
- 
### Проверка скролла карусели
**Шаги**
1. На основной странице в карусели последовательно прокликать кнопки влево и вправо не менее 8 раз каждую

**Результат**
- Картинки в карусели плавно сменяют друг друга по кругу
- Все 7 картинок соответствуют макетам

### Колокольчик уведомлений для незалогиненного пользователя
**Шаги**
1. Зайти на основную страницу незалогиненным пользователем
2. Кликнуть на колокольчик Уведомления

**Результат**
- Появляется попап Новых уведомлений нет
