# HE UT6 · Ficha 03 — Compromiso y escalada reproducible (HE-E12)

**Módulo** 5025 · **UT6** · **RA3 e** · **Evidencia HE-E12** (I3 · R3, reto integrado 35 %).
**Entorno**: VLAN aislada. **Se entrega también a IC** como caso a investigar.
Prerrequisito: ROE firmado. Comprometer sistemas de terceros es delito (arts. 197 bis, 264).

> El entregable **es** la reproducibilidad: un compañero debe poder repetir tu compromiso
> **solo con tu documento**, sin preguntarte nada. Si no es repetible, no está.

## Objetivo

Comprometer el servicio `vuln-app` (`http://objetivo.xest.local:8085`), obtener una shell,
**escalar a root** y documentar cada paso de forma reproducible sobre la plantilla
`plantilla-HE-E12-compromiso.md`.

## Fases (sigue el orden; documenta cada una con comando + salida)

1. **Reconocimiento del servicio.** Enumera el puerto 8085 con nmap; identifica la app y su
   punto de entrada (la consola de diagnóstico `/ping.php`).
2. **Acceso inicial (RCE).** La consola "hace ping" a un host. Encuentra por qué eso te deja
   ejecutar comandos arbitrarios y consigue ejecutar `id` en el servidor. ¿Con qué usuario
   corres?
3. **Shell interactiva.** Convierte la ejecución puntual en una shell. Usa **Metasploit**
   (`multi/handler`) para recibir una *reverse shell*. Genera la carga con `msfvenom`.
4. **Enumeración local.** Ya dentro, busca vías de escalada: `sudo -l`, binarios **SUID**,
   versión de kernel, credenciales en disco. Identifica la vía.
5. **Escalada a root.** Explota la vía encontrada y demuestra `id` con `uid=0`. Lee la prueba
   `/root/flag.txt`.
6. **Contramedida.** Para cada uno de los dos fallos (RCE y escalada), escribe la corrección
   concreta que lo habría impedido.

## Verificación (R3 · "Automatización y repetibilidad")

- El compromiso se comprueba en el destino: `id` con `uid=0` y el contenido de la flag.
- Prueba tu propia reproducibilidad: recrea el objetivo (`--force-recreate vuln-app`) y
  repite tu procedimiento **paso a paso desde tu documento**. Si algo falla, tu doc está
  incompleto.

## Higiene operativa

No dejes shells colgadas ni ficheros subidos al objetivo. Documenta qué tocaste. Los datos
capturados se gestionan según el ROE.

## Entregable

`NN-HE-E12-compromiso.md` sobre `plantilla-HE-E12-compromiso.md`: cadena completa (recon →
RCE → shell → enumeración → privesc → prueba), cada paso con **comando y salida**, y las dos
contramedidas. **Este documento se entrega a IC** para que investigue la intrusión. Mapea a
**MITRE ATT&CK**: Initial Access / **T1190** (Exploit Public-Facing Application),
Execution / **T1059**, Privilege Escalation / **T1548** (Abuse Elevation Control /SUID).
