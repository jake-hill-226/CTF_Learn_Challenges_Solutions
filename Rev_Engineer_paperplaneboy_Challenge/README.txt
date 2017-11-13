So I made the mistake of leaving my computer with my very immature friend, 
and he took the flag I had and hid it! Can you get it back?

PS: Excuse the poor naming of stuff, it's a product of my friend's immaturity.

https://mega.nz/#!RuQgyRgK!FQtaZJMIkKQloZS-dUHTxUBYeX2SnREmLP43aaJDuW4

Step1: Download .txt from link above

Step2: Determine what hash algorithm it is using
	-Base64
Step3: Decrypt hash
	- get a java program

	import java.util.Scanner;

	public class oof
	{
	    public static void main(String[] args){
	        System.out.println("what is it?");
	        Scanner in = new Scanner(System.in);
	        String input = in.next();
	        System.out.println(check(doStuff(input),input));
	    }
	    public static String check(String str, String in) {
	        return str.equals("cF/r;i{ID8BW}")
	        ?"here's your flag: " +in: "get rekt u lose haha !!!";
	    }
	    public static String doStuff(String str){
	        char[] boi = new char[13];
	        if (str.length() == 12){
	            for(int i = 0; i < 12; i++) {
	                boi[i] = (char)(str.charAt(i) - 4 + i*3);
	            }
	            boi[12] = '}';
	            return new String(boi);
	        }
	        return "get rekt u lose haha !!!";
	    }
	}

Step4: Reverse engineer the script
	- doStuff is creating a weird ascii shift cipher
	- take cF/r;i{ID8BW and thow it into a reverse for loop
	  present in doStuff() function

Step5: Get the flag
	- gG-m3^m80!(: