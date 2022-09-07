# SpinalHDL基於Scala的HDL語言

* https://github.com/SpinalHDL/SpinalHDL
* [SpinalHDL: An alternative to standard HDL (PDF)](https://cdn.jsdelivr.net/gh/SpinalHDL/SpinalDoc@master/presentation/en/presentation.pdf) (讚)
* https://github.com/SpinalHDL/Spinal-bootcamp (讚)

```scala
class CarryAdder(size : Int) extends Component{
  val io = new Bundle{
    val a = in UInt(size bits)
    val b = in UInt(size bits)
    val result = out UInt(size bits)      //result = a + b
  }

  var c = False                   //Carry, like a VHDL variable
  for (i <- 0 until size) {
    //Create some intermediate value in the loop scope.
    val a = io.a(i)
    val b = io.b(i)

    //The carry adder's asynchronous logic
    io.result(i) := a ^ b ^ c
    c \= (a & b) | (a & c) | (b & c);    //variable assignment
  }
}

showRtl(new CarryAdder(4))
```


## 其他參考
* [数字硬件系统设计之一：Scala快速入门(上)](https://blog.csdn.net/zhi12345678/article/details/107378589)
    * https://www.bilibili.com/video/av668823961?zw
* [通用語言簡化數位硬體設計](https://www.eettaiwan.com/20170925ta31-digital-hardware-design/)
* [spinal HDL - 04 - Spinal HDL - 组件、层次结构和区域](https://vuko-wxh.blog.csdn.net/article/details/121098318)