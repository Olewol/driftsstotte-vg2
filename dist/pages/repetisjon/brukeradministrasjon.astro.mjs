/* empty css                                     */
import { c as createComponent, e as renderComponent, a as renderTemplate, m as maybeRenderHead, d as addAttribute } from '../../chunks/astro/server_B0BmM5RJ.mjs';
import 'piccolore';
import { $ as $$RepetisjonLayout } from '../../chunks/RepetisjonLayout_DVT-Ri2U.mjs';
export { renderers } from '../../renderers.mjs';

const $$Brukeradministrasjon = createComponent(($$result, $$props, $$slots) => {
  const base = "/driftsstotte-vg2";
  return renderTemplate`${renderComponent($$result, "RepetisjonLayout", $$RepetisjonLayout, { "title": "Brukeradministrasjon", "description": "Katalogtjenester, Active Directory, OU-struktur, RBAC, Kerberos, GPO.", "prev": null, "next": "infrastruktur-maskinvare", "nextLabel": "Infrastruktur og maskinvare" }, { "default": ($$result2) => renderTemplate`
En katalogtjeneste (Active Directory eller Entra ID) lagrer alle brukere, maskiner og tilganger i en sentral database. AD organiseres som et hierarki: skog, trær, domener og OU-er. Roller gir rettigheter via grupper, ikke enkeltbrukere. Kerberos er standarden for autentisering — sikrere enn NTLM fordi passordet aldri går over nettverket.
${maybeRenderHead()}<div class="hvorfor-callout"> <div class="hvorfor-callout-title">Hvorfor skal du bry deg?</div> <p>Du kommer til å jobbe med brukeradministrasjon <strong>hver dag</strong>. Ny ansatt: opprett konto, plasser i riktig OU, gi tilganger via sikkerhetsgrupper, treff med GPO-er. Ansatt slutter: deaktiver, ikke slett. En sletting fjerner SID-en som henger sammen med alle ACL-er, e-postbokser og revisjonslogger. Feil her = sikkerhetshull eller ansatte som ikke får gjort jobben sin.</p> </div> <h2>Detaljer</h2> <h3>Katalogtjenester</h3>
En katalogtjeneste lagrer objekter (brukere, datamaskiner, skrivere, grupper) og gjør dem søkbare.
<table><thead><tr> <th>Tjeneste</th> <th>Type</th> <th>Bruksområde</th> </tr></thead><tbody> <tr> <td>Active Directory DS (AD DS)</td> <td>Lokal</td> <td>Windows-baserte bedriftsnettverk, egen server</td> </tr> <tr> <td>Entra ID (tidl. Azure AD)</td> <td>Sky</td> <td>Microsoft 365, skybasert identitetsstyring</td> </tr> <tr> <td>OpenLDAP</td> <td>Åpen kilde</td> <td>Linux/Unix-miljøer</td> </tr> </tbody></table> <h3>AD-hierarkiet — fra skog til OU</h3>
Active Directory er bygget opp som et hierarki. Rekkefølgen er viktig å kunne.
<img${addAttribute(`${base}/diagrams/ad-hierarchy.svg`, "src")} alt="AD-hierarki: Skog, Tre, Domene, OU" style="max-width:100%;height:auto;margin:1rem 0;border-radius:10px;border:1px solid var(--border);background:#fff;"> <table><thead><tr> <th>Nivå</th> <th>Beskrivelse</th> </tr></thead><tbody> <tr> <td><strong>Skog (Forest)</strong></td> <td>Øverste nivå, inneholder ett eller flere trær</td> </tr> <tr> <td><strong>Tre (Tree)</strong></td> <td>Hierarki av domener med felles navnerom</td> </tr> <tr> <td><strong>Domene (Domain)</strong></td> <td>Grunnenhet — deler felles database og sikkerhetspolicy</td> </tr> <tr> <td><strong>OU (Organisasjonsenhet)</strong></td> <td>Logisk beholder for brukere, maskiner, grupper</td> </tr> </tbody></table>
Hierarkiet betyr noe: GPO-er arves nedover. En policy satt på domenet gjelder alle OU-er med mindre en mer spesifikk policy overstyrer. Planlegg OU-strukturen før du oppretter brukere — det er mye vanskeligere å flytte dem etterpå.
<h4>Best Practice for OU-struktur</h4>
\`\`\`
firma.local
+-- OU=Brukere
|   +-- OU=AvdelingA
|   +-- OU=AvdelingB
|   +-- OU=AvdelingC
+-- OU=Datamaskiner
|   +-- OU=Kontor
|   +-- OU=Felt
+-- OU=Grupper
    +-- OU=Sikkerhetsgrupper
    +-- OU=Distribusjonsgrupper
\`\`\`
<h3>Rollebasert tilgang (RBAC)</h3>
RBAC er prinsippet om at rettigheter gis via roller/grupper, ikke til enkeltbrukere. Slik fungerer det i praksis:
<img${addAttribute(`${base}/diagrams/rbac-flow.svg`, "src")} alt="RBAC-flyt: Gruppe → Bruker → Rettigheter" style="max-width:100%;height:auto;margin:1rem 0;border-radius:10px;border:1px solid var(--border);background:#fff;"> <ol> <li>Opprett sikkerhetsgrupper per rolle: <code>SG_Admin</code>, <code>SG_Salg</code>, <code>SG_Drift</code></li> <li>Plasser brukere i riktig gruppe</li> <li>Tildel tillatelser til gruppen — <strong>aldri</strong> til enkeltbrukere</li> <li><strong>Minste privilegium</strong>: kun tilgangene som trengs for å utføre jobben</li> </ol>
Rettigheter på enkeltbrukere er en dårlig vane som går igjen. Problemet: når den ansatte bytter rolle, må du huske å fjerne alle de gamle rettighetene. Med grupper flytter du brukeren til ny gruppe, og alt følger automatisk.
<h3>Autentisering — Kerberos vs NTLM</h3> <table><thead><tr> <th>Egenskap</th> <th>Kerberos</th> <th>NTLM</th> </tr></thead><tbody> <tr> <td>Standard i AD</td> <td>Ja, siden Windows 2000</td> <td>Eldre, kun bakoverkompatibilitet</td> </tr> <tr> <td>Passord på nettverket</td> <td>Aldri — bruker billetter</td> <td>Sender hashet versjon</td> </tr> <tr> <td>Gjensidig autentisering</td> <td>Ja (både klient og server)</td> <td>Nei (kun klient)</td> </tr> <tr> <td>Motstår replay-angrep</td> <td>Ja (tidsstempler)</td> <td>Sårbar uten ekstra tiltak</td> </tr> </tbody></table> <h4>Slik fungerer Kerberos</h4>
Kerberos bruker en tredjepart (Key Distribution Center, KDC) som utsteder billetter. Når du logger på, får du en Ticket Granting Ticket (TGT). Denne bruker du til å be om billetter til spesifikke tjenester — uten at passordet ditt noen gang sendes over nettverket.
<h3>GPO — Group Policy Objects</h3>
Gruppepolicy distribuerer innstillinger til datamaskiner og brukere via OU-er. Eksempler: installer programvare, begrens tilgang til kontrollpanel, sett passordpolicy. Arves fra overordnet OU. Det mest spesifikke policy-nivået vinner.
<h4>Hvordan GPO-arving fungerer</h4> <ul> <li>En GPO på domenenivå gjelder alle OU-er under</li> <li>En GPO på en OU overstyrer domenepolicyen for den OU-en</li> <li>"Enforce" (tvungen) kan blokkere overstyring</li> <li>"Block inheritance" på en OU stopper arv fra overordnet</li> </ul> <div class="nokkelbegreper"> <div class="nokkelbegreper-title">Nøkkelbegreper</div> <div class="nokkelbegreper-grid"> <div class="nokkelbegrep-item"> <strong>SID</strong> <span>Unik sikkerhetsidentifikator for hver bruker/gruppe. Systemet bruker SID internt for tilgangskontroll — derfor ødelegger sletting av bruker alle ACL-er.</span> </div> <div class="nokkelbegrep-item"> <strong>LDAP</strong> <span>Protokoll for tilgang til katalogtjenesten (port 389). Slår opp brukere, grupper og maskiner.</span> </div> <div class="nokkelbegrep-item"> <strong>DC</strong> <span>Domenekontroller — server med AD DS. Autentiserer brukere og lagrer AD-databasen. Du trenger minst 2 for redundans.</span> </div> <div class="nokkelbegrep-item"> <strong>UAC</strong> <span>User Account Control. Hindrer programmer i å kjøre som admin uten godkjenning. Irriterende, men viktig.</span> </div> <div class="nokkelbegrep-item"> <strong>GPO</strong> <span>Group Policy Object. Sentrale innstillinger som distribueres til datamaskiner og brukere via AD.</span> </div> <div class="nokkelbegrep-item"> <strong>OU</strong> <span>Organisasjonsenhet i AD. Strukturerer domenet og knytter GPO-er til riktige brukere/maskiner.</span> </div> </div> </div> <div class="tips-callout"> <div class="tips-callout-title">Praktiske tips</div> <p><strong>Navnestandard:</strong> Bruk <code>fornavn.etternavn</code> for brukere, <code>SRV-funksjon-nummer</code> for servere. Konsistent navngivning sparer deg for mye letting.</p> <p><strong>Grupper, ikke enkeltbrukere:</strong> ALLTID rettigheter på grupper. Bruker skifter rolle? Flytt til ny gruppe — resten automatisk.</p> <p><strong>Deaktiver, ikke slett:</strong> Ansatt slutter? Deaktiver kontoen. Sletting fjerner SID-en og ødelegger ACL-er, e-post og revisjonslogg. La kontoen ligge deaktivert i 30 dager før du vurderer sletting.</p> </div> <div class="eksamen-callout"> <div class="eksamen-callout-title">Husk til eksamen</div> <p><strong>AD-hierarkiet:</strong> Skog → Tre → Domene → OU. Lær rekkefølgen.</p> <p><strong>Kerberos vs NTLM:</strong> Kerberos = billetter og gjensidig autentisering. NTLM = gammelt, kun for bakoverkompabilitet.</p> <p><strong>RBAC:</strong> Rettigheter til grupper, ikke enkeltbrukere. Minste privilegium er stikkordet.</p> <p><strong>GPO:</strong> Knyttes til OU-er. Arves nedover. Mest spesifikk vinner.</p> <p><strong>Vanlig oppgave på eksamen:</strong> "Foreslå OU-struktur for en bedrift med 3 avdelinger" — tegn hierarki, forklar hvorfor.</p> </div> <div class="sjekk-sporsmal"> <div class="sjekk-sporsmal-title">Sjekk om du kan dette</div> <div class="sjekk-q"> <div class="sjekk-q-question">Hva er forskjellen på Kerberos og NTLM?</div> <div class="sjekk-q-answer">Kerberos bruker billetter — passordet sendes aldri over nettverket. Gir gjensidig autentisering og beskytter mot replay-angrep. NTLM sender en hashet versjon av passordet og autentiserer kun klienten. Kerberos har vært standard i AD siden Windows 2000.</div> </div> <div class="sjekk-q"> <div class="sjekk-q-question">Hvorfor skal du aldri slette en brukerkonto når en ansatt slutter?</div> <div class="sjekk-q-answer">Sletting fjerner SID-en som er knyttet til alle ACL-er, e-post, SharePoint-tilganger og revisjonslogger. Riktig prosedyre: deaktiver kontoen, endre passord på tjenestekontoer vedkommende hadde tilgang til, og overfør e-post/filer til leder.</div> </div> <div class="sjekk-q"> <div class="sjekk-q-question">Hva er minste privilegium, og hvorfor er det viktig?</div> <div class="sjekk-q-answer">Brukere og systemer skal kun ha tilgangene de trenger for å utføre jobben. En selger trenger ikke admin-tilgang til servere. Reduserer risiko for både utilsiktede feil og bevisste angrep.</div> </div> </div> ` })}`;
}, "/home/ole/workspace/driftsstotte-vg2/src/pages/repetisjon/brukeradministrasjon.astro", void 0);
const $$file = "/home/ole/workspace/driftsstotte-vg2/src/pages/repetisjon/brukeradministrasjon.astro";
const $$url = "/driftsstotte-vg2/repetisjon/brukeradministrasjon";

const _page = /*#__PURE__*/Object.freeze(/*#__PURE__*/Object.defineProperty({
  __proto__: null,
  default: $$Brukeradministrasjon,
  file: $$file,
  url: $$url
}, Symbol.toStringTag, { value: 'Module' }));

const page = () => _page;

export { page };
