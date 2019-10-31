import simplecalculator

def test_add():
        assert simplecalculator.add(14,16) == 30
        assert simplecalculator.add(45,60) == 105
        assert simplecalculator.add(75,22) == 97

        assert simplecalculator.add(14,16,22) == 52
        assert simplecalculator.add(45,60,45,19) == 169
        assert simplecalculator.add(75,22,53,77) == 227

def test_multiply():
        
        assert simplecalculator.multiply(5,10) == 50
        assert simplecalculator.multiply(7,5) == 35
        assert simplecalculator.multiply(9,9) == 81

        assert simplecalculator.multiply(5,10,2) == 100 
        assert simplecalculator.multiply(7,5,10,9) == 3150
        assert simplecalculator.multiply(10,7,5,9,12,6) == 226800