
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

