import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bharat23", # Replace with your own username
    version="0.0.1",
    author="Bharat Sinha",
    author_email="bharat.sinha.2307@gmail.com",
    description="A plug-n-play package to start using new relic APIs for data gathering",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Bharat23/newrelic-api-parser",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

# curl -H "Accept: application/json" -H "X-Query-Key: a5dddf11c60833e89fd73b39e59438456aea2b0e0477d99" "https://insights-api.newrelic.com/v1/accounts/1690570/query?nrql=SELECT%20count(*)%20FROM%20PageView%20SINCE%2030%20MINUTES%20AGO%20COMPARE%20WITH%201%20WEEK%20AGO%20TIMESERIES"
