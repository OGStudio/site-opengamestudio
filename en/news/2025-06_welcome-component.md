Title: PSKOV 2 editor and components
Date: 2025-06-10 00:00
Category: News
Slug: welcome-component
Lang: en

<video controls width="700">
    <source src="../../images/2025-06_welcome-component.mp4" type="video/mp4"/>
</video>

# PSKOV 2 editor draft

In May I created PSKOV 2 editor draft which is only capable of:

1. display two left menu items
2. display contents in the right for the selected menu item

You probably can't see anything substantial in this, however, the listed
functionality is run by a component. In this case it's called [WelcomeComponent][wcmp].
Future functionality like Git and Markdown is expected to follow the same pattern of
components.

The structure of components is not yet stable, but here's a short excerpt of
the constructor of `WelcomeComponent` just so you can feel the mood:

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

# June

In June I plan to create a draft version of Git component.

[wcmp]: https://github.com/kornerr/pskov2/blob/main/welcome.js
