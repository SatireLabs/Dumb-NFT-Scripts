import glob
import PIL
from PIL import Image
import random

how_many = 10
list_fh = []
list_f = []
list_m = []
list_e = []
list_mp = []
list_h = []
for x in glob.glob('layers-infinite/m/Facial Hair/*'):
    list_fh.append(x)
for x in glob.glob('layers-infinite/m/faces-m/*'):
    list_f.append(x)
for x in glob.glob('layers-infinite/m/Mouth/*'):
    list_m.append(x)
for x in glob.glob('layers-infinite/m/Mouth Prop/*'):
    list_mp.append(x)
for x in glob.glob('layers-infinite/m/Eyes/*'):
    list_e.append(x)
for x in glob.glob('layers-infinite/m/Hair/*'):
    list_h.append(x)
w=600
h=600
n=0
dumb = Image.open("layers-infinite/dumb-real.png")
while n < how_many:
    fn = (random.choice(list_f))
    fhn = (random.choice(list_fh))
    mn = (random.choice(list_m))
    mpn = (random.choice(list_mp))
    en = (random.choice(list_e))
    hhn = (random.choice(list_h))
    f = Image.open(fn).resize((w,h),0).convert("RGBA")
    fh = Image.open(fhn).resize((w,h),0).convert("RGBA")
    m = Image.open(mn).resize((w,h),0).convert("RGBA")
    mp = Image.open(mpn).resize((w,h),0).convert("RGBA")
    e = Image.open(en).resize((w,h),0).convert("RGBA")
    hh = Image.open(hhn).resize((w,h),0).convert("RGBA")
    f.paste(fh, (0, 0),fh)
    f.paste(m, (0, 0),m)
    f.paste(mp, (0, 0),mp)
    f.paste(e, (0, 0),e)
    f.paste(hh, (0, 0),hh)
    pic_l,pic_u,pic_r,pic_d=f.getbbox()
    punked = f.crop((0,pic_u,pic_r,600))
    black = Image.new('RGBA', punked.size)
    myImage = Image.composite(punked, black, punked)
    punked = punked.crop((0,0,pic_r,600))
    punked
    new_size = (600,punked.size[1]+120)
    new_im = Image.new("RGBA", new_size)
    new_im.paste(punked,(0,120))
    new_im.paste(dumb,(0,0))
    f = new_im

    pic_l,pic_u,pic_r,pic_d=f.getbbox()
    punked = f.crop((0,pic_u,pic_r,pic_d))
    black = Image.new('RGBA', punked.size)
    myImage = Image.composite(punked, black, punked)
    f = punked.crop((pic_l,pic_u,pic_r,pic_d))

    f.save("layers-infinite/infinite-sample/m/{}_{}_{}_{}_{}_{}.png".format(fn.split("/")[-1][:-4], hhn.split("/")[-1][:-4], en.split("/")[-1][:-4],mn.split("/")[-1][:-4],mpn.split("/")[-1][:-4],fhn.split("/")[-1][:-4]))

    del f
    del fh
    del m
    del mp
    del e
    del hh
    n+=1