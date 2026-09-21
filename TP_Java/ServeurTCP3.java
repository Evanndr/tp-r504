import java.io.*;
import java.net.*;

public class ServeurTCP3
{
	public static void main (String[] args)
	{
		try 
		{
			ServerSocket socketserver = new ServerSocket( 2016 );
			System.out.println( "serveur en attente" );
			while (true)
			{
				Socket socket = socketserver.accept();
				DataInputStream dIn = new DataInputStream(socket.getInputStream() ); 
				System.out.println( "Connection d'un client" );
				String message = dIn.readUTF();
				System.out.println( "Message: " + message);
				socket.close();

				String rev = new StringBuilder(message).reverse().toString();
				Socket socket2 = new Socket( "localhost", 2017 );
				DataOutputStream dOut = new DataOutputStream( socket2.getOutputStream() );
				dOut.writeUTF(rev);
				dOut.flush();
				socket2.close();
			}
		}
		catch( Exception a )
		{
			System.out.println("Erreur.");
		}
	}
}




