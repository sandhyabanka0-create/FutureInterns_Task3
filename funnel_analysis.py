import pandas as pd
import matplotlib.pyplot as plt
import os

# Load dataset
df = pd.read_csv("data/bank-full.csv", sep=";")

# Create output folder
os.makedirs("output", exist_ok=True)

# ==============================
# OVERALL FUNNEL
# ==============================

total_contacts = len(df)
converted = (df["y"] == "yes").sum()
not_converted = (df["y"] == "no").sum()

conversion_rate = converted / total_contacts * 100
drop_off_rate = not_converted / total_contacts * 100

print("===== MARKETING FUNNEL ANALYSIS =====")
print(f"Total Contacts: {total_contacts}")
print(f"Converted Customers: {converted}")
print(f"Not Converted: {not_converted}")
print(f"Conversion Rate: {conversion_rate:.2f}%")
print(f"Drop-off Rate: {drop_off_rate:.2f}%")


# ==============================
# CONTACT CHANNEL
# ==============================

channel_analysis = df.groupby("contact")["y"].value_counts().unstack(fill_value=0)

channel_analysis["conversion_rate"] = (
    channel_analysis["yes"] /
    (channel_analysis["yes"] + channel_analysis["no"])
) * 100

print("\n===== CONVERSION BY CONTACT CHANNEL =====")
print(channel_analysis)


# ==============================
# JOB
# ==============================

job_analysis = df.groupby("job")["y"].value_counts().unstack(fill_value=0)

job_analysis["conversion_rate"] = (
    job_analysis["yes"] /
    (job_analysis["yes"] + job_analysis["no"])
) * 100

job_analysis = job_analysis.sort_values("conversion_rate", ascending=False)

print("\n===== CONVERSION BY JOB =====")
print(job_analysis)


# ==============================
# EDUCATION
# ==============================

education_analysis = df.groupby("education")["y"].value_counts().unstack(fill_value=0)

education_analysis["conversion_rate"] = (
    education_analysis["yes"] /
    (education_analysis["yes"] + education_analysis["no"])
) * 100

education_analysis = education_analysis.sort_values(
    "conversion_rate",
    ascending=False
)

print("\n===== CONVERSION BY EDUCATION =====")
print(education_analysis)


# ==============================
# HOUSING LOAN
# ==============================

housing_analysis = df.groupby("housing")["y"].value_counts().unstack(fill_value=0)

housing_analysis["conversion_rate"] = (
    housing_analysis["yes"] /
    (housing_analysis["yes"] + housing_analysis["no"])
) * 100

print("\n===== CONVERSION BY HOUSING LOAN =====")
print(housing_analysis)


# ==============================
# CHART 1 - CONTACT CHANNEL
# ==============================

plt.figure(figsize=(8, 5))
channel_analysis["conversion_rate"].plot(kind="bar")
plt.title("Conversion Rate by Contact Channel")
plt.xlabel("Contact Channel")
plt.ylabel("Conversion Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("output/conversion_by_channel.png")
plt.close()


# ==============================
# CHART 2 - JOB
# ==============================

plt.figure(figsize=(10, 6))
job_analysis["conversion_rate"].plot(kind="bar")
plt.title("Conversion Rate by Job")
plt.xlabel("Job")
plt.ylabel("Conversion Rate (%)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("output/conversion_by_job.png")
plt.close()


# ==============================
# CHART 3 - EDUCATION
# ==============================

plt.figure(figsize=(8, 5))
education_analysis["conversion_rate"].plot(kind="bar")
plt.title("Conversion Rate by Education")
plt.xlabel("Education")
plt.ylabel("Conversion Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("output/conversion_by_education.png")
plt.close()


# ==============================
# CHART 4 - HOUSING
# ==============================

plt.figure(figsize=(7, 5))
housing_analysis["conversion_rate"].plot(kind="bar")
plt.title("Conversion Rate by Housing Loan")
plt.xlabel("Housing Loan")
plt.ylabel("Conversion Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("output/conversion_by_housing.png")
plt.close()


# ==============================
# CHART 5 - FUNNEL
# ==============================

stages = ["Total Contacts", "Converted Customers"]
values = [total_contacts, converted]

plt.figure(figsize=(8, 5))
plt.bar(stages, values)
plt.title("Marketing Funnel")
plt.ylabel("Number of People")
plt.tight_layout()
plt.savefig("output/funnel_chart.png")
plt.close()


print("\n===== ALL CHARTS CREATED =====")
print("conversion_by_channel.png")
print("conversion_by_job.png")
print("conversion_by_education.png")
print("conversion_by_housing.png")
print("funnel_chart.png")