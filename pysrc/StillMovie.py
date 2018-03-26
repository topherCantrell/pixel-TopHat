import SpriteLoader
import HatFrame

sprites = SpriteLoader.SpriteLoader()

ghostMap = ['#', 1, '*', 2]
ghost = sprites.colorSprite("ghostc",ghostMap)

pacMap = ['#', 3]
pac = sprites.colorSprite("pac2", pacMap)

f = HatFrame.HatFrame()