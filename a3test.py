# a3test.py
# Kathryn Zimmerman kpz8, Max Senkovsky mgs253
# 10/6/2014
""" Unit Test for Assignment A3"""
import colormodel
import cornelltest
import a3

def test_complement():
    """Test function complement"""
    cornelltest.assert_equals(colormodel.RGB(255-250, 255-0, 255-71), 
            a3.complement_rgb(colormodel.RGB(250, 0, 71)))
    cornelltest.assert_equals(colormodel.RGB(255-0, 255-112, 255-17),
            a3.complement_rgb(colormodel.RGB(0, 112, 17)))
    cornelltest.assert_equals(colormodel.RGB(255-14, 255-112, 255-0),
            a3.complement_rgb(colormodel.RGB(14, 112, 0)))
    cornelltest.assert_equals(colormodel.RGB(255-255, 255-112, 255-0),
            a3.complement_rgb(colormodel.RGB(255, 112, 0)))
    


def test_truncate5():
    """Test function truncate5"""
    cornelltest.assert_equals('130.5',  a3.truncate5(130.59))
    cornelltest.assert_equals('130.5',  a3.truncate5(130.54))
    cornelltest.assert_equals('100.0',  a3.truncate5(100))
    cornelltest.assert_equals('99.56',  a3.truncate5(99.566))
    cornelltest.assert_equals('99.99',  a3.truncate5(99.99))
    cornelltest.assert_equals('99.99',  a3.truncate5(99.995))
    cornelltest.assert_equals('21.99',  a3.truncate5(21.99575))
    cornelltest.assert_equals('21.99',  a3.truncate5(21.994))
    cornelltest.assert_equals('10.01',  a3.truncate5(10.013567))
    cornelltest.assert_equals('10.00',  a3.truncate5(10.000000005))
    cornelltest.assert_equals('9.999',  a3.truncate5(9.9999))
    cornelltest.assert_equals('9.999',  a3.truncate5(9.9993))
    cornelltest.assert_equals('1.354',  a3.truncate5(1.3546))
    cornelltest.assert_equals('1.354',  a3.truncate5(1.3544))
    cornelltest.assert_equals('0.045',  a3.truncate5(.0456))
    cornelltest.assert_equals('0.045',  a3.truncate5(.0453))
    cornelltest.assert_equals('0.005',  a3.truncate5(.0056))
    cornelltest.assert_equals('0.001',  a3.truncate5(.0013))
    cornelltest.assert_equals('0.000',  a3.truncate5(.0004))
    cornelltest.assert_equals('0.000',  a3.truncate5(.0009999))
    cornelltest.assert_equals('0.000',  a3.truncate5(0))
    cornelltest.assert_equals('999.0',  a3.truncate5(999))

def test_round5():
    """Test function round5"""
    cornelltest.assert_equals('130.6',  a3.round5(130.59))
    cornelltest.assert_equals('130.5',  a3.round5(130.54))
    cornelltest.assert_equals('100.0',  a3.round5(100))
    cornelltest.assert_equals('99.57',  a3.round5(99.566))
    cornelltest.assert_equals('99.99',  a3.round5(99.99))
    cornelltest.assert_equals('100.0',  a3.round5(99.995))
    cornelltest.assert_equals('22.00',  a3.round5(21.99575))
    cornelltest.assert_equals('21.99',  a3.round5(21.994))
    cornelltest.assert_equals('10.01',  a3.round5(10.013567))
    cornelltest.assert_equals('10.00',  a3.round5(10.000000005))
    cornelltest.assert_equals('10.00',  a3.round5(9.9999))
    cornelltest.assert_equals('9.999',  a3.round5(9.9993))
    cornelltest.assert_equals('1.355',  a3.round5(1.3546))
    cornelltest.assert_equals('1.354',  a3.round5(1.3544))
    cornelltest.assert_equals('0.046',  a3.round5(.0456))
    cornelltest.assert_equals('0.045',  a3.round5(.0453))
    cornelltest.assert_equals('0.006',  a3.round5(.0056))
    cornelltest.assert_equals('0.001',  a3.round5(.0013))
    cornelltest.assert_equals('0.000',  a3.round5(.0004))
    cornelltest.assert_equals('0.001',  a3.round5(.0009999))
    cornelltest.assert_equals('0.000',  a3.round5(0))
    cornelltest.assert_equals('360.0',  a3.round5(360))


def test_round5_color():
    """Test the round5 functions for cmyk and hsv."""
    cornelltest.assert_equals('(98.45, 25.36, 72.80, 25.00)',
            a3.round5_cmyk(colormodel.CMYK(98.448, 25.362, 72.8, 25.0)));
    cornelltest.assert_equals('(0.000, 25.36, 100.0, 25.00)',
            a3.round5_cmyk(colormodel.CMYK(0.00000, 25.362, 100.000, 25.0)))
    cornelltest.assert_equals('(98.45, 0.250, 0.000)',
            a3.round5_hsv(colormodel.HSV(98.44834572, 0.25, 0.0001)))
    cornelltest.assert_equals('(360.0, 1.000, 0.002)',
            a3.round5_hsv(colormodel.HSV(359.9999999, 1.0, 0.0019)))


def test_rgb_to_cmyk():
    """Test rgb_to_cmyk"""
    rgb = colormodel.RGB(255, 255, 255);
    cmyk = a3.rgb_to_cmyk(rgb);
    cornelltest.assert_equals('0.000', a3.round5(cmyk.cyan))
    cornelltest.assert_equals('0.000', a3.round5(cmyk.magenta))
    cornelltest.assert_equals('0.000', a3.round5(cmyk.yellow))
    cornelltest.assert_equals('0.000', a3.round5(cmyk.black))
    
    rgb = colormodel.RGB(0, 0, 0);
    cmyk = a3.rgb_to_cmyk(rgb);
    cornelltest.assert_equals('0.000', a3.round5(cmyk.cyan))
    cornelltest.assert_equals('0.000', a3.round5(cmyk.magenta))
    cornelltest.assert_equals('0.000', a3.round5(cmyk.yellow))
    cornelltest.assert_equals('100.0', a3.round5(cmyk.black))
        
    rgb = colormodel.RGB(217, 43, 164);
    cmyk = a3.rgb_to_cmyk(rgb);
    cornelltest.assert_equals('0.000', a3.round5(cmyk.cyan))
    cornelltest.assert_equals('80.18', a3.round5(cmyk.magenta))
    cornelltest.assert_equals('24.42', a3.round5(cmyk.yellow))
    cornelltest.assert_equals('14.90', a3.round5(cmyk.black))
    
    rgb = colormodel.RGB(1, 1, 1);
    cmyk = a3.rgb_to_cmyk(rgb);
    cornelltest.assert_equals('0.000', a3.round5(cmyk.cyan))
    cornelltest.assert_equals('0.000', a3.round5(cmyk.magenta))
    cornelltest.assert_equals('0.000', a3.round5(cmyk.yellow))
    cornelltest.assert_equals('99.61', a3.round5(cmyk.black))


def test_cmyk_to_rgb():
    """Test translation function cmyk_to_rgb"""
    cmyk = colormodel.CMYK(0.000, 0.000, 0.000, 0.000);
    rgb = a3.cmyk_to_rgb(cmyk);
    cornelltest.assert_equals(255, rgb.red)
    cornelltest.assert_equals(255, rgb.green)
    cornelltest.assert_equals(255, rgb.blue)

    cmyk = colormodel.CMYK(50.00, 76.00, 12.97, 1.000);
    rgb = a3.cmyk_to_rgb(cmyk);
    cornelltest.assert_equals(126, rgb.red)
    cornelltest.assert_equals(61, rgb.green)
    cornelltest.assert_equals(220, rgb.blue)

    cmyk = colormodel.CMYK(100.0, 100.0, 100.0, 100.0);
    rgb = a3.cmyk_to_rgb(cmyk);
    cornelltest.assert_equals(0, rgb.red)
    cornelltest.assert_equals(0, rgb.green)
    cornelltest.assert_equals(0, rgb.blue)

def test_rgb_to_hsv():
    """Test translation function rgb_to_hsv"""
    rgb = colormodel.RGB(255, 255, 255);
    hsv = a3.rgb_to_hsv(rgb);
    cornelltest.assert_equals('0.000', a3.round5(hsv.hue))
    cornelltest.assert_equals('0.000', a3.round5(hsv.saturation))
    cornelltest.assert_equals('1.000', a3.round5(hsv.value))

    rgb = colormodel.RGB(255, 200, 50);
    hsv = a3.rgb_to_hsv(rgb);
    cornelltest.assert_equals('43.90', a3.round5(hsv.hue))
    cornelltest.assert_equals('0.804', a3.round5(hsv.saturation))
    cornelltest.assert_equals('1.000', a3.round5(hsv.value))
    
    rgb = colormodel.RGB(255, 50, 200);
    hsv = a3.rgb_to_hsv(rgb);
    cornelltest.assert_equals('316.1', a3.round5(hsv.hue))
    cornelltest.assert_equals('0.804', a3.round5(hsv.saturation))
    cornelltest.assert_equals('1.000', a3.round5(hsv.value))

    rgb = colormodel.RGB(50, 255, 200);
    hsv = a3.rgb_to_hsv(rgb);
    cornelltest.assert_equals('163.9', a3.round5(hsv.hue))
    cornelltest.assert_equals('0.804', a3.round5(hsv.saturation))
    cornelltest.assert_equals('1.000', a3.round5(hsv.value))
    
    rgb = colormodel.RGB(50, 200, 255);
    hsv = a3.rgb_to_hsv(rgb);
    cornelltest.assert_equals('196.1', a3.round5(hsv.hue))
    cornelltest.assert_equals('0.804', a3.round5(hsv.saturation))
    cornelltest.assert_equals('1.000', a3.round5(hsv.value))
    
    rgb = colormodel.RGB(255, 200, 200);
    hsv = a3.rgb_to_hsv(rgb);
    cornelltest.assert_equals('0.000', a3.round5(hsv.hue))
    cornelltest.assert_equals('0.216', a3.round5(hsv.saturation))
    cornelltest.assert_equals('1.000', a3.round5(hsv.value))
    
def test_hsv_to_rgb():
    """Test translation function hsv_to_rgb"""
    hsv = colormodel.HSV(200.0, 0.500, 0.400);
    rgb = a3.hsv_to_rgb(hsv);
    cornelltest.assert_equals(51, rgb.red)
    cornelltest.assert_equals(85, rgb.green)
    cornelltest.assert_equals(102, rgb.blue)
    
    hsv = colormodel.HSV(50.00, 0.500, 0.400);
    rgb = a3.hsv_to_rgb(hsv);
    cornelltest.assert_equals(102, rgb.red)
    cornelltest.assert_equals(94, rgb.green)
    cornelltest.assert_equals(51, rgb.blue)
    
    hsv = colormodel.HSV(110.0, 0.500, 0.400);
    rgb = a3.hsv_to_rgb(hsv);
    cornelltest.assert_equals(60, rgb.red)
    cornelltest.assert_equals(102, rgb.green)
    cornelltest.assert_equals(51, rgb.blue)
    
    hsv = colormodel.HSV(170, 0.500, 0.400);
    rgb = a3.hsv_to_rgb(hsv);
    cornelltest.assert_equals(51, rgb.red)
    cornelltest.assert_equals(102, rgb.green)
    cornelltest.assert_equals(94, rgb.blue)
    
    hsv = colormodel.HSV(230.0, 0.500, 0.400);
    rgb = a3.hsv_to_rgb(hsv);
    cornelltest.assert_equals(51, rgb.red)
    cornelltest.assert_equals(59, rgb.green)
    cornelltest.assert_equals(102, rgb.blue)
    
    hsv = colormodel.HSV(290.0, 0.500, 0.400);
    rgb = a3.hsv_to_rgb(hsv);
    cornelltest.assert_equals(94, rgb.red)
    cornelltest.assert_equals(51, rgb.green)
    cornelltest.assert_equals(102, rgb.blue)
    
    hsv = colormodel.HSV(350.0, 0.500, 0.400);
    rgb = a3.hsv_to_rgb(hsv);
    cornelltest.assert_equals(102, rgb.red)
    cornelltest.assert_equals(51, rgb.green)
    cornelltest.assert_equals(60, rgb.blue)
    

# Application Code
if __name__ == "__main__":
    test_complement()
    test_truncate5()
    test_round5()
    test_round5_color()
    test_rgb_to_cmyk()
    test_cmyk_to_rgb()
    test_rgb_to_hsv()
    test_hsv_to_rgb()
    print "Module a3 is working correctly"
