# HE UT6 · Ficha 01 — Ataque de intermediario y su límite (HE-E11)

**Módulo** 5025 Hacking Ético · **UT6** · **RA3 c,d** · **Evidencia HE-E11** (I1 · R1, 20 %).
**Entorno**: VLAN de laboratorio aislada. **Prerrequisito bloqueante**: ROE del curso
firmado (HE-E1). Interceptar tráfico ajeno fuera de aquí es delito (art. 197 ter CP).

> **Regla de la unidad**: cada ataque de hoy se documenta **junto a su contramedida**.
> HE-E11 no está completa si no demuestras a la vez que el MITM funciona en HTTP en claro
> **y** que HSTS lo frustra.

## Objetivo

Situarte entre la estación víctima y el portal, **leer y modificar** su tráfico HTTP en
claro, y después comprobar sobre un servicio con HTTPS+HSTS que el mismo ataque **falla**.

## Preparación (estación atacante, Kali)

```bash
ip a                                   # confirma tu interfaz e IP en la VLAN (ej. eth0, 10.10.10.50)
ping -c1 objetivo.xest.local           # el portal responde
```

Copia a tu carpeta de trabajo la plantilla de MITM: `caplets/xest-mitm.cap` y
`caplets/inject.js`. Ajusta en el `.cap` la IP de la **víctima** (`arp.spoof.targets`) y
tu interfaz.

## Tareas

1. **Reconocimiento del segmento.** Con bettercap, descubre los hosts de la VLAN y localiza
   la IP de la estación víctima y la del gateway. Anótalas.
2. **Envenenamiento ARP + intercepción.** Coloca a tu Kali como intermediario entre la
   víctima y el portal. Captura una petición de login del portal (usuario/contraseña) en
   **claro**. Adjunta la evidencia (captura de pantalla del sniffer / de Wireshark).
3. **Modificación del tráfico.** Inyecta el JavaScript de `inject.js` en las respuestas HTTP
   del portal. Demuestra con una captura que **la víctima ve contenido que el servidor no
   envió** (la banda del equipo rojo). *La modificación es lo que exige HE-E11; capturar no
   basta.*
4. **El límite defensivo.** Repite el intento contra `https://objetivo.xest.local:8443`
   (HSTS activo). Documenta **qué ocurre** y **por qué** el intermediario ya no puede leer
   ni reescribir. Explica el papel de la cabecera `Strict-Transport-Security`.
5. **Contramedida.** Enumera al menos **tres** medidas que habrían frustrado el ataque del
   punto 2-3 en una red real (una de red, una de servidor, una de cliente).

## Verificación (te la exigirá la rúbrica R1, criterio "Verificación del resultado")

- La modificación se comprueba **en el destino** (en el navegador de la víctima), no solo
  en tu consola de bettercap.
- El fallo contra HSTS se comprueba **por contenido**: el navegador rechaza el HTTP o no
  aparece tu inyección; una captura de "no pasó nada" no vale sin la explicación del porqué.

## Higiene operativa (criterio R1)

Al terminar: `arp.spoof off`, cierra bettercap, y verifica que la víctima recupera la
conectividad normal (sin ti de intermediario). No dejes el ARP envenenado.

## Entregable

`NN-HE-E11-mitm.md` con: mapa del segmento, evidencia de captura (paso 2), evidencia de
**modificación** (paso 3), el contraste con HSTS (paso 4) y las contramedidas (paso 5).
Cada evidencia con marca de tiempo. Mapea el ataque a **MITRE ATT&CK T1557**
(Adversary-in-the-Middle).
