package pixelHat;

import java.io.PrintStream;
import java.util.Random;

public class SparkleMovie {

	public static void main(String[] args) throws Exception {
		
		Random r = new Random();
		
		// 1831 possible
		// Ten frames per second
		// Twenty seconds = 200 frames
		
		// 8 fade on
		// 8 hold
		// 8 fade out
		
		// 300 pixel events
		
		int [][] pixels = new int[200][1831];
		
		for(int z=0;z<2000;++z) {			
			outer:
			while(true) {
				int color = r.nextInt(6)+1; // 1..7
				int pix = r.nextInt(1831);
				int sf = r.nextInt(200-24);
				
				System.out.println(pix+" "+color+" "+sf);
				for(int g=sf;g<sf+24;++g) {
					if(pixels[g][pix]!=0) {
						continue outer;
					}
				}
				for(int g=0;g<8;++g) {
					pixels[sf+g][pix] = color*8+(7-g)+1; // Fade in
				}
				for(int g=0;g<8;++g) {
					pixels[sf+g+8][pix] = color*8+1; // Hold
				}
				for(int g=0;g<8;++g) {
					pixels[sf+g+16][pix] = color*8+g+1; // Fade on
				}
				break;
			}
		}
		
		int max = 0;
		for(int z=0;z<200;++z) {
			int cnt = 0;
			for(int x=0;x<1831;++x) {
				if(pixels[z][x]!=0) ++cnt;
			}
			System.out.println(z+" "+cnt);
			if(cnt>max) max=cnt;
		}
		
		PrintStream ps = new PrintStream("sparkGEN.txt");
		
		for(int[] pix : pixels) {
			HatFrame f = new HatFrame();
			for(int p=0;p<1831;++p) {
				if(pix[p]!=0) {
					f.setPixel(p,pix[p]);
				}
			}
			ps.println("%");
			ps.println(f.toString());
		}
		
		ps.flush();
		ps.close();
		

	}

}
