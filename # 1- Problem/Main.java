
public class Main
{
    public static void main(String[] args) 
    {
        int sum = 0;
        int index = 0;
        while(index < 1000)
        {
            if(index % 3 == 0 || index % 5 == 0)
            {
                sum = sum + index;
            }
            index++;
        }
        System.out.println("The sum of multiples of 3 or 5 below 1000 is "+ sum);
    }   
}