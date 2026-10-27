package com.xest.notaslab;

import android.content.SharedPreferences;
import android.content.Context;

/**
 * Gestión de la compra "NotasXest Premium" — versión de laboratorio VULNERABLE (PPS · UT6).
 *
 * Error a encontrar:
 *   6) La compra se valida SOLO en el cliente. El propio dispositivo decide si el usuario
 *      es premium mirando una respuesta manipulable y escribiendo un flag local. Un cliente
 *      modificado (o un simple proxy) activa premium sin pagar.
 *
 * Corrección (RA4.c): la validación va en el SERVIDOR. El cliente envía el recibo/token de
 * compra firmado por la tienda; el servidor lo verifica contra la tienda y responde con un
 * derecho firmado. El cliente nunca decide por su cuenta.
 */
public class PurchaseManager {

    private final Context ctx;

    public PurchaseManager(Context ctx) {
        this.ctx = ctx;
    }

    /** VALIDACIÓN SOLO EN CLIENTE: confía en lo que diga la respuesta. */
    public boolean activarPremiumSiPagado(String respuestaCompra) {
        // Basta con que la respuesta contenga "valid": el cliente decide -> manipulable
        boolean valido = respuestaCompra != null && respuestaCompra.contains("\"purchase_valid\":true");
        if (valido) {
            SharedPreferences prefs = ctx.getSharedPreferences("compras", Context.MODE_PRIVATE);
            prefs.edit().putBoolean("premium", true).apply();
        }
        return valido;
    }

    public boolean esPremium() {
        SharedPreferences prefs = ctx.getSharedPreferences("compras", Context.MODE_PRIVATE);
        return prefs.getBoolean("premium", false);
    }
}
