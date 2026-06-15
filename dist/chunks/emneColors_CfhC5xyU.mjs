const COLORS = {
  nettverk: { color: "#4f8cff", bg: "rgba(79,140,255,.13)" },
  sikkerhet: { color: "#f97316", bg: "rgba(249,115,22,.13)" },
  operativsystem: { color: "#a855f7", bg: "rgba(168,85,247,.13)" },
  skripting: { color: "#10b981", bg: "rgba(16,185,129,.13)" },
  databaser: { color: "#f59e0b", bg: "rgba(245,158,11,.13)" },
  "it-drift": { color: "#ec4899", bg: "rgba(236,72,153,.13)" }
};
const EMNE_LIST = Object.keys(COLORS);
function getEmneColor(emne) {
  return COLORS[emne] ?? COLORS["nettverk"];
}

export { EMNE_LIST as E, getEmneColor as g };
