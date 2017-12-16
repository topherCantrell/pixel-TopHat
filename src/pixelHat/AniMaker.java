package pixelHat;

import java.awt.BorderLayout;
import java.awt.Color;

import javax.swing.JFrame;

public class AniMaker {
	
	public static void main(String[] args) {
	
		BodyPixels cont = new BodyPixels();
		Color [] c = {Color.BLACK, Color.RED, Color.GREEN, Color.BLUE, Color.WHITE};
		cont.colorPalette = c;
		
		cont.pixels[0][0] = 1;
		cont.pixels[1][1] = 2;
		cont.pixels[2][2] = 3;
		cont.pixels[3][3] = 4;		
		
		JFrame frame = new JFrame("AniMaker");
			
		frame.getContentPane().add(cont,BorderLayout.CENTER);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.pack();
		frame.setVisible(true);		

	}

}
