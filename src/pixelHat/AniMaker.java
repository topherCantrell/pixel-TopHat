package pixelHat;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.FlowLayout;
import java.io.IOException;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JTextField;

public class AniMaker {
	
	public static void main(String[] args) throws IOException {
		
		FrameFile ff = new FrameFile("sampleSave.txt");
		
		JPanel controls = new JPanel(new FlowLayout());
		JButton frev = new JButton("<<");
		JButton rev = new JButton("<");
		JButton forw = new JButton(">");
		JButton fforw = new JButton(">>");
		
		JTextField frameNumber = new JTextField("");
		
		
		controls.add(new JButton("Save"));
		controls.add(new JButton("Cancel"));		
		
		BodyPixels cont = new BodyPixels();
		Color [] c = {Color.BLACK, Color.RED, Color.GREEN, Color.BLUE, Color.WHITE};
		cont.colorPalette = c;		
		cont.pixels[0][0] = 1;
		cont.pixels[1][1] = 2;
		cont.pixels[2][2] = 3;
		cont.pixels[3][3] = 4;		
		
		BrimPixels brim = new BrimPixels();
		brim.colorPalette = c;
		brim.pixels[0][0] = 4;
		brim.pixels[1][1] = 3;
		brim.pixels[2][2] = 2;
		brim.pixels[3][3] = 1;		
		
		JPanel pixels = new JPanel(new BorderLayout());
		pixels.add(cont,BorderLayout.CENTER);
		pixels.add(brim,BorderLayout.SOUTH);		
		
		JPanel mainApp = new JPanel(new BorderLayout());
		mainApp.add(pixels,BorderLayout.CENTER);
		mainApp.add(controls,BorderLayout.SOUTH);
			
		JFrame frame = new JFrame("AniMaker");
			
		frame.getContentPane().add(mainApp, BorderLayout.CENTER);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.pack();
		frame.setVisible(true);		

	}

}
