#pragma once
#include  <iostream>
class angleConvert{
public:
  const int pi = 3.14159265359;
  angleConvert(); //default constructor
  double convertAngle(double);
  double deg, rad;

private:
  double degrees, radians;
  //double convert_ToRadians();
  //double convert_toDegrees();

};
