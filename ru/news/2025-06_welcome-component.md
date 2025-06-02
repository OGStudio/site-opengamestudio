Title: Редактор ПСКОВ 2 и компоненты
Date: 2025-06-10 00:00
Category: News
Slug: welcome-component
Lang: ru

<video controls width="700">
    <source src="../../images/2025-06_welcome-component.mp4" type="video/mp4"/>
</video>

# Заготовка редактора ПСКОВ 2

В мае сделал заготовку редктора ПСКОВ 2, которая умеет лишь:

1. показывать два пункта в левом меню
2. отображать содержимое выбранного пункта меню

Функционально в этом сложно увидеть что-либо занимательно. Но
таковое есть: и левое меню, и содержимое управляется так компонентом,
в данном случае он называется [WelcomeComponent][wcmp]. Функциональность
как Git, так и Markdown по задуме тоже будет будет представлена компонентами.

Структура компонента ещё не устоялась, но для примерного понимания приведу
текущий вид конструктора `WelcomeComponent`:

```javascript
function WelcomeComponent() {
    this._construct = function() {
        this.ctrl = new CLDController(new WelcomeContext());
        // Dbg.
        this.ctrl.registerCallback((c) => {
            console.log(`ИГР WelcomeC._construct ctrl key/value: '${c.recentField}'/'${c.field(c.recentField)}'`);
        });
        this.setupHTML();
        this.setupEffects();
        this.setupEvents();
        this.setupShoulds();
    };
	- - - -
```

# Июнь

В июне планирую сделать заготовку компонента Git со своей частью
левого меню и содержимого справа.

[wcmp]: https://github.com/kornerr/pskov2/blob/main/welcome.js
