import mc

imageName="Screen1.png"

def switchImage():
	global imageName

	if imageName == "Screen2.png":
		imageName = "Screen1.png"
	else:
		imageName = "Screen2.png"

	image = mc.GetWindow(14000).GetImage(120)
	image.SetTexture(imageName)
