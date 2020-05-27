from django.db import models




class Post(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=100)
    day = models.DateField()
    overview = models.TextField()

    def __str__(self):
        return self.title



class Bio(models.Model):
    titlebio = models.CharField(max_length=100)
    aboutimg = models.ImageField()
    about = models.TextField()


    def __str__(self):
        return self.titlebio
    


class Patios(models.Model):
    p_title = models.CharField(max_length=50)
    p_pic= models.IntegerField()
    p_label= models.FileField()


    def __str__(self):
        return self.p_title


class Patiosimage(models.Model):
    patios = models.ForeignKey(Patios, default=None, on_delete=models.CASCADE)
    p_images = models.FileField(upload_to = 'images/')
    
    def __str__(self):
        return self.patios.p_title




class Resins(models.Model):
    r_title = models.CharField(max_length=50)
    r_pic= models.IntegerField()
    r_label= models.FileField()


    def __str__(self):
        return self.r_title

class Resinsimage(models.Model):
    resins = models.ForeignKey(Resins, default=None, on_delete=models.CASCADE)
    r_images = models.FileField(upload_to = 'images/')
    
    def __str__(self):
        return self.resins.r_title


class Tarmac(models.Model):
    t_title = models.CharField(max_length=50)
    t_pic= models.IntegerField()
    t_label= models.FileField()



    def __str__(self):
        return self.t_title


class Tarmacimage(models.Model):
    tarmac = models.ForeignKey(Tarmac, default=None, on_delete=models.CASCADE)
    t_images = models.FileField(upload_to = 'images/')
    
    def __str__(self):
        return self.tarmac.t_title


class Fencing(models.Model):
    f_title = models.CharField(max_length=50)
    f_pic = models.IntegerField()
    f_label= models.FileField()

    def __str__(self):
        return self.f_title



class Fencingimage(models.Model):
    fencing = models.ForeignKey(Fencing, default=None, on_delete=models.CASCADE)
    f_images = models.FileField(upload_to = 'images/')
    
    def __str__(self):
        return self.fencing.f_title

class BlockPaving(models.Model):
    b_title = models.CharField(max_length=50)
    b_num_pic= models.IntegerField()
    b_label= models.FileField()


    def __str__(self):
        return self.b_title

class BlockPavingimage(models.Model):
    blockpaving = models.ForeignKey(BlockPaving, default=None, on_delete=models.CASCADE)
    b_images = models.FileField(upload_to = 'images/')
    
    def __str__(self):
        return self.blockpaving.b_title



class Walls(models.Model):
    w_title = models.CharField(max_length=50)
    w_pic = models.IntegerField()
    w_label= models.FileField()

    def __str__(self):
        return self.w_title



class Wallsimage(models.Model):
    wall = models.ForeignKey(Walls, default=None, on_delete=models.CASCADE)
    w_images = models.FileField(upload_to = 'images/')
    
    def __str__(self):
        return self.wall.w_title

