//calculator using single responsibility principle
class calculator
{
public static int add(int x,int y)
{return x+y;}
public static int sub(int x,int y)
{return x-y;}
public static int mul(int x,int y)
{return x*y;}
public static int div(int x,int y)
{return x/y;}
}
class Resultprinter
{public static void display(int value)
{System.out.println("The value is:"+value);
}
}
class caldemo2
{public static void main(String args[])
{int a=calculator.add(20,30);
Resultprinter.display(a);
int b=calculator.sub(20,30);
Resultprinter.display(b);
int c=calculator.mul(20,30);
Resultprinter.display(c);
int d=calculator.div(20,30);
Resultprinter.display(d);
}
}

