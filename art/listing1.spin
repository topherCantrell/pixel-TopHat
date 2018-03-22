    ' Read the first frame. We have to wait on this one.
    SD.readFileSectors(@frameBuffer,currentSector,2)
    currentSector := currentSector + 2 
    i := SD.waitForDone
    if i<>0
      showError(string("DISK ERROR 5"),i)

    repeat    
      
      ' Check for serial command here (removed for listing)      
                   
      ' Start loading the next frame in the back buffer
      i:=SD.waitForDone ' Hopefully this never waits (long delay coming up)
      if i<>0
        showError(string("DISK ERROR 6"),i)          
      SD.readFileSectors(@frameBuffer+bufferNextOffset,currentSector,2)
      currentSector := currentSector + 2          

      ' Make sure the two CPUs draw at the same time
      syncToOther
      
      ' Draw the current frame
      STRIPA.draw(2, @adjustedColors, @frameBuffer    +bufferOffset, pinS1, 256)
      STRIPB.draw(2, @adjustedColors, @frameBuffer+256+bufferOffset, pinS2, 256)
      STRIPC.draw(2, @adjustedColors, @frameBuffer+512+bufferOffset, pinS3, 256)
      STRIPD.draw(2, @adjustedColors, @frameBuffer+768+bufferOffset, pinS4, 256)  
      
      PauseMSec(currentDelay)
        
      ' Count the frames      
      currentFrameCount := currentFrameCount - 1
      if currentFrameCount == 0
        currentSector := currentSector - 2 ' Back up to start of next movie                   
        quit ' Break out of this loop

      ' Swap the back buffer and the current buffer
      i := bufferOffset
      bufferOffset := bufferNextOffset
      bufferNextOffset := i
      ' Back to top of this loop