from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result[0] == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result[0] == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result[0] == "Too Low"
    
def test_guess_5_vs_secret_10():
    # Numerical: 5 < 10, so "Too Low"
    # Lexicographical (old bug): "5" > "10", would incorrectly return "Too High"
    result = check_guess(5, 10)
    assert result[0] == "Too Low"
    assert result[1] == "📈 Go HIGHER!"

def test_guess_9_vs_secret_10():
    # Numerical: 9 < 10, so "Too Low"
    # Lexicographical (old bug): "9" > "10", would incorrectly return "Too High"
    result = check_guess(9, 10)
    assert result[0] == "Too Low"
    assert result[1] == "📈 Go HIGHER!"

def test_guess_10_vs_secret_2():
    # Numerical: 10 > 2, so "Too High"
    # Lexicographical: "10" > "2", correctly "Too High" (this was already working)
    result = check_guess(10, 2)
    assert result[0] == "Too High"
    assert result[1] == "📉 Go LOWER!"

def test_guess_15_vs_secret_10():
    # Numerical: 15 > 10, so "Too High"
    # Lexicographical: "15" > "10", correctly "Too High"
    result = check_guess(15, 10)
    assert result[0] == "Too High"
    assert result[1] == "📉 Go LOWER!"

def test_guess_1_vs_secret_10():
    # Numerical: 1 < 10, so "Too Low"
    # Lexicographical: "1" < "10", correctly "Too Low"
    result = check_guess(1, 10)
    assert result[0] == "Too Low"
    assert result[1] == "📈 Go HIGHER!"

def test_guess_100_vs_secret_50():
    # Larger numbers: 100 > 50, "Too High"
    result = check_guess(100, 50)
    assert result[0] == "Too High"
    assert result[1] == "📉 Go LOWER!"

def test_guess_0_vs_secret_1():
    # Edge case: 0 < 1, "Too Low"
    result = check_guess(0, 1)
    assert result[0] == "Too Low"
    assert result[1] == "📈 Go HIGHER!"

def test_guess_99_vs_secret_100():
    # Edge case near upper bound: 99 < 100, "Too Low"
    result = check_guess(99, 100)
    assert result[0] == "Too Low"
    assert result[1] == "📈 Go HIGHER!"