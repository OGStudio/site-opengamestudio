# Repository Structure

PSKOV static site with localized content. Markdown source → HTML output.

**Site parts** (from `pskov.cfg` input):
- `news` — articles (primary work area)
- `page` — static pages (e.g. about)
- `game` — game descriptions
- `tool` — tool descriptions

**Localized directories**: `{en,ru}/` each contain `news/`, `page/`, `game/`, `tool/`.

**Images**: `images/` directory. Referenced as `../../images/` from markdown files.

**Videos**: `vid/` directory. Referenced as `../../vid/` from markdown files.

# Markdown File Format

Filename: `YYYY-MM-DD_slug.md` or `YYYY-MM_slug.md` (older files use 2-digit months)

Frontmatter (Pelican-style, lines at top):
```
Title: Article Title
Date: YYYY-MM-DD
Category: News
Slug: article-slug
Lang: en
```

Category matches the site part. `Lang` is `en` or `ru`. Slug matches the filename without date prefix and `.md` extension.

# Creating New Stub Pages

When asked to create a new stub page:

1. Find the most recent `.md` file in `en/news/` to determine the current date
2. Increment that date by **one month**
3. Create two files with identical names:
   - `en/news/YYYY-MM_slug.md` (English)
   - `ru/news/YYYY-MM_slug.md` (Russian)
4. Each file must have matching frontmatter (same Title, Date, Slug; different Lang)
5. The slug should match the filename (without date prefix and `.md`)

**Key rules:**
- English and Russian files share the same slug and date
- Date is always the 1st of the month (unless the source file uses a specific day)
- Stub content can be minimal — just a title and a placeholder line
