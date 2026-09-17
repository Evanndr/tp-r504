import java.io.*;
import java.net.*;

public class ServeurUDP 
{
    public static void main(String[] args) 
    {
        try (DatagramSocket serveurSock = new DatagramSocket(1234)) 
        {
            System.out.println("Serveur UDP démarré sur le port 1234...");
            while (true) 
            {
                System.out.println("-Waiting data");
                DatagramPacket packet = new DatagramPacket(new byte[1024], 1024);
                serveurSock.receive(packet);
                String str = new String(packet.getData(), 0, packet.getLength());
                System.out.println("str=" + str);
                InetAddress clientAddr = packet.getAddress();
                serveurSock.send(packet);
                System.out.println("Réponse envoyée au client.");
            }
        } 
        catch (IOException e) 
        {
            System.err.println("Erreur");
            e.printStackTrace();
        }
    }
}

