// Helpers for building the research paper with docx-js.
// Light inline markup supported: [label](url) hyperlinks, **bold**, *italic*.
const {
  Paragraph, TextRun, ExternalHyperlink, HeadingLevel, AlignmentType, Table, TableRow, TableCell,
  WidthType, ShadingType, PageBreak,
} = require('docx');

const FONT = 'Georgia';
const FONT_SANS = 'Arial';
const LINK = '1F4E79';

function runsFromMarkup(s, base = {}) {
  const out = [];
  const re = /\[([^\]]+)\]\((https?:\/\/[^\s)]+)\)|\*\*([^*]+)\*\*|\*([^*]+)\*/g;
  const size = base.size || 22;
  const font = base.font || FONT;
  let last = 0, m;
  while ((m = re.exec(s)) !== null) {
    if (m.index > last) out.push(new TextRun({ ...base, text: s.slice(last, m.index), font, size }));
    if (m[1]) {
      out.push(new ExternalHyperlink({
        link: m[2],
        children: [new TextRun({ ...base, text: m[1], font, size, color: LINK, underline: {} })],
      }));
    } else if (m[3]) {
      out.push(new TextRun({ ...base, text: m[3], font, size, bold: true }));
    } else if (m[4]) {
      out.push(new TextRun({ ...base, text: m[4], font, size, italics: true }));
    }
    last = re.lastIndex;
  }
  if (last < s.length) out.push(new TextRun({ ...base, text: s.slice(last), font, size }));
  return out;
}

const p = (s, opts = {}) => new Paragraph({
  children: runsFromMarkup(s, opts.run || {}),
  spacing: { after: 160, line: 300 },
  alignment: opts.align || AlignmentType.JUSTIFIED,
  ...(opts.para || {}),
});

const h1 = (s) => new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun({ text: s })], spacing: { before: 360, after: 160 } });
const h2 = (s) => new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun({ text: s })], spacing: { before: 280, after: 120 } });
const h3 = (s) => new Paragraph({ heading: HeadingLevel.HEADING_3, children: [new TextRun({ text: s })], spacing: { before: 200, after: 100 } });

const bullet = (s) => new Paragraph({ children: runsFromMarkup(s), numbering: { reference: 'bullets', level: 0 }, spacing: { after: 100, line: 280 } });
const numbered = (s) => new Paragraph({ children: runsFromMarkup(s), numbering: { reference: 'numbers', level: 0 }, spacing: { after: 100, line: 280 } });

const pageBreak = () => new Paragraph({ children: [new PageBreak()] });

function table(header, rows, widths) {
  const total = widths.reduce((a, b) => a + b, 0);
  const cell = (txt, isHead, w) => new TableCell({
    width: { size: w, type: WidthType.DXA },
    shading: isHead ? { type: ShadingType.CLEAR, fill: 'E7ECF3', color: 'auto' } : undefined,
    margins: { top: 60, bottom: 60, left: 80, right: 80 },
    children: [new Paragraph({
      children: runsFromMarkup(txt, { size: 18, bold: isHead, font: FONT_SANS }),
      spacing: { after: 0, line: 240 },
    })],
  });
  return new Table({
    width: { size: total, type: WidthType.DXA },
    columnWidths: widths,
    rows: [
      new TableRow({ tableHeader: true, children: header.map((h, i) => cell(h, true, widths[i])) }),
      ...rows.map(r => new TableRow({ children: r.map((c, i) => cell(c, false, widths[i])) })),
    ],
  });
}

const caption = (s) => new Paragraph({ children: [new TextRun({ text: s, font: FONT_SANS, size: 18, italics: true })], spacing: { before: 80, after: 200 }, alignment: AlignmentType.LEFT });

module.exports = { runsFromMarkup, p, h1, h2, h3, bullet, numbered, pageBreak, table, caption, FONT, FONT_SANS };
