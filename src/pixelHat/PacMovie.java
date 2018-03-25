package pixelHat;

import java.io.IOException;
import java.io.PrintStream;
import java.util.Random;

public class PacMovie {
	
	static void setRings(HatFrame f) {
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
	}
	
	static int pacPos = -1;
	static String getPacImageName() {
		pacPos += 1;
		pacPos %= 4;
		switch(pacPos) {
		case 0:
			return "pac3";
		case 1:
			return "pac2";
		case 2:
			return "pac1";
		case 3:
			return "pac2";		
			default:
				return "?";
		}
	}
	
	static int ghostPos = -1;
	static String getBlueGhostImageName() {
		ghostPos += 1;
		ghostPos %= 2;
		switch(ghostPos) {
		case 0:
			return "ghostc";
		case 1:
			return "ghostd";
			default:
				return "??";
		}
	}
	static String getRedGhostImageName() {
		ghostPos += 1;
		ghostPos %= 2;
		switch(ghostPos) {
		case 0:
			return "ghosta";
		case 1:
			return "ghostb";
			default:
				return "??";
		}
	}
	
	static Random rand = new Random();
	
	static void drawFlasher(HatFrame f, boolean in, int count) {
		
		f.setSideBrimPixel(0, 7, rand.nextInt(3)+12);
		f.setSideBrimPixel(0, 8, rand.nextInt(3)+12);
		f.setSideBrimPixel(1, 7, rand.nextInt(3)+12);
		f.setSideBrimPixel(1, 8, rand.nextInt(3)+12);
		if(count>0) {
			f.setSideBrimPixel(0, 6, rand.nextInt(3)+12);
			f.setSideBrimPixel(0, 9, rand.nextInt(3)+12);
			f.setSideBrimPixel(1, 6, rand.nextInt(3)+12);
			f.setSideBrimPixel(1, 9, rand.nextInt(3)+12);
		}
		if(count>1) {
			f.setSideBrimPixel(0, 5, rand.nextInt(3)+12);
			f.setSideBrimPixel(0, 4, rand.nextInt(3)+12);
			f.setSideBrimPixel(0, 10, rand.nextInt(3)+12);
			f.setSideBrimPixel(0, 11, rand.nextInt(3)+12);
			f.setSideBrimPixel(1, 5, rand.nextInt(3)+12);
			f.setSideBrimPixel(1, 4, rand.nextInt(3)+12);
			f.setSideBrimPixel(1, 10, rand.nextInt(3)+12);
			f.setSideBrimPixel(1, 11, rand.nextInt(3)+12);
		}
		if(count>2) {
			f.setSideBrimPixel(0, 3, rand.nextInt(3)+12);
			f.setSideBrimPixel(0, 2, rand.nextInt(3)+12);
			f.setSideBrimPixel(0, 12, rand.nextInt(3)+12);
			f.setSideBrimPixel(0, 13, rand.nextInt(3)+12);
			f.setSideBrimPixel(1, 3, rand.nextInt(3)+12);
			f.setSideBrimPixel(1, 2, rand.nextInt(3)+12);
			f.setSideBrimPixel(1, 12, rand.nextInt(3)+12);
			f.setSideBrimPixel(1, 13, rand.nextInt(3)+12);
		}
		if(count>3) {
			f.setSideBrimPixel(0, 0, rand.nextInt(3)+12);
			f.setSideBrimPixel(0, 1, rand.nextInt(3)+12);
			f.setSideBrimPixel(0, 14, rand.nextInt(3)+12);
			f.setSideBrimPixel(0, 15, rand.nextInt(3)+12);
			f.setSideBrimPixel(1, 0, rand.nextInt(3)+12);
			f.setSideBrimPixel(1, 1, rand.nextInt(3)+12);
			f.setSideBrimPixel(1, 14, rand.nextInt(3)+12);
			f.setSideBrimPixel(1, 15, rand.nextInt(3)+12);
		}
		
		if(in) {
			for(int x=2;x<50-count;++x) {
				for(int y=0;y<16;++y) {
					f.setSideBrimPixel(x, y, 0);
				}
			}
		} else {
			for(int x=2;x<count;++x) {
				for(int y=0;y<16;++y) {
					f.setSideBrimPixel(x, y, 0);
				}
			}
		}
	}

	public static void main(String[] args) throws IOException {
		
		SpriteLoader sprites = new SpriteLoader();
		
		int [] blueGhostMap =      {'#', 1, '*', 2};
		int [] blueGhostFlashMap = {'#', 6, '*', 7};
		int [] redGhostMap =       {'#', 8, '*', 10, '+', 11};	
		int [] cyanGhostMap =      {'#', 9, '*', 10, '+', 11};
		int [] pacMap =            {'#', 3};
		
		PrintStream ps = new PrintStream("pacGEN.txt");
		
		// pac chases blue ghosts once around
		
		// blue ghosts flash once around
		
		// non-blue ghosts chases pac around once the other way
		
		// Add warp line at start and end
		
		int pacX = 32+1+2;
		int ghost1X =  32-15+2;
		int ghost2X =  ghost1X - 16;		
		
		for(int i=0;i<64;++i) {
			HatFrame f = new HatFrame();
			setRings(f);
			f.drawSprite(pacX, 2, sprites.colorSprite(getPacImageName(), pacMap));
			pacX = pacX - 1;			
			String g = getBlueGhostImageName();
			f.drawSprite(ghost1X, 1, sprites.colorSprite(g, blueGhostMap));			
			ghost1X = ghost1X - 1;
			f.drawSprite(ghost2X, 1, sprites.colorSprite(g, blueGhostMap));			
			ghost2X = ghost2X - 1;
			
			drawFlasher(f,true,i);
			
			ps.println("%");
			ps.println(f.toString());			
		}
		
		int [] gm = blueGhostMap;
		int flashTimer = 0;
		
		for(int i=0;i<64;++i) {
			HatFrame f = new HatFrame();
			setRings(f);			
			f.drawSprite(pacX, 2, sprites.colorSprite(getPacImageName(), pacMap));
			pacX = pacX - 1;	
			String g = getBlueGhostImageName();
			f.drawSprite(ghost1X, 1, sprites.colorSprite(g, gm));
			ghost1X = ghost1X - 1;
			f.drawSprite(ghost2X, 1, sprites.colorSprite(g, gm));
			ghost2X = ghost2X - 1;			
			flashTimer = flashTimer + 1;
			if(flashTimer == 5) {
				if(gm==blueGhostMap) {
					gm = blueGhostFlashMap;
				} else {
					gm = blueGhostMap;
				}
				flashTimer = 0;
			}
			
			ps.println("%");
			ps.println(f.toString());			
		}
		
		for(int i=0;i<64;++i) {
			HatFrame f = new HatFrame();
			setRings(f);			
			f.drawSprite(pacX, 2, sprites.flipLeftRight(sprites.colorSprite(getPacImageName(), pacMap)));
			pacX = pacX + 1;	
			String g = getRedGhostImageName();
			f.drawSprite(ghost1X, 1, sprites.colorSprite(g, redGhostMap));
			ghost1X = ghost1X + 1;
			f.drawSprite(ghost2X, 1, sprites.colorSprite(g, cyanGhostMap));
			ghost2X = ghost2X + 1;
			
			drawFlasher(f,false,i-8);
			
			ps.println("%");
			ps.println(f.toString());			
		}
		
		ps.println();
		ps.flush();
		ps.close();
		

	}

}
