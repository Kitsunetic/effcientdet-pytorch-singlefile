from setuptools import find_packages, setup

setup(
    name="effdet_torch_singlefile",
    version="0.0.2",
    url="https://github.com/Kitsunetic/effcientdet-pytorch-singlefile",
    license="MIT",
    author="Kitsunetic",
    author_email="1996.jh.shim@gmail.com",
    description="effdet_torch_singlefile",
    packages=find_packages(),
    long_description=open("README.md").read(),
    zip_safe=False,
    setup_requires=["opencv-python", "numpy", "torch", "webcolors", "requests", "torchvision"],
    test_suite="nose.collector",
)
