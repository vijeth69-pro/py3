//different types of variables
class lewis44
{
static int institutioncode=391;
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
System.out.println("Institution code:"+institutioncode);
System.out.println("Roll no:"+rollno);
System.out.println("Name:"+name);
System.out.println("Marks:"+marks);
}
}
class magwheel
{
public static void main(String[]args)
{
lewis44 l1=new lewis44(111,"lewis",789);
l1.putdata();
}
}