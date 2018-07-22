"""intialize booter"""
import jpype 
jpype.startJVM(path to jvm.dll, "-ea") 
javaPackage = jpype.JPackage("boot") 
javaClass = javaPackage.JavaClassName 
javaObject = javaClass() 
javaObject.JavaMethodName() 
jpype.shutdownJVM() 
