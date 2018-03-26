package pixelHat;

import java.io.PrintStream;

public class InvadersMovie {

	public static void main(String[] args) throws Exception {
		
		SpriteLoader sprites = new SpriteLoader();
				
		int [] invaderMap = {'#', 1};
		int [][][] invaders = {
			sprites.doubler(sprites.colorSprite("invaderA1", invaderMap)),
			sprites.doubler(sprites.colorSprite("invaderA2", invaderMap)),	
			sprites.doubler(sprites.colorSprite("invaderB1", invaderMap)),	
			sprites.doubler(sprites.colorSprite("invaderB2", invaderMap)),	
			sprites.doubler(sprites.colorSprite("invaderC1", invaderMap)),	
			sprites.doubler(sprites.colorSprite("invaderC2", invaderMap))
		};
				
		PrintStream ps = new PrintStream("invGEN.txt");
		
		for(int y=-15;y<0;++y) {
			HatFrame f = new HatFrame();
			int ofs = y%2;
			if(ofs<0) ofs=-ofs;
			f.drawSprite(0, y, invaders[2+ofs]);	
			f.drawSprite(35,y, invaders[4+ofs]);
			ps.println("%");
			ps.println(f.toString());
		}
		
		
		for(int x=0;x<64;++x) {
			HatFrame f = new HatFrame();
			int ofs = x%2;
			if(ofs<0) ofs=-ofs;
			f.drawSprite(x+0, 0, invaders[2+ofs]);	
			f.drawSprite(x+35,0, invaders[4+ofs]);
			ps.println("%");
			ps.println(f.toString());
		}
		
		for(int y=0;y>-16;--y) {
			HatFrame f = new HatFrame();
			int ofs = y%2;
			if(ofs<0) ofs=-ofs;
			f.drawSprite(0, y, invaders[2+ofs]);	
			f.drawSprite(35,y, invaders[4+ofs]);
			ps.println("%");
			ps.println(f.toString());
		}
				
		ps.flush();
		ps.close();

	}

}
