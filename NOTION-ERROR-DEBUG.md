# 🔧 NOTION ERROR DEBUGGING GUIDE

## Stap 1: Check Zapier Step 5 Output

1. Open je Zapier workflow
2. Ga naar Step 5 (Code by Zapier)
3. Klik "Test"
4. Scroll naar beneden naar "Output"
5. Check deze velden:

```
notion_vacature_url: [moet null zijn of een URL]
notion_jobdigger_url: [moet null zijn of een URL]
notion_linkedin_ti_url: [moet null zijn of een URL]
```

**❌ FOUT**: Als je ziet `""` (lege string) → Code niet geüpdatet!
**✅ GOED**: Als je ziet `null` of een URL → Code is correct!

---

## Stap 2: Check Notion Step 7 Configuration

### Optie A: Gebruik Text Properties (SIMPELSTE OPLOSSING!)

In plaats van URL properties, gebruik **Text** properties in Notion:

1. Open je Notion database
2. Klik op "Vacature URL" property → Properties → Edit property
3. Verander Type van "URL" naar "Text"
4. Herhaal voor "Jobdigger URL" en "LinkedIn TI URL"

**Dit lost 99% van de URL errors op!**

---

### Optie B: Gebruik URL Properties met Filter

Als je toch URL properties wilt gebruiken:

1. In Zapier Step 7 (Notion)
2. Klik op het tandwiel naast elk URL veld
3. Voeg een "Filter" toe:
   - **Only continue if**: `{{5. notion_vacature_url}}` exists
   - En is not: (empty)

Dit slaat lege velden over.

---

## Stap 3: Check Field Mapping

In Zapier Step 7, zorg dat je dit exact gebruikt:

```yaml
Vacature URL: {{5. notion_vacature_url}}
Jobdigger URL: {{5. notion_jobdigger_url}}
LinkedIn TI URL: {{5. notion_linkedin_ti_url}}
```

**NIET**:
```yaml
Vacature URL: {{1. Vacature URL}}  ❌ FOUT - Dit is van JotForm!
```

---

## Stap 4: Verwijder Page Content Blocks met Links

Als je "Page Content Blocks" hebt in Notion step:

1. Scroll naar beneden in Zapier Step 7
2. Zie je "Add Page Content"?
3. Verwijder alle blocks die URLs bevatten
4. Of maak ze CONDITIONAL met filter

---

## Veelvoorkomende Errors & Oplossingen

### Error: "body.children[X].bulleted_list_item.rich_text[0].text.link.url should be populated"

**Oorzaak**: Je hebt een Page Content block met een lege URL link.

**Oplossing 1** (Simpelst): Verwijder alle Page Content blocks
**Oplossing 2**: Maak elk block conditional (zie Stap 2, Optie B)

---

### Error: "validation_error: body.properties.Vacature URL.url"

**Oorzaak**: Notion URL property krijgt lege string `""` in plaats van `null`

**Oplossing**:
1. Check of Step 5 output `null` toont (niet `""`)
2. Zo niet → Update de code in Step 5
3. Zo wel → Verander property type naar "Text" in Notion

---

### Error: "invalid_json"

**Oorzaak**: Field mapping klopt niet

**Oplossing**: Check dat je `{{5. notion_vacature_url}}` gebruikt (van Step 5 output), niet `{{1. Vacature URL}}`

---

## Quick Fix Checklist

- [ ] Code geüpdatet in Step 5?
- [ ] Step 5 output toont `null` voor lege URLs?
- [ ] Notion properties zijn "Text" (niet "URL")?
- [ ] Field mapping gebruikt `{{5. notion_...}}`?
- [ ] Geen Page Content blocks met URLs?
- [ ] Test gedraaid na elke change?

---

## Test Data voor Debugging

Gebruik deze test data in JotForm:

```
bedrijfsnaam: Test BV
functietitel: Test Developer
contactpersoon: Jan de Tester
email: test@test.nl
telefoon: 0612345678
sector: IT & Technology
locatie: Amsterdam
urgentie: Normaal

vacature_url: [LAAT LEEG]
jobdigger_url: https://drive.google.com/file/d/test123
linkedin_ti_url: [LAAT LEEG]
```

**Verwachte output Step 5**:
```
notion_vacature_url: null
notion_jobdigger_url: "https://drive.google.com/file/d/test123"
notion_linkedin_ti_url: null
```

**Verwachte resultaat Notion**:
- Vacature URL: [leeg]
- Jobdigger URL: https://drive.google.com/file/d/test123
- LinkedIn TI URL: [leeg]

✅ **GEEN ERROR!**

---

## Nog steeds error?

**Stuur me**:
1. Screenshot van Step 5 output (notion_vacature_url, notion_jobdigger_url, notion_linkedin_ti_url)
2. Exacte error message van Step 7
3. Screenshot van je Notion property types (URL of Text?)

Dan kunnen we het verder troubleshooten!
