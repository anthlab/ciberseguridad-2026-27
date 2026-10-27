# Ficha — Lectura crítica de las métricas del simulacro (IC UT2 · para el alumnado)

Parte de **IC-E3** (laboratorio, rúbrica R1). Trabajáis con `metricas-simulacro-ejemplo.csv`:
un export sintético de un simulacro sobre una organización de 30 personas (10 por segmento).
El correo se **envió a las 09:00**. Trabajo en parejas.

> No basta con decir "un 30 % picó". La pregunta que contiene el incidente es:
> **¿cuánto tardó el primero en avisar?**

## 1. Embudo global
Calcula sobre el total (30) y anota el porcentaje:

| Métrica | Cuenta | % |
|---|---|---|
| Enviados | | |
| Abrieron | | |
| Hicieron clic | | |
| Enviaron credenciales | | |
| **Reportaron** | | |

Pista de cálculo rápido (línea de comandos):
```bash
# nº de clics
awk -F, 'NR>1 && $6=="si"' metricas-simulacro-ejemplo.csv | wc -l
# nº de reportes
awk -F, 'NR>1 && $9=="si"' metricas-simulacro-ejemplo.csv | wc -l
```

## 2. Tiempo de reacción
- Hora del **primer clic**: __________
- Hora del **primer reporte**: __________
- ¿Qué ocurrió antes, el primer clic o el primer aviso? ¿Qué implica para el SOC?

## 3. Desglose por segmento
Completa (clic %, reporte %, credenciales %, hora del primer reporte del segmento):

| Segmento | Clic % | Reporte % | Credenciales % | 1.er reporte |
|---|---|---|---|---|
| Dirección | | | | |
| Técnicos | | | | |
| Administración | | | | |

## 4. Interpretación (lo que de verdad se evalúa)
1. ¿Qué segmento es el **más fuerte** y cuál el **más débil**? Justifícalo con los números.
2. Alguien dice: "clic = comprometido". ¿Lo confirman los datos? (mira clic vs credenciales).
3. "Modela la clase inocente": ¿quién, además de quien no picó, cuenta como **buen
   comportamiento**? ¿Por qué es un error resumir todo a "picó / no picó"?
4. Da **una** acción correctora concreta que saldría de estos datos.

**Entrega IC-E3**: `NN-IC-E3-simulacro.md` con el embudo, el desglose y esta interpretación,
más la ficha de auditoría de cumplimiento.
