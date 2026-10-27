// inject.js — carga útil de MODIFICACIÓN para el MITM de HE UT6.
// bettercap la inserta en toda respuesta HTTP en claro servida a la víctima.
// Objetivo pedagógico: demostrar que el intermediario no solo LEE, también REESCRIBE
// el contenido. Es la evidencia que pide HE-E11. Inofensiva: solo pinta una banda.
(function () {
  function marcar() {
    var b = document.createElement('div');
    b.textContent = '⚠ CONTENIDO INTERCEPTADO Y MODIFICADO POR EL EQUIPO ROJO — HE UT6 (laboratorio xest)';
    b.style.cssText = 'position:fixed;top:0;left:0;right:0;z-index:2147483647;' +
      'background:#f7768e;color:#111a2b;font:700 15px/1.4 system-ui,sans-serif;' +
      'padding:10px 14px;text-align:center;box-shadow:0 2px 8px rgba(0,0,0,.4)';
    document.body.appendChild(b);
    console.log('[MITM-HE-UT6] respuesta HTTP modificada en tránsito');
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', marcar);
  } else {
    marcar();
  }
})();
