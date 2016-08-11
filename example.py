from ImageInfo.ImageThread import get_image_meta

urls = [
  "http://rohitkhatri.com/assets/profile-photo.png",
  "http://rohitkhatri.com/assets/photo1-sm.jpg",
  "http://rohitkhatri.com/assets/photo2-sm.jpg",
  "http://rohitkhatri.com/assets/photo3-sm.jpg",
  "http://rohitkhatri.com/assets/mikey-ahdoot.png",
  "http://rohitkhatri.com/assets/benny-schafier.png",
  "http://rohitkhatri.com/assets/b-west-interactive.png"
]

images = get_image_meta(urls)
print(images)