package com.xest.notaslab;

import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;

/**
 * Cliente HTTP de NotasXest — versión de laboratorio VULNERABLE (PPS · UT6).
 *
 * Errores a encontrar en el análisis estático:
 *   1) URL base en HTTP en claro (usesCleartextTraffic + http://).
 *   2) Clave de API incrustada en el binario (secreto en el código).
 *   3) Credencial de servicio "oculta" en una constante — la ofuscación no protege esto.
 */
public class ApiClient {

    // FUGA 1: URL interna del backend, en claro
    public static final String BASE_URL = "http://api.xest.local:8090";

    // FUGA 2: clave de API incrustada — jadx/grep la sacan en segundos
    private static final String API_KEY = "xk_live_9f2c7b41ad554e0e8d3b6a1029f4c7de";

    // FUGA 3: credencial del bucket de sincronización, "escondida" partida en dos
    private static final String SYNC_SECRET_A = "AKIAX3STLAB";
    private static final String SYNC_SECRET_B = "0RQEXAMPLEK3Y";

    public String login(String usuario, String password) throws Exception {
        URL url = new URL(BASE_URL + "/login");
        HttpURLConnection con = (HttpURLConnection) url.openConnection();
        con.setRequestMethod("POST");
        con.setRequestProperty("X-Api-Key", API_KEY);
        con.setRequestProperty("Content-Type", "application/json");
        con.setDoOutput(true);

        // La contraseña viaja en el cuerpo, sobre HTTP en claro
        String body = "{\"usuario\":\"" + usuario + "\",\"password\":\"" + password + "\"}";
        try (OutputStream os = con.getOutputStream()) {
            os.write(body.getBytes("UTF-8"));
        }
        return leer(con);
    }

    public String sincronizarNotas(String token) throws Exception {
        URL url = new URL(BASE_URL + "/sync");
        HttpURLConnection con = (HttpURLConnection) url.openConnection();
        con.setRequestProperty("X-Api-Key", API_KEY);
        con.setRequestProperty("Authorization", "Bearer " + token);
        con.setRequestProperty("X-Sync-Secret", SYNC_SECRET_A + SYNC_SECRET_B);
        return leer(con);
    }

    private String leer(HttpURLConnection con) throws Exception {
        java.io.BufferedReader r = new java.io.BufferedReader(
                new java.io.InputStreamReader(con.getInputStream()));
        StringBuilder sb = new StringBuilder();
        String linea;
        while ((linea = r.readLine()) != null) sb.append(linea);
        r.close();
        return sb.toString();
    }
}
