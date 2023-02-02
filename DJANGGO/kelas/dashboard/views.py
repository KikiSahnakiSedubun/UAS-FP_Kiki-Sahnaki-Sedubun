from django.shortcuts import render,redirect
from dashboard.forms import FormBarang, FormBuku, FormDaftarbuku
from dashboard.models import Barang, Jenis, Buku, Daftarbuku
from dashboard.views import *
from django.contrib import messages


def produk(request):
    titelnya="Produk"
    konteks = {
        'titel':titelnya,
    }
    return render(request,'produk.html',konteks)
# Create your views here.

def tambah_barang(request):
    if request.POST:
        form=FormBarang(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil Ditambahkan")
            form = FormBarang()
            konteks = {
                'form': form,
            }
            return render(request,'tambah_barang.html',konteks)
    else:
        form=FormBarang()
        titelnya="Form"
        konteks={
            'form':form,
        }
    return render(request,'tambah_barang.html',konteks)

def tambah_buku(request):
    if request.POST:
        form=FormBuku(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil Ditambahkan")
            form = FormBuku()
            konteks = {
                'form': form,
            }
            return render(request,'tambah_buku.html',konteks)
    else:
        form=FormBuku()
        titelnya="Form"
        konteks={
            'form':form,
        }
    return render(request,'tambah_buku.html',konteks)

def tambah_daftarbuku(request):
    if request.POST:
        form=FormDaftarbuku(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil Ditambahkan")
            form = FormDaftarbuku()
            konteks = {
                'form': form,
            }
            return render(request,'tambah_daftarbuku.html',konteks)
    else:
        form=FormDaftarbuku()
        titelnya="Form"
        konteks={
            'form':form,
        }
    return render(request,'tambah_daftarbuku.html',konteks)

def ubah_brg(request,id_barang):
    barangs=Barang.objects.get(id=id_barang)
    if request.POST:
        form=FormBarang(request.POST,instance=barangs)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil diubah")
            return redirect('ubah_brg',id_barang=id_barang)
    else:
        form=FormBarang(instance=barangs)
        konteks = {
            'form' : form,
            'barangs' : barangs
        }
    return render(request,'ubah_brg.html', konteks)



def hapus_brg(request,id_barang) :
    barangs=Barang.objects.filter(id=id_barang)
    barangs.delete()
    messages.success(request,"Data Terhapus")
    return redirect('Vbrg')



def Barang_view(request):
    barangs=Barang.objects.all()
    titelnya="Daftar Barang"
    konteks={
        'barangs':barangs,
        'titel':titelnya,
    }
    return render(request,'tampilbrg.html', konteks)

def jenis(request):
    jeniss=Jenis.objects.all()
    titelnya="Jenis"
    konteks={
        'jeniss':jeniss,
        'titel':titelnya,
    }
    return render(request,'jenis.html', konteks)

def buku(request):
    bukus=Buku.objects.all()
    titelnya="Buku"
    konteks={
        'bukus':bukus,
        'titel':titelnya,
    }
    return render(request,'buku.html', konteks)

def daftarbuku(request):
    daftarbukus=Daftarbuku.objects.all()
    titelnya="Daftar buku"
    konteks={
        'daftarbukus':daftarbukus,
        'titel':titelnya,
    }
    return render(request,'daftarbuku.html', konteks)