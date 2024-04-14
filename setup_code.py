import os


def trigger_yaml():
    train_path=os.path.join("artifacts","datasets","train","images")
    test_path=os.path.join("artifacts","datasets","test","images")

    with open("config/data.yaml","w") as f:
        f.write("train: "+str(train_path))
        f.write("\n")
        f.write("val: "+str(test_path))
        f.write("\n")
        f.write("\n")
        f.write("\n")
        f.write("nc: 5")
        f.write("\n")
        f.write("\n")
        f.write("names: [ 'Helmet','Goggles','Jacket' ,'Gloves' ,'Footwear']")