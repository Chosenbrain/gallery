from django.contrib import admin

from .models import (Patios,Patiosimage,
Resins,Resinsimage,
Tarmac,Tarmacimage,
Fencing,Fencingimage,
BlockPaving,BlockPavingimage,
Walls,Wallsimage,Post,Bio)

admin.site.register(Post)
admin.site.register(Bio)


class PatiosimageAdmin(admin.TabularInline):
    model = Patiosimage

@admin.register(Patios)
class PatiosAdmin(admin.ModelAdmin):
    inlines = [PatiosimageAdmin]

    class Meta:
        model = Patios


class PatiosimageAdmin(admin.ModelAdmin):
    pass


class ResinsimageAdmin(admin.TabularInline):
    model = Resinsimage

@admin.register(Resins)
class ResinsAdmin(admin.ModelAdmin):
    inlines = [ResinsimageAdmin]

    class Meta:
        model = Resins


class ResinsimageAdmin(admin.ModelAdmin):
    pass


class TarmacimageAdmin(admin.TabularInline):
    model = Tarmacimage

@admin.register(Tarmac)
class TarmacAdmin(admin.ModelAdmin):
    inlines = [TarmacimageAdmin]

    class Meta:
        model = Tarmac

class TarmacimageAdmin(admin.ModelAdmin):
    pass


class FencingimageAdmin(admin.TabularInline):
    model = Fencingimage

@admin.register(Fencing)
class FencingAdmin(admin.ModelAdmin):
    inlines = [FencingimageAdmin]

    class Meta:
        model = Fencing


class FencingimageAdmin(admin.ModelAdmin):
    pass


class BlockPavingimageAdmin(admin.TabularInline):
    model = BlockPavingimage

@admin.register(BlockPaving)
class BlockPavingAdmin(admin.ModelAdmin):
    inlines = [BlockPavingimageAdmin]

    class Meta:
        model = BlockPaving


class BlockPavingimageAdmin(admin.ModelAdmin):
    pass


class WallsimageAdmin(admin.TabularInline):
    model = Wallsimage

@admin.register(Walls)
class WallsAdmin(admin.ModelAdmin):
    inlines = [WallsimageAdmin]

    class Meta:
        model = Walls


class WallsimageAdmin(admin.ModelAdmin):
    pass
    