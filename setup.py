from setuptools import find_packages, setup

setup(
    name="effcientdet-pytorch-singlefile",
    version="0.0.1",
    url="https://github.com/Kitsunetic/effcientdet-pytorch-singlefile",
    license="MIT",
    author="Kitsunetic",
    author_email="1996.jh.shim@gmail.com",
    description="effcientdet-pytorch-singlefile",
    packages=find_packages(),
    long_description=open("README.md").read(),
    zip_safe=False,
    setup_requires=["opencv-python", "numpy", "torch", "webcolors", "requests", "torchvision"],
    test_suite="nose.collector",
)
