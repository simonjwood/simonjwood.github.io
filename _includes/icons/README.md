# Icons

Inline SVG icons used via `{% include icon.html name="..." %}`. They replace the
Font Awesome and Academicons web fonts, so pages no longer download ~225 KB of
icon fonts to show a handful of icons, and only the icons a page uses are sent.

Sources and licences:

- Academicons (arxiv, google-scholar, impactstory, orcid, pubmed, scopus,
  semantic-scholar): glyphs extracted from Academicons 1.9.4 by James Walsh
  and Katja Bercic, https://jpswalsh.github.io/academicons/ — SIL Open Font License 1.1.
- All other icons: Font Awesome Free 6.7.2 by Fonticons, Inc.,
  https://fontawesome.com — icons licensed CC BY 4.0
  (https://fontawesome.com/license/free).

To add a Font Awesome icon, download
`https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.7.2/svgs/<solid|regular|brands>/<name>.svg`,
remove the licence comment, and save it here as `<name>.svg`.
