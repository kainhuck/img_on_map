import exifread 

def exifread_infos(photo):
    f = open(photo, 'rb')
    tags = exifread.process_file(f)

    try:
        #拍摄时间
        EXIF_Date=tags["EXIF DateTimeOriginal"].printable
        #纬度
        LatRef=tags["GPS GPSLatitudeRef"].printable
        Lat=tags["GPS GPSLatitude"].printable[1:-1].replace(" ","").replace("/",",").split(",")
        Lat=float(Lat[0])+float(Lat[1])/60+float(Lat[2])/float(Lat[3])/3600
        if LatRef != "N":
            Lat=Lat*(-1)
        #经度
        LonRef=tags["GPS GPSLongitudeRef"].printable
        Lon=tags["GPS GPSLongitude"].printable[1:-1].replace(" ","").replace("/",",").split(",")
        Lon=float(Lon[0])+float(Lon[1])/60+float(Lon[2])/float(Lon[3])/3600
        if LonRef!="E":
            Lon=Lon*(-1)
        f.close()
    except :
        return "ERROR:请确保照片包含经纬度等EXIF信息。"
    else:
        return EXIF_Date,Lat,Lon

if __name__ == "__main__":
    print(exifread_infos('static/pic/test4.jpg'))
    import os
    
    for each in os.listdir('static/pic'):
        print(each)