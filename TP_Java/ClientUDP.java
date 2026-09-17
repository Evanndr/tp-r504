import java.io.*;
import java.net.*;

public class ClientUDP
{
	public static void main (String[] args)
	{
		try 
		{
			InetAddress addr = InetAddress.getLocalHost();
			System.out.println("adresse = " + addr.getHostAddress());
			String s = "Hello World";
			byte[] data = s.getBytes();
			DatagramPacket packetToSend = new DatagramPacket(data, data.length, addr, 1234);
			DatagramSocket sock = new DatagramSocket();
			sock.send(packetToSend);
			System.out.println("Message envoyé : " + s);
			System.out.println("Attente du retour serveur...");
			byte[] responseBuffer = new byte[1024];
			DatagramPacket packetFromServer = new DatagramPacket(responseBuffer, responseBuffer.length);
			sock.receive(packetFromServer);
			String str = new String(packetFromServer.getData(), 0, packetFromServer.getLength());
			System.out.println("Message du serveur = " + str); 
			sock.close();
		}
		catch( Exception a )
		{
			System.out.println("Erreur.");
		}
	}
}

