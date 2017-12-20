package pixelHat;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class FrameFile {
	
	List<int[]> frames = new ArrayList<int[]>();
	List<String> lines;
	
	public FrameFile(String filename) throws IOException {
		lines = Files.readAllLines(Paths.get(filename));
		int[] currentFrame = null;
		for(String s : lines) {
			if(s.trim().startsWith(";")) continue; // Allow comments
			if(s.trim().isEmpty()) continue; // Allow blank lines
			if(s.trim().startsWith("----")) continue; // Allow graphical grid
			if(s.trim().startsWith("#####")) {
				currentFrame = new int[32*8*6];
				frames.add(currentFrame);
				continue;
			}
			// TODO here is where we process the data
		}
	}
	
	public int [] getFrame(int index) {
		return frames.get(index);
	}
	
	public void setFrame(int index, int [] data) {
		frames.set(index,data);
		// TODO save the file
		// TODO there is some ASCII art here ... the circle at the top.
		// TODO persist the comments
	}

}
