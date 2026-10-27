// PPS UT1 · Validador de nombre de usuario — versión Java (MÁQUINA VIRTUAL / bytecode).
//
// Ejercicio PPS-E1: localiza PUNTO DE ENTRADA, SINK y VALIDACIÓN, y señala
// DÓNDE PUEDE FALLAR este modelo.
// Pista: el bytecode se decompila con facilidad (jadx, procyon); no confíes en
// "ocultar" secretos en el .class. Y la concatenación en SQL sigue siendo inyección.

import java.sql.*;

public class Validar {

    // VALIDACIÓN (débil): solo longitud.
    static boolean validarNombre(String nombre) {
        return nombre != null && nombre.length() > 0 && nombre.length() <= 32;
    }

    static void buscarUsuario(String nombre) throws SQLException {
        // PUNTO DE ENTRADA: 'nombre' viene del exterior.
        if (!validarNombre(nombre)) throw new IllegalArgumentException("nombre no válido");

        Connection con = DriverManager.getConnection("jdbc:sqlite::memory:");
        Statement st = con.createStatement();
        // SINK (SQL): concatenación directa -> inyección SQL.
        String consulta = "SELECT * FROM usuarios WHERE nombre = '" + nombre + "'";
        st.executeQuery(consulta);

        // "Secreto" en el binario: aparente ofuscación que jadx revela al instante.
        String apiKey = "LAB-DEMO-NO-REAL-1234";   // no confiar en la ofuscación
        System.out.println("acceso de " + nombre);
    }

    public static void main(String[] args) throws SQLException {
        buscarUsuario(args.length > 0 ? args[0] : "ana");
    }
}
