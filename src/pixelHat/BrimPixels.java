package pixelHat;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;

import javax.swing.JPanel;

public class BrimPixels extends JPanel implements PixelContainer {
	
	private static final long serialVersionUID = 1L;
	
	public BrimPixels() {		
		setPreferredSize(new Dimension(64*8*2+50,8*8*2+50));
	}
	
	Color[] colorPalette;
	int [][] pixels = new int[8][64];
	
	@Override
	public void paint(Graphics g) {
		super.paint(g);
		
		g.setColor(Color.RED);
		g.drawLine(25+32*8*2, 25+0, 25+32*8*2, 25+8*8*2);		
		
		for(int y=0;y<8;++y) {
			for(int x=0;x<64;++x) {
				g.setColor(colorPalette[pixels[y][x]]);
				g.fillRect(25+8*2*x+2, 25+8*2*y+2, 12, 12);
			}
		}
		
	}
	
	@Override
	public void setPixel(int x, int y, int color) {
		pixels[y][x] = color;
	}

}
