//default constructor
class lewis44
{
int rollno;
String name;
int marks;
lewis44()
{
rollno=111;
name="Vijeth";
marks=789;
}
void putdata()
{
System.out.println("Rollno"+rollno);
System.out.println("Name:"+name);
System.out.println("Marks:"+marks);
}
}
class ferari44
{
public static void main(String[]args)
{
lewis44 l1=new lewis44();
l1.putdata();
}
}
