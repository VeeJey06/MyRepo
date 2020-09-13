from django.shortcuts import render
from gtts import gTTS
import pandas
import numpy
from django.http import HttpResponse, FileResponse
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler
import seaborn
import matplotlib.pyplot as plt
from django.views.decorators.csrf import csrf_exempt
import threading


class DigDoc:
    def __init__(self):
        self.cva_path = "./Resources/sample_output.csv"
        self.model = None
        self.thread = threading.Thread()

    def text_to_speech(self, req, input):
        """

        :param req:
        :param input:
        :return:
        """
        text = "Something went wrong. please try again later" if not input else input
        lang = "en"
        voice = gTTS(text=text, lang=lang, slow=False)
        voice.save("c:\\voice.mp3")
        return FileResponse(open("c:\\voice.mp3", "rb"))

    def tst(self, req):
        """

        :param req:
        :return:
        """
        render(req, "home.html")

    def append_data(self, newrow):
        """

        :param newrow:
        :return:
        """
        data = pandas.read_csv(self.cva_path)
        data = data.append(newrow, ignore_index=True)
        data.to_csv(self.cva_path, index=False)
        return True

    def analize(self, file):
        """

        :return:
        """
        x = file.drop(['risk', 'age'], axis=1)
        y = file["risk"]
    #   Train
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
        # sc = StandardScaler()
        # x_train = sc.transform(x_train)
        # x_test = sc.transform(x_test)
        self.model = LogisticRegression(multi_class="multinomial", max_iter=10000).fit(x_train, y_train)

    #   Accuracy
        op = self.model.predict(x_test)
        print("Accuracy:", accuracy_score(y_test, op))
        con_mat = confusion_matrix(y_test, op)
        print(con_mat)
        print(classification_report(y_test, op))

    #   Plot
    #     fig, ax = plt.subplots(figsize=(8, 8))
    #     ax.imshow(con_mat)
    #     ax.grid(False)
    #     ax.set_xlabel('Predicted outputs', fontsize=10, color='black')
    #     ax.set_ylabel('Actual outputs', fontsize=10, color='black')
    #     ax.xaxis.set(ticks=range(4))
    #     ax.yaxis.set(ticks=range(4))
    #     # ax.set_ylim(9.5, -0.5)
    #     for i in range(4):
    #         for j in range(4):
    #             ax.text(j, i, con_mat[i, j], ha='center', va='center', color='black')
        # plt.show()
        return True

    @csrf_exempt
    def predict_op(self, req):
        """

        :param req:
        :return:
        """
        file = pandas.read_csv(self.cva_path)
        if not self.model:
            self.analize(file)
        temp = int(req.POST.get("temp"))
        age = int(req.POST.get("age"))
        cough = int(req.POST.get("cough"))
        oxi = int(req.POST.get("oxi"))
        data = [[temp, cough, oxi]]
        # data = numpy.array([temp, cough, oxi]).reshape(1, -1)
        op = self.model.predict(data)
        new_row = {"age": age,
                   "temperature": temp,
                   "cough": cough,
                   "oximeter": oxi,
                   "risk": op[0]
                   }
        self.append_data(new_row)
        t1 = threading.Thread(target=self.analize, args=(file,))
        if self.thread.is_alive():
            self.thread.join()
        t1.start()
        self.thread = t1
        plot1 = seaborn.displot(x="risk", data=file, legend=True)
        plot1.savefig("sdf.png")
        return HttpResponse(op)


if __name__ == '__main__':
    a = DigDoc()
    # cva_path = "../Resources/sample.cva"
    # d = {"age": 10,
    #      "temp": 10,
    #      "cough": 10,
    #      "oxi": 10,
    #      "risk": "lig"
    #      }
    # a.append_data(d)
    # a.analize()
