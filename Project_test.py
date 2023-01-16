from project import pet_type, time_feeding, breed_food, dog_weight_modulo, weight_food
import pytest

def main():
    test_pet_type()
    test_breed_food()
    test_dog_weight_modulo()
    test_weight_food()
    test_time_feeding()

def test_pet_type():
    with pytest.raises(SystemExit):
        pet_type("cat")
        pet_type("")
        pet_type("monkey")

def test_time_feeding():
    with pytest.raises(SystemExit):
        time_feeding("13.10")
        time_feeding("13")
        time_feeding("8")

def test_breed_food():
    assert breed_food("Golden retriever") == 700
    assert breed_food("Bulldog") == 300
    assert breed_food("Border collie") == 500


def test_dog_weight_modulo():
    assert dog_weight_modulo(28) == 30
    assert dog_weight_modulo(22) == 20

def test_weight_food():
    assert weight_food(35) == 700
    assert weight_food(15) == 300
    assert weight_food(5) == 100


if __name__ == "__main__":
    main()
