# Schools - Open data

## Sources

### Cermat

-  [Jednotná přijímací zkouška](https://data.cermat.cz/menu/data-a-analyticke-vystupy-jednotna-prijimaci-zkouska) - [Datové soubory](https://data.cermat.cz/menu/data-a-analyticke-vystupy-jednotna-prijimaci-zkouska/datove-soubory)
   - Data za uchazeče (fyzické osoby) - přihlášky a výsledky
   - Rok 2024: [Kolo 1](https://data.cermat.cz/files/files/pz2024_kolo1_fyzosoby_prihlasky_vysledky.xlsx), [Kolo 2](https://data.cermat.cz/files/files/pz2024_kolo2_fyzosoby_prihlasky_vysledky.xlsx)
   - Format: Excel
 - [Položková data didaktických testů jednotné přijímací zkoušky](https://vysledky.cermat.cz/statistika/Default.aspx)
   - Je nutne zvolit v levem menu typ zkousky
   - [Schema a vysvetleni polozek](https://vysledky.cermat.cz/statistika/Info.aspx?infoid=polozkovaData_info5b)

### Ministerstvo skolstvi

- [Vsechny mozne ciselniky ve skolstvi](http://stistko.uiv.cz/katalog/ciselnik.asp?vse=Zobrazit+v%9Aechny)
  - [AKSO  Obory vzdělání regionálního školství (KKOV)](http://stistko.uiv.cz/katalog/ciselnik11x.asp?idc=AKSO&ciselnik=Obory+vzd%ECl%E1n%ED+region%E1ln%EDho+%9Akolstv%ED+%28KKOV%29&aap=on&poznamka=)
  - [AKDT  Druhy a typy škol a školských zařízení (nové)](http://stistko.uiv.cz/katalog/ciselnik11x.asp?idc=AKDT&ciselnik=Druhy+a+typy+%9Akol+a+%9Akolsk%FDch+za%F8%EDzen%ED+%28nov%E9%29&aap=on&poznamka=)
- [Rejstrik skol](https://rejstriky.msmt.cz/rejskol/)
- [Kategorie Vzdelavani na npi](https://archiv-nuv.npi.cz/t/stredni-vzdelavani.html)
- [Kategorie Vzdelavani na wiki](https://cs.wikipedia.org/wiki/Obor_vzd%C4%9Bl%C3%A1n%C3%AD)
- [Rejstrik skol na data.gov (XML)](https://data.gov.cz/datov%C3%A1-sada?iri=https%3A%2F%2Fdata.gov.cz%2Fzdroj%2Fdatov%C3%A9-sady%2F00022985%2F63989c80e16fc31c77e23ab529c76b52)

### CSU

- [Malý lexikon obcí České republiky - 2023](https://csu.gov.cz/produkty/maly-lexikon-obci-ceske-republiky-2023)

### Atlas Skolstvi

- [Homepage -> stredni skoly](https://www.atlasskolstvi.cz/stredni-skoly)
   - [Praha](https://www.atlasskolstvi.cz/stredni-skoly?region=hlm-praha)
     - Skoly jsou v seznamu elementu
     - xpath: `/html/body/section[1]/div/div[1]/ul`
     - class="schoollist"
     ``` html
     <ul class="schoollist cols1">
      <li>
         <a href="/ss172-stredni-skola-podnikani-a-gastronomie">
         <h2>Střední škola podnikání a gastronomie</h2>
         <article>Za Černým mostem 362/3, Hloubětín, 198 00 Praha 9</article>	</a>
      </li>
     </ul>
     ```
     - Musi se pagovat pres `p=2`

### Verejny dalkovy pristup k datum RUIAN

- [Adresy v CR (pozor, opravdu velky soubor)](https://vdp.cuzk.cz/vdp/ruian/vymennyformat?crKopie=on&casovyRozsah=U&svyAdresy=on&svyber=svyAdresy&search=)
- [Adresní místa RÚIAN ve formátu CSV](https://nahlizenidokn.cuzk.cz/StahniAdresniMistaRUIAN.aspx)
  - [Popis](https://vdp.cuzk.cz/vymenny_format/csv/hierarchie-prvku-ruian-popis.pdf)
  - 

### Ceska Inspekce

- [Formular na vyhledavani skol](https://portal.csicr.cz/Search/School)
  - Moznost vyhledavani i podle Kraje, ICO, RED-IZO
  - Parametery
    - pageSize
      - `pageSize=400`
    - Kraj (a05ID):
         ``` html
         <select data-val="true" data-val-number="The field a05ID must be a number." data-val-required="The a05ID field is required." id="a05ID" name="a05ID"><option value="">-- vyberte --</option>
         <option value="1">Praha</option>
         <option value="11">Středočeský</option>
         <option value="3">Jihočeský</option>
         <option value="10">Plzeňský</option>
         <option value="7">Karlovarský</option>
         <option value="13">Ústecký</option>
         <option value="8">Liberecký</option>
         <option value="5">Královéhradecký</option>
         <option value="4">Pardubický</option>
         <option value="6">Vysočina</option>
         <option value="2">Jihomoravský</option>
         <option value="9">Olomoucký</option>
         <option value="15">Zlínský</option>
         <option value="12">Moravskoslezský</option>
         </select>
         ```
      - Priklad: [Praha](https://portal.csicr.cz/Search/School/?FilterType=Default&advancedFilter=false&pageSize=25&totalFound=0&page=1&a03ICO=&a03REDIZO=&a17UIVCode=C&Lat=&Lng=&LatLngRadius=10&a03Name=&a03Street=&a03City=&a05ID=1&a09ID=)
    - Podle RED-IZO (uvedene v detailech pro predmet)
      ``` html
      <input id="a03REDIZO" name="a03REDIZO" type="text" value="">
      ```
   - Typ Skoly
      ``` html
      <select id="a17UIVCode" name="a17UIVCode"><option value="">-- vyberte --</option>
      <option value="A">Mateřské školy</option>
      <option value="B">Základní školy</option>
      <option selected="selected" value="C">Střední školy</option>
      <option value="D">Konzervatoře</option>
      <option value="E">Vyšší odborné školy</option>
      <option value="F10">Základní umělecké školy</option>
      <option value="G11">Střediska volného času</option>
      <option value="K10,K20">Školská poradenská zařízení</option>
      <option value="H22,H21">Domovy mládeže</option>
      <option value="F20">Jazykové školy s p. jaz. zk.</option>
      </select>
      ```
- URLko primo na detail skoly (pres RED-IZO)
  - https://portal.csicr.cz/School/600008703 (to posledni cislo je prave to RED-IZO)
  - Doplnujici udaje jsou v tabulce, ale je to system "harmonika", ktery vyzaduje rucni rozkliknuti (tj asi pres Selenium)
