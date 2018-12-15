#include  <iostream>
#include  <iomanip>
#include  "angleConvert.h"

//default constructor
angleConvert::angleConvert(){
  degrees = 0.0, radians = 0.0;
}

double angleConvert::convertAngle(double angle){
  int choice;
  double output = 0.0;

  std::cout   << "1. Convert to Degrees" << '\n'
              << "2. Convert to Radians" << '\n'
              << "\n\n"
              ;
  std::cout << "Choice: ";
  std::cin >> choice;

  switch (choice) {
    case 1:
      degrees = angle;
      output = degrees * 180 / pi;
      break;
    case 2:
      radians = angle;
      output = radians * pi / 180;
      break;
  }

  return output;
}

int main(){
  double angle = 90.0000000;
  angleConvert lens1;

  std::cout << std::fixed << std::setprecision(3)
    << lens1.convertAngle(angle);

}
