package pixelHat;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SpriteLoader {
	
	Map<String,List<String>> sprites = new HashMap<String,List<String>>();
	
	public SpriteLoader() throws IOException {
		
		List<String> lines = Files.readAllLines(Paths.get("Sprites.txt"));
		
		List<String> currentSprite = new ArrayList<String>();
		String currentName = null;
		
		for(String line : lines) {
			line = line.trim();
			if(line.isEmpty()) continue;
			if(line.startsWith("-")) {
				if(currentName!=null) {
					sprites.put(currentName, currentSprite);
				}
				currentName = line.substring(1);
				currentSprite = new ArrayList<String>();
				continue;
			}
			currentSprite.add(line);
		}
		
		if(currentName!=null) {
			sprites.put(currentName, currentSprite);
		}
		
	}
	
	int [][] colorSprite(String name, int [] colorMap) {
		List<String> sprite = sprites.get(name);
		int [][] ret = new int[sprite.size()][];
		for(int y=0;y<sprite.size();++y) {
			String s = sprite.get(y);
			ret[y] = new int[s.length()];
			for(int x=0;x<s.length();++x) {
				char c = s.charAt(x);
				int v = 0;
				if(c=='.' || c==' ') {
					v = 0;
				} else {
					for(int z=0;z<colorMap.length;z=z+2) {
						if(colorMap[z]==c) {
							v = colorMap[z+1];
							break;
						}
					}					
				}
				ret[y][x] = v;
			}
		}
		return ret;
	}

	public int[][] doubler(int[][] colorSprite) {
		int [][] ret = new int[colorSprite.length*2][];
		for(int y=0;y<colorSprite.length;++y) {
			int [] drow = new int[colorSprite[y].length*2];
			for(int x=0;x<colorSprite[y].length;++x) {
				drow[x*2+0] = colorSprite[y][x];
				drow[x*2+1] = colorSprite[y][x];
			}
			ret[y*2+0] = drow;
			ret[y*2+1] = drow;
		}
		return ret;
	}
	
	public int[][] flipLeftRight(int[][] colorSprite) {
		int [][] ret = new int[colorSprite.length][colorSprite[0].length];
		for(int y=0;y<colorSprite.length;++y) {
			for(int x=0;x<colorSprite[y].length;++x) {
				ret[y][colorSprite[y].length-x-1] = colorSprite[y][x];
			}
		}
		return ret;
	}

	public int[][] flipUpDown(int[][] colorSprite) {
		int [][] ret = new int[colorSprite.length][];
		int i = ret.length-1;
		for(int x=0;x<colorSprite.length;++x) {
			ret[i] = colorSprite[x];
			--i;
		}		
		return ret;
	}

}
