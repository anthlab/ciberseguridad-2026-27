# HE-E12 — Compromiso de `vuln-app` documentado y reproducible

> Rellena esta plantilla. **Criterio de superación**: un compañero repite tu compromiso
> desde cero usando solo este documento. Cada paso = comando + salida real (marca de tiempo).
> Se entrega también a IC como caso a investigar.

- **Autor (nº lista + nombre)**:
- **Fecha / hora (ventana del ROE)**:
- **Objetivo**: `objetivo.xest.local:8085` (vuln-app) · VLAN de laboratorio aislada
- **Alcance / autorización**: ROE del curso HE-E1 (ref.:            )
- **Estación atacante**: IP            · herramientas: nmap, curl, Metasploit

## 1. Reconocimiento
_Comando + salida. Servicio y punto de entrada identificados._

## 2. Acceso inicial (vulnerabilidad explotada)
_Qué fallo, en qué parámetro/endpoint. Comando que consigue ejecución. Usuario obtenido (`id`)._
- Técnica ATT&CK: T1190 (Exploit Public-Facing Application) / T1059 (Command and Scripting Interpreter)

## 3. Shell interactiva
_Cómo pasas de ejecución puntual a shell. Carga (msfvenom), manejador (multi/handler), sesión abierta._

## 4. Enumeración local
_`sudo -l`, SUID (`find / -perm -4000`), kernel. Vía de escalada identificada y por qué._

## 5. Escalada de privilegios
_Comando exacto de la escalada. Prueba: `id` con `uid=0`/`euid=0` + contenido de `/root/flag.txt`._
- Técnica ATT&CK: T1548 (Abuse Elevation Control Mechanism — SUID)

## 6. Impacto
_Qué controla un atacante con este acceso. Dimensión(es) de seguridad rota(s)._

## 7. Contramedidas
| Fallo | Corrección concreta |
|---|---|
| RCE |  |
| Escalada (SUID) |  |

## 8. IoC para IC (equipo azul)
| Indicador | Valor | Dónde se ve |
|---|---|---|
| IP atacante |  | logs Apache / conexiones salientes |
| Patrón de petición | `/ping.php?host=...;<cmd>` | access.log de Apache |
| Conexión C2 | `10.10.10.50:4444` | netstat / firewall |

## 9. Reproducibilidad (autocomprobación)
_Recreé el objetivo y repetí el procedimiento desde este documento: ¿funcionó sin ayuda? (sí/no + qué faltó)._
