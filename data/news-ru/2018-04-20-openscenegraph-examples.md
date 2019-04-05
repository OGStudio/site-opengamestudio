Title: Кросс-платформенные примеры OpenSceneGraph
Date: 2018-04-20 00:00
Category: News
Slug: openscenegraph-examples
Lang: ru

![Screenshot][screenshot]

Эта статья резюмирует создание первых двух кросс-платформенных примеров OpenSceneGraph.

К тому времени, как мы выпустили [первую техническую демонстрацию OGS Mahjong 2][tech-demo-1], нас уже дожидался [запрос на описание работы с изображениями][android-image-issue] в OpenSceneGraph на Android. Сначала мы рассматривали возможность создания нового самоучителя для [кросс-платформенного руководства OpenSceneGraph][osgcpg], но позже мы оценили необходимые трудозатраты и посчитали их излишними для освещения такой небольшой темы (по сравнению с тем, что умеет средняя игра) как загрузка изображений. Мы решили продолжить делиться нашими знаниями в виде конкретных примеров. Так на свет появились [кросс-платформенные примеры OpenSceneGraph][osgcpe].

Каждый пример:

* объясняет критически важный код для выполнения поставленной задачи
* акцентирует внимание на нюансах, специфичных для каждой платформы
* предоставляет реализации примера для десктопа, мобилок и веба
* предоставляет сборку для веба, чтобы упростить оценку результата

Первая пара примеров освещает следующие темы:

* Встраивание ресурсов в исполняемый файл: значительное упрощение работы с ресурсами на всех платформах
* Использование изображений PNG с помощью плагинов PNG: описание требований, необходимых для сборки и использования плагинов PNG

Мы будем и впредь добавлять новые примеры по мере продвижения нашей разработки OGS Mahjong 2.

На этом мы заканчиваем резюме о создании первых двух кросс-платформенных примеров OpenSceneGraph.


[screenshot]: ../../images/2018-04-20-openscenegraph-examples.png

[tech-demo-1]: mahjong-techdemo1-gameplay.html
[android-image-issue]: https://github.com/OGStudio/openscenegraph-cross-platform-guide/issues/4
[osgcpg]: https://github.com/OGStudio/openscenegraph-cross-platform-guide
[osgcpe]: https://github.com/OGStudio/openscenegraph-cross-platform-examples
