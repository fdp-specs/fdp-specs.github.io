# Generates images/FDPmetadatadiagram.svg: FDP metadata model on DCAT 3.
W, H = 1580, 1080
HEAD, LINE, FS = 34, 20, 13
CY = dict(fill="#cdf3f9", stroke="#78b6c3")   # DCAT / standard vocabularies
GR = dict(fill="#c9f5c3", stroke="#7cbd76")   # FDP ontology
TXT = "#174f7c"
out = []
def esc(s): return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
boxes = {}
def box(name, x, y, w, attrs, style, italic=False):
    h = HEAD + (LINE*len(attrs) if attrs else 26)
    boxes[name] = (x, y, w, h)
    out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{style["fill"]}" stroke="{style["stroke"]}" stroke-width="1.5"/>')
    out.append(f'<line x1="{x}" y1="{y+HEAD}" x2="{x+w}" y2="{y+HEAD}" stroke="{style["stroke"]}" stroke-width="1.5"/>')
    fs = ' font-style="italic"' if italic else ''
    out.append(f'<text x="{x+w/2}" y="{y+23}" text-anchor="middle" font-size="14" font-weight="bold" fill="{TXT}"{fs}>{esc(name)}</text>')
    for i, a in enumerate(attrs):
        out.append(f'<text x="{x+10}" y="{y+HEAD+15+i*LINE}" font-size="{FS}" fill="{TXT}">{esc(a)}</text>')
def edge(pts, label=None, lpos=None, kind="assoc", card=None, cpos=None, anchor="start"):
    d = " ".join(f"{x},{y}" for x, y in pts)
    dash = ' stroke-dasharray="7 5"' if kind == "dashed" else ''
    marker = '' if kind == "dashed" else (' marker-end="url(#sub)"' if kind == "sub" else ' marker-end="url(#arr)"')
    out.append(f'<polyline points="{d}" fill="none" stroke="#333" stroke-width="1.4"{dash}{marker}/>')
    if label:
        x, y = lpos
        for j, ln in enumerate(label.split("\n")):
            out.append(f'<text x="{x}" y="{y+j*15}" font-size="{FS}" fill="#222" text-anchor="{anchor}">{esc(ln)}</text>')
    if card:
        x, y = cpos
        out.append(f'<text x="{x}" y="{y}" font-size="{FS}" fill="#222">{esc(card)}</text>')

# ---- classes
res_attrs = ["dcat:contactPoint","dcat:keyword","dcat:landingPage","dcat:theme","dcat:hasVersion","dcat:version",
 "dcat:versionNotes","dcat:hasCurrentVersion","dcat:previousVersion","dcat:qualifiedRelation","dcterms:accessRights",
 "dcterms:conformsTo","dcterms:creator","dcterms:description","dcterms:identifier","dcterms:isReferencedBy",
 "dcterms:issued","dcterms:language","dcterms:license","dcterms:modified","dcterms:publisher","dcterms:relation",
 "dcterms:rights","dcterms:title","dcterms:type","odrl:hasPolicy","prov:qualifiedAttribution"]
box("dcat:Resource", 900, 100, 260, res_attrs, CY, italic=True)
box("foaf:Agent", 560, 60, 200, [], CY)
box("skos:Concept", 600, 145, 160, [], CY)
box("skos:ConceptScheme", 300, 145, 200, [], CY)
box("vcard:Kind", 1290, 145, 190, [], CY)
box("dcat:Relationship", 1300, 330, 220, ["dcat:hadRole"], CY)
box("dcat:Catalog", 60, 330, 260, ["foaf:homepage","dcat:catalog","dcat:service","dcat:resource"], CY)
box("dcat:Dataset", 480, 380, 290, ["dcat:spatialResolutionInMeters","dcat:temporalResolution","dcterms:accrualPeriodicity","dcterms:spatial","dcterms:temporal","prov:wasGeneratedBy"], CY)
box("dcat:DatasetSeries", 560, 580, 210, [], CY)
box("dcat:Distribution", 480, 720, 290, ["dcat:accessURL","dcat:downloadURL","dcat:byteSize","dcat:mediaType","dcterms:format","dcat:compressFormat","dcat:packageFormat","dcterms:title","dcterms:description","dcterms:license","dcterms:issued","dcterms:modified","dcterms:conformsTo"], CY)
box("dcat:DataService", 900, 760, 220, ["dcat:endpointURL","dcat:endpointDescription"], CY)
box("dcat:CatalogRecord", 60, 470, 260, ["dcterms:title","dcterms:description","dcterms:issued","dcterms:modified","dcterms:conformsTo"], CY)
box("fdp-o:FAIRDataPoint", 1240, 560, 250, ["fdp-o:startDate","fdp-o:endDate","fdp-o:uiLanguage","fdp-o:hasSoftwareVersion","fdp-o:conformsToFdpSpec"], GR)
box("fdp-o:MetadataService", 1240, 780, 250, [], GR)
box("fdp-o:MetadataRecord", 60, 880, 260, ["dcterms:issued","dcterms:modified","dcterms:conformsTo","dcterms:creator"], GR)

# ---- edges (Resource spans y 100..674, x 900..1160)
edge([(1030,100),(1030,40),(660,40),(660,60)], "dcterms:publisher", (700,32))
edge([(900,118),(760,118)], "dcterms:creator", (775,112))
edge([(900,175),(760,175)], "dcat:theme", (790,168), card="0..*", cpos=(770,190))
edge([(600,175),(500,175)], "skos:inScheme", (505,168))
edge([(1160,175),(1290,175)], "dcat:contactPoint", (1165,168), card="0..*", cpos=(1170,190))
edge([(1160,360),(1300,360)], "dcat:qualifiedRelation", (1163,378))
edge([(1410,330),(1410,300),(1160,300)], "dcterms:relation", (1175,293))
edge([(310,330),(310,205)], "dcat:themeTaxonomy", (318,270), card="1", cpos=(318,222))
edge([(150,330),(150,240),(900,240)], "dcterms:hasPart", (760,233), card="0..*", cpos=(870,256))
edge([(250,330),(250,290),(600,290),(600,380)], "dcat:dataset", (510,283), card="0..*", cpos=(608,372))
edge([(320,400),(480,400)], "rdfs:subClassOf", (340,393), kind="sub")
edge([(770,400),(900,400)], "rdfs:subClassOf", (780,393), kind="sub")
edge([(190,444),(190,470)], "dcat:record", (198,462), card="0..*", cpos=(150,462))
edge([(620,580),(620,534)], "rdfs:subClassOf", (612,565), kind="sub", anchor="end")
edge([(720,534),(720,580)], "dcat:inSeries", (712,565), card="0..*", cpos=(726,572), anchor="end")
edge([(515,534),(515,720)], "dcat:distribution", (410,630), card="0..*", cpos=(470,645))
edge([(770,800),(900,800)], "dcat:accessService", (776,793), card="0..*", cpos=(860,815))
edge([(950,760),(950,688),(800,688),(800,520),(770,520)], "dcat:servesDataset", (808,682), card="0..*", cpos=(808,610))
edge([(1010,760),(1010,674)], "rdfs:subClassOf", (1018,722), kind="sub")
edge([(1240,810),(1120,810)], "rdfs:subClassOf", (1128,803), kind="sub")
edge([(1365,694),(1365,780)], "rdfs:subClassOf", (1373,742), kind="sub")
edge([(1490,620),(1540,620),(1540,15),(40,15),(40,370),(60,370)], "fdp-o:metadataCatalog", (48,322), card="0..*", cpos=(45,362))
out.append('<text transform="translate(1553,470) rotate(-90)" font-size="13" fill="#222">fdp-o:metadataCatalog</text>')
edge([(190,994),(190,1040),(1520,1040),(1520,85),(1100,85),(1100,100)], "foaf:primaryTopic  (the described metadata record: a dcat:Resource, a dcat:Distribution or an entity of any other class of the content model)", (200,1058), card="1", cpos=(1108,97))
edge([(190,604),(190,880)], "typed additionally as dcat:CatalogRecord\nwhen the topic is a dcat:Resource", (200,735), kind="dashed")

# ---- legend
lx, ly = 1180, 870
out.append(f'<rect x="{lx}" y="{ly}" width="300" height="150" fill="#fff" stroke="#999"/>')
out.append(f'<rect x="{lx+12}" y="{ly+14}" width="26" height="16" fill="{CY["fill"]}" stroke="{CY["stroke"]}"/>')
out.append(f'<text x="{lx+48}" y="{ly+27}" font-size="{FS}" fill="#222">DCAT 3 and other standard vocabularies</text>')
out.append(f'<rect x="{lx+12}" y="{ly+40}" width="26" height="16" fill="{GR["fill"]}" stroke="{GR["stroke"]}"/>')
out.append(f'<text x="{lx+48}" y="{ly+53}" font-size="{FS}" fill="#222">FDP ontology (fdp-o)</text>')
out.append(f'<line x1="{lx+12}" y1="{ly+76}" x2="{lx+38}" y2="{ly+76}" stroke="#333" stroke-width="1.4" marker-end="url(#sub)"/>')
out.append(f'<text x="{lx+48}" y="{ly+80}" font-size="{FS}" fill="#222">rdfs:subClassOf</text>')
out.append(f'<line x1="{lx+12}" y1="{ly+100}" x2="{lx+38}" y2="{ly+100}" stroke="#333" stroke-width="1.4" marker-end="url(#arr)"/>')
out.append(f'<text x="{lx+48}" y="{ly+104}" font-size="{FS}" fill="#222">property (domain → range)</text>')
out.append(f'<text x="{lx+12}" y="{ly+124}" font-size="11" fill="#555">Italics: abstract class.</text>')
out.append(f'<text x="{lx+12}" y="{ly+140}" font-size="11" fill="#555">Only terms used in this specification are shown.</text>')

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Helvetica, Arial, sans-serif">
<title>FDP metadata model based on DCAT 3</title>
<defs>
  <marker id="arr" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="9" markerHeight="9" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="#333"/></marker>
  <marker id="sub" viewBox="0 0 12 12" refX="12" refY="6" markerWidth="12" markerHeight="12" orient="auto"><path d="M 0 0 L 12 6 L 0 12 z" fill="#fff" stroke="#333" stroke-width="1.2"/></marker>
</defs>
<rect width="{W}" height="{H}" fill="#fff"/>
''' + "\n".join(out) + "\n</svg>\n"
open("images/FDPmetadatadiagram.svg","w").write(svg)
print("svg written", len(svg), "bytes")
