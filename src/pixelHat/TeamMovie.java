package pixelHat;

import java.io.PrintStream;

public class TeamMovie {

	public static void main(String[] args) throws Exception {
		
		SpriteLoader sprites = new SpriteLoader();
		
		int [] ghostMap = {'#', 1, '*', 2, '+', 3};
		int [] letterMap = {'#', 4};		
		int [][] ghostA = sprites.colorSprite("ghosta", ghostMap);
		int [][] ghostB = sprites.colorSprite("ghostb", ghostMap);
		
		int [][] five = sprites.colorSprite("five", letterMap);
		int [][] eight = sprites.colorSprite("eight", letterMap);
		
		PrintStream ps = new PrintStream("teamGEN.txt");
		
		for(int y=22;y>1;--y) {
			HatFrame f = new HatFrame();
			if((y%2==0)) {
				f.drawSprite(0,  y+1, ghostA);
			} else {
				f.drawSprite(0,  y+1, ghostB);
			}
			f.drawSprite(18, y+2, five);
			f.drawSprite(28, y+2, eight);
			f.drawSprite(38, y+2, five);
			f.drawSprite(48, y+2, eight);
			ps.println("%");
			ps.println(f.toString());
		}
		
		for(int z=0;z<2;++z) {
			for(int x=0;x<63;++x) {		
				HatFrame f = new HatFrame();
				if((x%2==0)) {
					f.drawSprite(x+0,  1, ghostA);
				} else {
					f.drawSprite(x+0,  1, ghostB);
				}
				f.drawSprite(x+18, 2, five);
				f.drawSprite(x+28, 2, eight);
				f.drawSprite(x+38, 2, five);
				f.drawSprite(x+48, 2, eight);
				ps.println("%");
				ps.println(f.toString());
			}		
		}
		
		for(int y=1;y<23;++y) {
			HatFrame f = new HatFrame();
			if((y%2==0)) {
				f.drawSprite(0,  y+1, ghostA);
			} else {
				f.drawSprite(0,  y+1, ghostB);
			}
			f.drawSprite(18, y+2, five);
			f.drawSprite(28, y+2, eight);
			f.drawSprite(38, y+2, five);
			f.drawSprite(48, y+2, eight);
			ps.println("%");
			ps.println(f.toString());
		}
		
		ps.flush();
		ps.close();

	}

}
