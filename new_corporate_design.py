from PIL import Image
import glob, os

def changeDesign(kachel=False):
  """This function changes the old CB corporate design to the new colors."""
  all_files = glob.glob("*.png")
  all_files.extend(glob.glob("*.jpg"))
  all_files.extend(glob.glob("*.jpeg"))
  all_files.extend(glob.glob("*.PNG"))
  all_files.extend(glob.glob("*.JPG"))
  all_files.extend(glob.glob("*.JPEG"))

  for infile in all_files:
      file, ext = os.path.splitext(infile)
      im = Image.open(infile).convert('RGBA')
      
      width, height = im.size

      *rgb, _  = im.getpixel( (5,5) )

      if rgb == [255,204,51]:
        kachel=True
      if rgb == [255,255,255]:
        kachel=False

      # Process every pixel
      for y in range(height):
        if kachel:
          *rgb, _  = im.getpixel( (1,y) )
          if rgb == [255,255,255]:
            continue
        for x in range(width):
            *rgb, _  = im.getpixel( (x,y) )

            # if rgb == [51,51,51]:
            #   im.putpixel( (x,y), (0, 65, 75, _))

            #dark violet
            if rgb == [63,61,86]:
              im.putpixel( (x,y), (0, 65, 75, _))

            #light violet
            if rgb == [96,93,130] or rgb == [87,90, 136] or rgb == [87,90, 137]:
              im.putpixel( (x,y), (75, 120, 125, _))
            
            if kachel: 
              if rgb == [255,255,255]:
                im.putpixel( (x,y), (255, 233, 0, _))

              if rgb == [255,204,51]:
                im.putpixel( (x,y), (0, 65, 75, _))
            else:
              if rgb == [70,69,91]:
                im.putpixel( (x,y), (0, 60, 68, _))

              if rgb == [255,204,51]:
                im.putpixel( (x,y), (255, 233, 0, _))

      #display(im)

      try:
        im.save("./new/"+file+ext)
      except FileNotFoundError:
        os.mkdir("new")
        print("Folder ./new/ created")
        im.save("./new/"+file+ext)
        
def create_zip():
  !zip -r /content/new.zip /content/new
  from google.colab import files
  files.download("/content/new.zip")

def remove_all():
  !find . -name "*.png" -type f -delete
  !find . -name "*.PNG" -type f -delete
  !rm new.zip
