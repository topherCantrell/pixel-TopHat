package pixelHat;

import java.io.PrintStream;

public class RedBlueMovie {

	public static void main(String[] args) throws Exception {
			
		SpriteLoader sprites = new SpriteLoader();
		
		PrintStream ps = new PrintStream("redBlueGEN.txt");
		
		int [] letterMap =      {'#', 1};
		
		int [][] letterG = sprites.colorSprite("letterG", letterMap);
		int [][] lettero = sprites.colorSprite("lettero", letterMap);
				
		int [][] five = sprites.colorSprite("five", letterMap);
		int [][] eight = sprites.colorSprite("eight", letterMap);
		
		for(int i=0;i<10;++i) {
		for(int x=0;x<63;x=x+2) {
			HatFrame f = new HatFrame();
			f.drawSprite(x+0, 2+1, letterG);
			f.drawSprite(x+13, 2+5, lettero);
			f.drawSprite(x+23, 2+0, five);
			f.drawSprite(x+33, 2+0, eight);
			f.drawSprite(x+43, 2+0, five);
			f.drawSprite(x+53, 2+0, eight);
						
			ps.println("%");
			ps.println(f.toString());
		}
		}	
		
		ps.println();
		ps.flush();
		ps.close();			
		
	}

}
