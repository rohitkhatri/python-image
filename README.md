# Python Image

**Requirements:**

* Python 3
* requests
* Pillow

## Usage

```python
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
```
## Response

```python
{
  'succeeded':[
    {
      'mime':'image/png',
      'size':58910,
      'ratio':100.0,
      'url':'http://rohitkhatri.com/assets/profile-photo.png',
      'width':152,
      'height':152
    },
    {
      'mime':'image/jpeg',
      'size':50426,
      'ratio':100.0,
      'url':'http://rohitkhatri.com/assets/photo1-sm.jpg',
      'width':152,
      'height':152
    },
    {
      'mime':'image/jpeg',
      'size':40794,
      'ratio':100.0,
      'url':'http://rohitkhatri.com/assets/photo2-sm.jpg',
      'width':152,
      'height':152
    },
    {
      'mime':'image/jpeg',
      'size':53899,
      'ratio':100.0,
      'url':'http://rohitkhatri.com/assets/photo3-sm.jpg',
      'width':152,
      'height':152
    },
    {
      'mime':'image/png',
      'size':23312,
      'ratio':100.0,
      'url':'http://rohitkhatri.com/assets/mikey-ahdoot.png',
      'width':104,
      'height':104
    },
    {
      'mime':'image/png',
      'size':26538,
      'ratio':100.0,
      'url':'http://rohitkhatri.com/assets/benny-schafier.png',
      'width':104,
      'height':104
    },
    {
      'mime':'image/png',
      'size':7782,
      'ratio':100.0,
      'url':'http://rohitkhatri.com/assets/b-west-interactive.png',
      'width':104,
      'height':104
    }
  ],
  'failed':[]
}
```