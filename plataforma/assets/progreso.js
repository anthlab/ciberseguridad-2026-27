// Progreso del alumno: se guarda solo en su navegador (localStorage). No sale de su equipo.
(function () {
  const CLAVE = "curso2627-progreso";
  const UT_RE = /(PPS|HE|IC)\/UT(\d)\/GUIA-ALUMNADO\.html/;
  const leer = () => { try { return JSON.parse(localStorage.getItem(CLAVE)) || {}; } catch (e) { return {}; } };
  const guardar = (p) => localStorage.setItem(CLAVE, JSON.stringify(p));

  function botonUT() {
    const m = location.pathname.match(UT_RE);
    const h1 = document.querySelector(".md-content h1");
    if (!m || !h1 || document.querySelector(".progreso-ut")) return;
    const id = m[1] + "-UT" + m[2];
    const caja = document.createElement("div");
    caja.className = "progreso-ut";
    const b = document.createElement("button");
    const pintar = () => {
      const hecha = !!leer()[id];
      b.className = hecha ? "hecha" : "";
      b.textContent = hecha ? "✓ Unidad terminada" : "Marcar unidad como terminada";
    };
    b.onclick = () => { const p = leer(); p[id] = !p[id]; guardar(p); pintar(); marcarNav(); };
    pintar();
    caja.appendChild(b);
    h1.after(caja);
  }

  function barras() {
    const p = leer();
    document.querySelectorAll(".progreso-modulo[data-modulo]").forEach((el) => {
      const mod = el.dataset.modulo;
      const n = Object.keys(p).filter((k) => k.startsWith(mod + "-") && p[k]).length;
      el.innerHTML = '<div class="barra"><span style="width:' + (n / 8) * 100 + '%"></span></div>' +
        "<small>" + n + " de 8 unidades terminadas</small>";
    });
  }

  function marcarNav() {
    const p = leer();
    document.querySelectorAll(".md-nav__link[href]").forEach((a) => {
      const m = a.getAttribute("href").match(/(PPS|HE|IC)\/UT(\d)\/GUIA-ALUMNADO\.html/) ||
        new URL(a.href, location.href).pathname.match(UT_RE);
      if (m) a.classList.toggle("ut-hecha", !!p[m[1] + "-UT" + m[2]]);
    });
    barras();
  }

  function iniciar() { botonUT(); marcarNav(); }
  if (window.document$) document$.subscribe(iniciar); else document.addEventListener("DOMContentLoaded", iniciar);
})();
