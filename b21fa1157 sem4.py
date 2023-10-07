#1 50-100 хүртэл тоон утга бүхий нэг хэмжээст массив (вектор) үүсгэ. 
import numpy as np
A = np.arange(50,100)
A

#2 Арван ширхэг 1, арван ширхэг 0, арван ширхэг 6 тоо бүхий нэг хэмжээст массивууд (вектор) үүсгэ.
import numpy as np
a=np.ones(10)
b=np.zeros(10)
c=np.ones(10)*6
np.concatenate([a,b,c])

#3 20-32 хүртэл тоон утга бүхий 3x4 хэмжээтэй массив үүсгэ.
import numpy as np
x=np.arange(20,32)
a=np.reshape(x, (3,4), 'F')
print(a)

#4 Диагональ нь 1-ийн тоо, бусад нь 0 байх 3x3 хэмжээтэй массив үүсгэ.
import numpy as np
ar = np.array([1, 1, 1])
res = np.diag(ar)
print(res)

#5 Диагональ нь 1-5 хүртэл тоо, бусад нь 0 байх 5х5 хэмжээтэй массив үүсгэ.
import numpy as np
a = np.diag([1,2,3,4,5])
a

#6 Хоёр хэмжээстэй массив үүсгэж, нийт элементүүдийн нйилөэр, багана, мөрийн нийлбэрүүдийг хэвлэ.
import numpy as np
y=np.random.randn(5,2)
print(y)
a=np.sum(y)
b=np.sum(y, axis=0)
c=np.sum(y, axis=1)
print(a,b,c)

#7 Спортын сайтуудын мэдээллийг ашиглан хөл бөмбөгийн спортын дурын 10 тоглогчийн сүүлийн арван жилийн цалин, нийт тоглолт, оруулсан гоалуудын талаар мэдээллийг цуглуулж тус бүрээр массив үүсгэ. Үүсгэсэн массив тус бүрийн багана болон мөрүүдийн нийлбэрийг хэвлэ.
import numpy as np
Haaland = np.random.randn(5,5)
Saka = np.random.randn(5,5)
Jesus = np.random.randn(5,5)
Martinelli = np.random.randn(5,5)
Trossard = np.random.randn(5,5)
Xhaka = np.random.randn(5,5)
Martin = np.random.randn(5,5)
Jojo = np.random.randn(5,5)
Saliba = np.random.randn(5,5)
Gabriel = np.random.randn(5,5)
a=(Haaland,Saka,Jesus,Martinelli,Trossard,Xhaka,Martin,Jojo,Saliba,Gabriel)
for i in a:
    print("Баганы дагуу", np.sum(i, axis=0))
    print("Мөрийн дагуу", np.sum(i, axis=1))