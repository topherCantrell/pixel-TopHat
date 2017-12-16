package pixelHat;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;

import javax.swing.JPanel;

public class BodyPixels extends JPanel {

	private static final long serialVersionUID = 1L;
	
	public BodyPixels() {		
		setPreferredSize(new Dimension(64*8*2,16*8*2));
	}
	
	Color[] colorPalette;
	int [][] pixels = new int[16][64];
	
	@Override
	public void paint(Graphics g) {
		super.paint(g);
		
		g.setColor(Color.RED);
		g.drawLine(32*8*2, 0, 32*8*2, 16*8*2);
		g.drawLine(0, 8*8*2, 64*8*2, 8*8*2);
		
		for(int y=0;y<16;++y) {
			for(int x=0;x<64;++x) {
				g.setColor(colorPalette[pixels[y][x]]);
				g.fillRect(8*2*x+2, 8*2*y+2, 12, 12);
			}
		}
		
	}

}
