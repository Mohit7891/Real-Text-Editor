class Box {
    private int length,height,width;
    public void setLength(int l,int b,int h)
    {
        length = l;
        width=b;
        height=h;
    }
    public void showdata()
    {
        System.out.println("L="+length);
        System.out.println("B="+width);
        System.out.println("H="+height);
    }
}
class Example
{
    public static void main(String[] args)
{
    Box smallbox = new Box();
    smallbox.setLength(12,35,22);
    smallbox.showdata();
}
}