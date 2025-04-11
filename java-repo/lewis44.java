//intatiastion of object
class vijju
{
int rollno;
String name;
int marks;
void getdata(int rno,String n,int m)
{
rollno=rno;
name=n;
marks=m;
}
void putdata()
{
System.out.println("Rollno:"+rollno);
System.out.println("Name:"+name);
System.out.println("Marks:"+marks);
}
}
class lewis44
{
public static void main(String[]args)
{
vijju v1=new vijju();
v1.getdata(391,"vjeth",555);
v1.putdata();
}
}