FROM registry.redhat.io/ubi7/ubi
LABEL description="A custom Linear Regression container based on UBI 7" \
      Software="scikit-learn,numpy,joblib python library available in the container"\
      Purpose="Input the exprience and get salary predicted accordingly" \
      Files="Dataset('Salary_Data.csv'),salary_pred.py and salary_pred.pk1(model saved to after training),salary.py" \
      DatasetLink=" https://www.kaggle.com/vihansp/salary-data" \
      Maintainer="Deepak Yadav <alfo7742@gmail.com>" \
      Extra="if wanted to re-run the salary.py to make model again install python libaray pandas and download the dataset form above provided link"
COPY src/salary_pred.* .
COPY src/salary.py .
RUN yum install python3 -y && pip3 install joblib scikit-learn && \
        yum clean all
CMD ["python","./salary_pred.py"]
