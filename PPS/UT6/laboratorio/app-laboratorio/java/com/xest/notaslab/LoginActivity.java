package com.xest.notaslab;

import android.app.Activity;
import android.content.SharedPreferences;
import android.os.Bundle;

/**
 * Pantalla de login de NotasXest — versión de laboratorio VULNERABLE (PPS · UT6).
 *
 * Errores a encontrar:
 *   4) Almacenamiento inseguro: guarda token Y contraseña en claro en SharedPreferences.
 *      Lo correcto es Android Keystore / EncryptedSharedPreferences y NO guardar la
 *      contraseña nunca.
 *   5) La contraseña maestra de "modo demo" está incrustada como constante.
 */
public class LoginActivity extends Activity {

    // FUGA 5: contraseña de demostración incrustada
    private static final String DEMO_PASSWORD = "SuperSecreto123!";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        String usuario = "demo";
        String password = DEMO_PASSWORD;

        try {
            ApiClient api = new ApiClient();
            String respuesta = api.login(usuario, password);
            String token = extraerToken(respuesta);
            guardarSesion(usuario, password, token);
        } catch (Exception e) {
            // En laboratorio, ignoramos el error de red si el backend no está arrancado
        }
    }

    /** ALMACENAMIENTO INSEGURO: SharedPreferences en claro, incluida la contraseña. */
    private void guardarSesion(String usuario, String password, String token) {
        SharedPreferences prefs = getSharedPreferences("sesion", MODE_PRIVATE);
        SharedPreferences.Editor ed = prefs.edit();
        ed.putString("usuario", usuario);
        ed.putString("password", password);   // NUNCA se guarda una contraseña en claro
        ed.putString("auth_token", token);
        ed.apply();
    }

    private String extraerToken(String json) {
        int i = json.indexOf("\"token\":\"");
        if (i < 0) return "";
        int j = json.indexOf('"', i + 9);
        return json.substring(i + 9, j);
    }
}
