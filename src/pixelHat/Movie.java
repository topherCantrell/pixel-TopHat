package pixelHat;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Movie {
	
	int delay;
	String name;	
	List<Long> colors = new ArrayList<Long>();
	
	List<HatFrame> frames = new ArrayList<HatFrame>();
	
	public Movie(String fileName) throws IOException {
		int i = fileName.indexOf(".");
		if(i<0) i = fileName.length();
		name = fileName.substring(0,i);
		if(i>15) {
			throw new RuntimeException("Name must be less than 16 characters: "+name);
		}		
		List<String> lines = BinMaker.readFile(fileName);
		
		int pos = 0;		
		while(true) {			
			String g = lines.get(pos++);
			if(g.startsWith("%")) break;
			if(g.startsWith("#")) {
				g = g.replaceAll("_","");
				colors.add(Long.parseLong(g.substring(1),16));
			}
			if(g.startsWith("delay ")) {
				delay = Integer.parseInt(g.substring(6).trim());
			}
		}
		
		String fs = "";
		while(true) {			
			if(pos==lines.size() || lines.get(pos).startsWith("%")) {
				HatFrame f = new HatFrame();
				//System.out.println(fs);
				f.fromString(fs);
				frames.add(f);
				fs = "";
				++pos;
			}
			if(pos>=lines.size()) break;
			fs = fs + lines.get(pos++);
		}
		
		System.out.println("Movie '"+name+"' delay="+delay+" colors="+colors.size()+" frames="+frames.size());		
		
	}

}
