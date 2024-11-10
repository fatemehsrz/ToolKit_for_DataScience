
from functools import *

def power(exponent, base):
    return base ** exponent
 
square = partial(power, 2) # setting value of exponent to 2
cube = partial(power, 3) # setting value of exponent to 3
print("The square of 5 is", square(5))
print("The cube of 7 is", cube(7))

def print_msg(name, message):
    msg = str(name) +", "+ str(message)
    return msg

welcome = partial(print_msg, message='Welcome to the Team!') #setting the welcome message
holidays = partial(print_msg, message='Happy Holidays!')
print(welcome('Sourish'))
print(holidays('Shubhrima'))


from scipy.stats import probplot, skew

# Loop through each numeric column
for column in numeric_columns:
    fig, axes = plt.subplots(1, 3, figsize=(20, 4))

    # Distribution plot
    sns.histplot(df_user[column], kde=False, ax=axes[0])
    axes[0].set_title(f"{column} | Distribution Plot")

    # Boxplot
    sns.boxplot(df_user[column], ax=axes[1])
    axes[1].set_title(f"{column} | Boxplot")
    axes[1].set_yticklabels([])
    axes[1].set_yticks([])

    # Probability plot
    probplot(df_user[column], plot=axes[2])
    skew_val = round(df_user[column].skew(), 1)
    axes[2].set_title(f"{column} | Probability Plot - Skew: {skew_val}")

    # Display the plots
    plt.show()


daily_counts = df_new['Day'].value_counts().sort_index()
plt.figure(figsize=(10, 6))
sns.barplot(x=daily_counts.index, y=daily_counts.values)
plt.title('Course Enrollments by day')
plt.xlabel('Days of week')
plt.ylabel('Number of Enrollments')
plt.show()


from scipy.stats import probplot, skew

# Loop through each numeric column
for column in df_feat.columns:
    fig, axes = plt.subplots(1, 3, figsize=(20, 4))

    # Distribution plot
    sns.histplot(df_feat[column], kde=False, ax=axes[0])
    axes[0].set_title(f"{column} | Distribution Plot")

    # Boxplot
    sns.boxplot(df_feat[column], ax=axes[1])
    axes[1].set_title(f"{column} | Boxplot")
    axes[1].set_yticklabels([])
    axes[1].set_yticks([])

    # Probability plot
    probplot(df_feat[column], plot=axes[2])
    skew_val = round(df_feat[column].skew(), 1)
    axes[2].set_title(f"{column} | Probability Plot - Skew: {skew_val}")

    # Display the plots
    plt.show()

# Count the number of courses per person in df_new
courses_per_person = df_new.groupby('Personen-ID')['Kursnummer'].nunique()
courses_per_person_df = courses_per_person.reset_index(name='Number of Courses')

# Plot the distribution of the number of courses per person
plt.figure(figsize=(10, 6))
sns.histplot(courses_per_person_df['Number of Courses'], color="purple", bins=30, kde=True, common_norm=True)
plt.title('Distribution of Number of Courses per Person (df_new)')
plt.xlabel('Number of Courses')
plt.ylabel('Probability Density')
plt.show()


import sklearn.tree
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X[, y, test_size=0.2, random_state=0)

X_test_summary = shap.kmeans(X_test, 50)
dtree = sklearn.tree.DecisionTreeClassifier(min_samples_split=2)
dtree.fit(X_train, y_train)
explainer = shap.KernelExplainer(dtree.predict_proba,  X_test_summary)
shap_values = explainer.shap_values(X_test)
shap.initjs()
shap.summary_plot(shap_values, X_test)


