#np行列計算　code
#code
#numpyで行列計算する練習用コード
#code:python3
import numpy as np
 #arrayなどで作成されるのは、通常のリストではなく、ndarryというクラスのインスタンス。
#ベクトルの作成
arr = np.array([10,20,30.])
print(arr)
#ゼロのベクトル
arr0=np.zeros(5)
#単位ベクトル
arr1=np.ones(5)
print(arr0)
print(arr1)
 
#arangeはステップ（いくつづつ増えるか）を指定
#linspaceは分割数を指定
arr1 = np.arange(0,100,20)
arr2 = np.linspace(0,100,5)
print(arr1)
print(arr2)

#ベクトルと数値の演算
arr1 = np.array([1,2,3,5,8])
print(arr1)
print(arr1 + 10)
print(arr1 - 10)
print(arr1 * 2)
print(arr1 / 2)
print(arr1 % 2)
print(arr1 ** 2)

#ベクトル同士の演算
arr1 = np.array([1,2,3,5])
arr2 = np.array([8,13,21,34])
print(arr2 + arr1)
print(arr2 - arr1)
print(arr2 * arr1)
print(arr2 / arr1)
print(arr2 % arr1)

#行列作成
arr1 = np.matrix([[1,2,3],
                 [4,5,6],
                 [7,8,9]])
print(arr1)

#単位行列の作成
arr1 = np.identity(3)
arr2 = np.identity(5)
print(arr1)
print(arr2)

#非正方の単位行列
arr1 = np.eye(5,7,0)
arr2 = np.eye(5,7,2)
print(arr1)
print(arr2)

#その他の対角行列
arr1 = np.diag([1,2,3])
arr2 = np.diag([3,5,8,13,21])
print(arr1)
print(arr2)

#ベクトルから行列への変換
arr1 = np.array([1,2,3,5,8,13,21,34,55])
arr2 = arr1.reshape((3,3))
print(arr1)
print(arr2)

#行列からベクトルへの変換
arr1 = np.diag([1,2,3,5])
arr2 = np.ravel([arr1])
print(arr1)
print(arr2)

#転置行列
arr1 = np.array([1,2,3,5,8,13,21,34,55])
arr2 = arr1.reshape((3,3))
print(arr2)
print(arr2.T)

#ベクトル・行列の演算
#ベクトルの結合
import numpy as np

arr1= np.array([1,2,3])
arr2 = np.array([5,8,13])
arr3 = arr1 + arr2
arr4 = np.ravel([arr1,arr2])
print(arr3)
print(arr4)

#ベクトルの内積・外積
import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([5,8,13])
arr3 = np.inner(arr1,arr2)
arr4 = np.outer(arr1,arr2)
print(arr3)
print(arr4)

#行列の四則演算
import numpy as np
arr1 = np.matrix([[1,2,3],
                 [5,8,13],
                 [21,34,55]])
#単位正方行列
arr2 = np.identity(3)

print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr2 / arr1)

#ndarryは乗算が異なる
import numpy as np
arr1 = np.array([[1,2,3],
               [5,8,13],
               [21,34,55]])
arr2 = np.array([[1,0,0],
               [0,1,0],
               [0,0,1]])

print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr2 / arr1)

#ndarrayを用いた行列の積
import numpy as np
arr1 = np.matrix([[1,2,3],
                 [5,8,13],
                 [21,34,55]])
arr2 = np.matrix([[2,1,1],
                [1,3,1],
                [1,1,4]])

print(np.dot(arr1,arr2))
print(np.outer(arr1, arr2))

#行列の結合
import numpy as np
arr1 = np.matrix([[1,2,3],
                 [5,8,13],
                 [21,34,55]])
arr2 = np.identity(3)

print(np.hstack([arr1,arr2]))
print(np.vstack([arr1,arr2]))

#行列結合
import numpy as np
arr1 = np.matrix([[1,2,3],
                 [5,8,13],
                 [21,34,55]])
arr2 = np.identity(3)
print(np.bmat([[arr1,arr2],
              [arr2,arr1]]))

#行列の分割
import numpy as np
arr1 = np.arange(16).reshape(4,4)
(v1,v2)=np.vsplit(arr1,2)
(h1,h2)=np.hsplit(arr1,2)

print(arr1)
print(v1)
print(v2)
print(h1)
print(h2)

#総和の計算
import numpy as np
arr1 = np.arange(16).reshape(4,4)
print(arr1)
print()
print(np.sum(arr1))
#axis=0は列の和
print(np.sum(arr1, axis=0))
#axis=1は行の和
print(np.sum(arr1, axis=1))

#最大値・最小値
import numpy as np
arr1 = np.arange(16).reshape(4,4)
print(arr1)
print()
print(np.min(arr1))
print(np.min(arr1, axis=0))
print(np.min(arr1, axis=1))
print(np.max(arr1))
print(np.max(arr1, axis=0))
print(np.max(arr1,axis=1))

#統計計算
import numpy as np
arr1 = np.array(np.random.randint(0,100,(10,10)))
print("平均:" + str(np.mean(arr1)))
print("平均:" + str(np.mean(arr1,axis=0)))
print("平均:" + str(np.mean(arr1,axis=1)))
print("分散:" + str(np.median(arr1)))
print("分散:" + str(np.median(arr1,axis=0)))
print("分散:" + str(np.median(arr1,axis=1)))
print("標準偏差:" + str(np.median(arr1)))
print("標準偏差:" + str(np.median(arr1,axis=0)))
print("標準偏差:" +str(np.median(arr1,axis=1)))

#行列のべき乗計算
import numpy as np
arr1 = np.matrix([[1,2,3],
                 [5,8,13],
                 [21,34,55]])
re0 = np.linalg.matrix_power(arr1,0)
re1 = np.linalg.matrix_power(arr1,1)
re2 = np.linalg.matrix_power(arr1,2)
print(re0)
print(re1)
print(re2)

#逆行列と行列式
#invは逆行列,detは行列式
import numpy as np

arr1 = np.matrix([[0,1,3],
                 [3,5,8],
                 [21,34,55]])
print(np.linalg.inv(arr1))
print(np.linalg.det(arr1))

 
 

