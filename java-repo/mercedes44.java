//parameterized constructor
class lewis44
{
int rollno;
String name;
int marks;
lewis44(int rno,String n,int m)
{
rollno=rno;
name=n;
marks=m;
}
void putdata()
{
System.out.println("Rollno"+rollno);
System.out.println("Name:"+name);
System.out.println("Marks:"+marks);
}
}
class mercedes44
{
public static void main(String[]args)
{
lewis44 l1=new lewis44(111,"lewis",789);
l1.putdata();
}
}