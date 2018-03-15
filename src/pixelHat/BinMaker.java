package pixelHat;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class BinMaker {
	
	public static List<String> readFile(String name) throws IOException {
		List<String> lines = Files.readAllLines(Paths.get(name));
		List<String> ret = new ArrayList<String>();
		for(String line : lines) {
			int i = line.indexOf(";");
			if(i>=0) {
				line = line.substring(0,i);
			}
			line = line.trim();
			if(!line.isEmpty()) ret.add(line);
		}
		return ret;
	}
	
	public static byte[] fourByteNumber(long number) {
		byte [] ret = new byte[4];
		ret[3] = (byte) ((number>>24) & 0xFF);
		ret[2] = (byte) ((number>>16) & 0xFF);
		ret[1] = (byte) ((number>>8) & 0xFF);
		ret[0] = (byte) ((number) & 0xFF);
		return ret;
	}

	public static void main(String[] args) throws Exception {
		
		List<String> lines = readFile("master.txt");
		if(lines.size()>31) {
			throw new RuntimeException("Limited to 31 animations for now");
		}
		
		List<Movie> movies = new ArrayList<Movie>();
		
		for(String n : lines) {			
			Movie m = new Movie(n);
			movies.add(m);
		}
				
		OutputStream osA = new FileOutputStream("a.bin");
		OutputStream osB = new FileOutputStream("b.bin");
		
		// One sector for mapping
		
		int currentSector = 1;		
		for(int ent=0;ent<32;++ent) {
			byte [] data = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
			if(ent<movies.size()) {
				Movie m = movies.get(ent);
				for(int x=0;x<16;++x) {
					if(x<m.name.length()) {
						data[x] = (byte) m.name.charAt(x);
					} 
				}
				byte [] num = fourByteNumber(currentSector);
				data[12] = num[0];
				data[13] = num[1];
				data[14] = num[2];
				data[15] = num[3];
				currentSector = currentSector + 3 + m.frames.size()*2;	
			}
			osA.write(data);
			osB.write(data);
		}
		
				
		
		for(Movie m : movies) {
			// Write 1 sector info NUMFRAMES,DELAY
			byte [] data = fourByteNumber(m.frames.size());
			osA.write(data);
			osB.write(data);
			data = fourByteNumber(m.delay);
			osA.write(data);
			osB.write(data);
			for(int x=0;x<512-8;++x) {
				osA.write(0);
				osB.write(0);
			}
						
			// Write 2 sectors colors
			for(int x=0;x<256;++x) {
				if(x<m.colors.size()) {
					data = fourByteNumber(m.colors.get(x));
				} else {
					data = fourByteNumber(0);
				}
				osA.write(data);
				osB.write(data);
			}
			
			// Write 2 sectors per frame
			for(HatFrame f : m.frames) {
				int [] d = f.getBinary(true);
				for(int dd : d) {
					osA.write(dd);					
				}
				d = f.getBinary(false);
				for(int dd : d) {
					osB.write(dd);					
				}
			}
		}
		
		osA.flush();
		osA.close();
		osB.flush();
		osB.close();		

	}

}
