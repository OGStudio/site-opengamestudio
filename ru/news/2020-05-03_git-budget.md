Title: Почему я сделал личный проект учёта трат на Git+JS
Date: 2020-05-03 00:00
Category: News
Slug: git-budget
Lang: ru

![ГитБюджет][снимок]

В этой статье Михаил поделится опытом использования Git+JS.

Здравствуйте, господа, в этой статье я поделюсь опытом создания приложения учёта трат, в частности отвечу на следующие вопросы:

1. Зачем мне приложение учёта трат?
1. Почему это личный проект?
1. Почему проект на Git+JS?

**1. Зачем мне приложение учёта трат?**

Как и многие другие люди я давно хотел стать богатым и практиковать [успешный успех][успех]. Одной из рекомендаций в таких случаях часто выступает предложение вести собственный бюджет, чем я и занялся несколько лет назад. Скажу сразу, что ведение бюджета не сделало меня богатым и успешным, а своё материальное положение я улучшил обычным переездом в Москву.

Вести бюджет я начал, если не изменяет память, где-то в 2012-м году. В то время у меня уже была профессиональная деформация программиста, выражающаяся формулой "сделано не мной" и попыткой написать всё самому. Тем не менее, по неопытности я решил начать с "проверенных" решений и приобрёл [YNAB][ynab] (You Need A Budget), т.к. приложение позволяло работать и с ПК, и с телефона.

Я честно пытался задавать план трат на месяц и укладываться в него года три. Однако, где-то в 2015-м году авторы выпустили новую версию приложения, за которую **опять хотели денег**, старую же версию эти недальновидные капиталисты выкинули на обочину истории. В итоге мне пришлось выбирать из двух вариантов:

1. Заплатить за новую версию и пользоваться "совершенно новым" приложением с другим интерфейсом.
1. Послать их нафиг, сохранить деньги, но потерять текущую историю трат.

Я рассудил, что:

1. приложение уже оплачивал;
1. старая версия меня устраивала;
1. новую версия я не просил;
1. если бы они мне до покупки сказали, что будут каждый раз драть с меня деньги, я бы им не заплатил и первый раз;
1. спонсировать такое хамство я не буду;

и выбрал второй вариант: послал их нафиг и **потерял историю трат**.

Эта ситуация меня довольно сильно разочаровала, поэтому я забросил ведение бюджета где-то на год. Однако, в один из дней "болезненной синхронизации" (также известной как "выяснение отношений") я **не смог отбить финансовый наброс** вида "ты транжира, вечно тратишь деньги на ерунду", после чего ясно осознал важность учёта трат.

В этот раз я решил не повторять ошибку и не отдавать свои данные неизвестно куда с потенциальной возможностью их потерять, поэтому начал вести учёт трат в самых обычных заметках телефона. Формат был довольно простым и выглядел следующим образом:

![Заметки][снимок-заметки]

Заметки продержались у меня до середины 2018-го, пока я всё-таки не захотел иметь возможность **работать с тратами на ПК**, чтобы анализировать их. Я решил поискать решение, которое позволит мне **бесплатно работать** с историей трат и на ПК, и на телефоне. Таким решением оказался обычный календарь:

![Календарь][снимок-календарь-день]

![Новая запись][снимок-календарь-запись]

В календаре я использовал учётку Google, чтобы иметь доступ к [Apps Script][apps-script] (фактически JavaScript) для анализа записей. Делать скрипты оказалось не очень удобно, т.к. формат хранения календарных записей мало подходит для трат. Вопрос владения данными также оставался нерешённым: мои данные опять пылились на неизвестном и неподконтрольном мне сервере, а доступ к ним был лишь через неподконтрольный мне и **изменяющийся по чужой прихоти** API.

Во время использования календаря меня периодически посещали две мысли:

1. как здорово было бы все свои данные хранить в Git, чтобы легко анализировать траты;
1. как здорово было бы использовать интерфейс без всего лишнего, чтобы ускорить запись трат.

Осенью 2019-го я наткнулся на проект [Isomorphic-Git][isomorphic-git], позволяющий работать с Git из JavaScript, бегло проверил его работоспособность и понял, что нашёл свой Святой Грааль. Недавно я завершил создание первой версии приложения ГитБюджет, функциональность которого можно увидеть в следующем видео: 

<iframe width="720" height="405" src="https://www.youtube.com/embed/ii_cLXAy3S0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

В итоге, сейчас учёт трат на телефоне у меня выглядит следующим образом:

![ГитБюджет][снимок-гит-бюджет]

Данные в Git выглядят cледующим образом: [https://gitlab.com/kornerr/git-budget-sample-data/-/blob/me/gb.log](https://gitlab.com/kornerr/git-budget-sample-data/-/blob/me/gb.log)

Отмечу некоторые важные моменты:

* по ссылке представлено хранилище Git, отражающее действия из видео;
* свои траты я храню в отдельном закрытом хранилище, так следует делать каждому;
* приложение работает полностью на устройстве и не имеет сервера: используется хостинг GitHub Pages;
* приложение общается с внешним миром лишь в момент синхронизации с Git;
* пароль хранит браузер, приложение использует его лишь в момент синхронизации с Git;
* приложение необходимо загружать по HTTP, т.к. используемая  версия Isomorphic-Git (0.70.0) некоторые запросы (метаданные) к Git выполняет по HTTP, а браузеры нынче запрещают обращения к HTTP из HTTPS.

**2. Почему это личный проект?**

На ГитБюджет я потратил 40 часов своей жизни в течение первого квартала 2020-го, т.е. в среднем каждый день я тратил около получаса.

Личный проект обладает следующими преимуществами по сравнению с рабочим:

1. Можно делать всё, что угодно, и учиться на своих ошибках.
1. Никто не стоит над душой и не ограничивает фантазию.
1. Предыдущие два пункта дают душевный покой и возможность совершенно спокойно принимать и исполнять самые идиотские решения на работе.
1. Шишки, набитые в личном проекте, колоссально расширяют кругозор.

У личного проекта также есть и недостатки:

1. На твой проект пофиг всем в мире, кроме тебя.
1. Никто не даст тебе ни гроша.
1. Нужно умудряться выкраивать время на личный проект каждый день.
1. Жена не скажет тебе "спасибо", даже если сама потом будет использовать приложение.

Легко заметить, что все недостатки личного проекта перекрываются преимуществами рабочего проекта. А все недостатки рабочего проекта перекрываются преимуществами личного проекта. Инь и янь.

**3. Почему проект на Git+JS?**

Хранение данных в Git вместо неизвестного сервера/API даёт следующие преимущества:

1. Git является самым распространённым решением для децентрализованного хранения проектов среди разработчиков, т.е. практически каждый разработчик умеет работать с Git.
1. Для работы с Git не нужен очередной API: вы просто работаете с файлами.
1. Есть много сервисов, предоставляющих хранилище Git бесплатно, если вы не помешаны на безопасности или не хотите платить денег за сервис.
1. Владелец сервиса Git, конечно, может через несколько лет [быть выкуплен крупной корпорацией][поглощение], однако, вы легко сможете перенести свои данные Git.
1. Для максимальной безопасности данных вы всегда можете поднять свой Git.

Использование JS с HTML/CSS вместо Swift/Kotlin/C#/Python даёт следующие преимущества:

1. Ваше приложение будет работать и на телефоне, и на планшете, и на ПК.
1. Вам не нужно проходить никаких проверок вроде AppStore, для того чтобы попасть в каждое устройство.
1. Ввиду того, что стандарты HTML/CSS/JS согласуются огромным количеством компаний, ни одна из компаний не может [в одностороннем порядке прекратить поддерживать какую-либо технологию][opengl] или [в очередной раз поменять API][swift], так что обратная совместимость может достигать [20 лет][долговечные-приложения] и больше.
1. Ввиду отсутствия сервера вся логика размещается в JS, исполняемый на клиенте, что даёт возможность сохранить ту версию приложения, которая устраивает лично вас, и забыть про обновления, зачастую [приводящие лишь к увеличению тормозов][обновления].

ГитБюджет является лишь первым испытанием возможностей Git+JS. Посмотрим, что удастся сделать ещё.

[снимок]: ../../images/2020-05-06_гит-бюджет_снимок.png

[снимок-заметки]: ../../images/2020-05-06_гит-бюджет_заметки.png
[снимок-календарь-день]: ../../images/2020-05-06_гит-бюджет_календарь-день.png
[снимок-календарь-запись]: ../../images/2020-05-06_гит-бюджет_календарь-запись.png
[снимок-гит-бюджет]: ../../images/2020-05-06_гит-бюджет.png

[успех]: https://успешный-успех.рф
[ynab]: https://www.youneedabudget.com
[apps-script]: https://developers.google.com/apps-script?hl=ru
[isomorphic-git]: https://isomorphic-git.org/
[поглощение]: https://habr.com/ru/post/413215/
[opengl]: https://habr.com/ru/post/413335/
[swift]: https://arm1.ru/blog/pro-perehod-na-swift-3-i-swift-2-4
[долговечные-приложения]: on-the-way-to-durable-applications.html
[обновления]: https://pikabu.ru/story/android_skoree_vsego_stanet_platnyim_6052457?cid=118211967
