package pixelHat;

import java.io.IOException;
import java.io.PrintStream;

public class StillMovie {

	public static void main(String[] args) throws IOException {
		
		SpriteLoader sprites = new SpriteLoader();
		
		int [] ghostMap = {'#', 1, '*', 2};		
		int [][] ghost = sprites.colorSprite("ghostc", ghostMap);
		
		int [] pacMap = {'#', 3};
		int [][] pac = sprites.colorSprite("pac2", pacMap);
		
		HatFrame f = new HatFrame();
		
		f.drawSprite(32-15+32, 1, ghost);		
		f.drawSprite(32+1+32,2,pac);
		
		f.setRing(0, 4);
		f.setRing(1, 5);
		f.setRing(2, 4);
		f.setRing(3, 5);
		f.setRing(4, 4);
		f.setRing(5, 5);
		f.setRing(6, 4);
		f.setRing(7, 5);
		f.setRing(8, 4);
		f.setRing(9, 5);
		f.setRing(10, 4);
		f.setRing(11, 5);
		
		f.setRing(28, 4);
		f.setRing(29, 5);
		f.setRing(30, 4);
		f.setRing(31, 5);
		f.setRing(32, 4);
		f.setRing(33, 5);
		f.setRing(34, 4);
		f.setRing(35, 5);
				
		PrintStream ps = new PrintStream("stillGEN.txt");
		ps.println(f.toString());			
		
		ps.flush();
		ps.close();

	}

}
