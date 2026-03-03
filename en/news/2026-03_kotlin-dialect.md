Title: Kotlin dialect
Date: 2026-03-07
Category: News
Slug: cld-to-kd
Lang: en

![][splash]

# February

I planned on running GitBudget on Desktop with the help of Qt, however,
the rabbit's hole of Kotlin Multiplatform + C++ turned out to be way
deeper than I initially anticipated. I managed to confirm the technical side
of the binding but the result is due to arrive only in March.

While in the rabbit hole I realized the need to turn Cross-language dialect
into Kotlin dialect to have the main focus on Kotlin Multiplatform. That's why
I've created KD based on CLD in Febrary: KD is now a Node.js application (yes,
it's still Kotlin, but no JVM now, Kotlin is transpiled to JS). I've also added
F fields generation.

## March

I plan on finishing KD to make it generate C++ bindings so that GitBudget
is finally available on Desktop with the help of Qt.

[splash]: ../../images/2026-02_cld-to-kd.jpg