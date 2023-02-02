from django.contrib import admin

# Register your models here.

from .models import Barang, Jenis
from .models import Transaksi
from .models import Detailtrans
from .models import Buku
from .models import Daftarbuku


admin.site.register(Barang)
admin.site.register(Jenis)
admin.site.register(Buku)
admin.site.register(Daftarbuku)
