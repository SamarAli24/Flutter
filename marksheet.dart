import 'dart:io';


void main()
{
  stdout.write("Enter Chemistry Marks :");
  double chem = double.parse(stdin.readLineSync()!);

  stdout.write("Enter Maths Marks :");
  double math = double.parse(stdin.readLineSync()!);

  stdout.write("Enter Physics Marks :");
  double physics = double.parse(stdin.readLineSync()!);

  stdout.write("Enter English Marks :");
  double eng = double.parse(stdin.readLineSync()!);

  stdout.write("Enter Computer Marks :");
  double computer = double.parse(stdin.readLineSync()!);


  stdout.write("Enter Statitics Marks :");
  double stats= double.parse(stdin.readLineSync()!);


  num obtained=(math+computer+eng+stats+physics+chem);
  num total_marks=600;

  num result=((obtained)/(total_marks)*(100));

  print("Percentage $result");

  if(result<=99 && result>=80){
    print("You got A+ Grade");
  }
else if(result<=79 && result>=70){
  print("You got A grade");
  }

else if(result<=69 && result>=60){
  print("You got B grade");
  }
  else if(result<=59 && result>=50){
    print("You got C grade");
  }

  else if(result<=49 && result>=40){
    print("You got D grade");
  }
  else if(result<=39 && result>=30){
    print("You got E grade");
  }
  else if(result<30){
    print("Failed");
  }



}