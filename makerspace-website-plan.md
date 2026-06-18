# Makerspace Website Plan — חוויות מייקרס

**Status:** Approved. Implementation not started.
**Last updated:** 2026-06-18

---

## Stack

| Item | Choice | Reason |
|---|---|---|
| Generator | Pelican (Python) | Aligns with Ophir's Python preference; teachable at the makerspace |
| Package manager | uv | Preferred over pip |
| Multilingual | `pelican-i18n-subsites` plugin | One subsite per language |
| Styling | Plain CSS | Readable, no framework lock-in |
| Hosting | GitHub Pages | Free, fits existing git workflow |

Pelican was chosen over Eleventy (JS) — see decision note in `makers-management/M-memory/decisions.md`.

---

## Pages (MVP)

| Page | Hebrew | Notes |
|---|---|---|
| Home | ראשי | Logo placeholder, tagline, location + hours, library sponsor link |
| Activities | פעילויות | Equipment and skills available at the space |
| Past Activities | פעילויות שעברו | Pelican blog — title + date + text + images/video embeds. One placeholder post on build. |
| Contact | צור קשר | WhatsApp links, address, Google Maps embed |

---

## Multilingual

- **Languages:** Hebrew (primary/default), Arabic, English, Russian
- **RTL:** Hebrew, Arabic
- **LTR:** English, Russian
- Language switcher in the header
- Hebrew is the main site; other languages at `/en/`, `/ar/`, `/ru/`
- Browser default: Hebrew

---

## Content Workflow

CREATE workflow produces Hebrew Markdown → file drops into `content/` → Pelican rebuilds the site.

---

## File Structure

```
makers-website/
├── content/
│   ├── pages/          ← Home, Activities, Contact (all 4 languages)
│   ├── posts/          ← Past Activities blog posts (Hebrew primary)
│   ├── en/             ← English translations
│   ├── ar/             ← Arabic translations
│   └── ru/             ← Russian translations
├── themes/
│   └── makers/
│       ├── templates/  ← Jinja2 (base, index, article, page)
│       └── static/
│           ├── css/    ← RTL/LTR switching, layout
│           └── images/ ← logo placeholder
├── pelicanconf.py      ← main config
├── publishconf.py      ← production config
└── requirements.txt
```

---

## Assets Pending

- [ ] Makerspace logo (from Ophir)
- [ ] GitHub account + public repo (for hosting)

## Fixed Links

- Sponsor: https://www.havayot.org.il/%D7%A1%D7%A4%D7%A8%D7%99%D7%95%D7%AA/
