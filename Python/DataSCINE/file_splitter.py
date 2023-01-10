import os
import pandas as pd
import uuid
 
 
class FileSplitter(object):
 
    def __init__(self, file_name, row_size=100):
        self.file_name = file_name
        self.row_size = row_size
 
        self.df = pd.read_csv(self.file_name, chunksize=self.row_size)
 
    def run(self, directory="temp"):
 
        try:os.makedirs(directory)
        except Exception as e:pass
 
        counter = 0
 
        while True:
            try:
                file_name = "{}/{}_{}_row_{}_{}.csv".format(
                    directory,  self.file_name.split(".")[0], counter, self.row_size, str(uuid.uuid4())
                )
                df = next(self.df).to_csv(file_name)
                counter = counter + 1
            except StopIteration:
                break
            except Exception as e:
                print("Error:", e)
                break
 
        return True
 
 
def main():
    helper =  FileSplitter(
        file_name='sample1.csv',
        row_size=10
    )
    helper.run()
 
main()