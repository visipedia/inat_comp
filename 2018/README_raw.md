![Banner](https://rawgit.com/visipedia/inat_comp/master/assets/banner2018.jpg)

# iNaturalist 2018 Competition
The 2018 competition is part of the [FGVC^5 workshop](https://sites.google.com/view/fgvc5/home) at [CVPR](http://cvpr2018.thecvf.com/).

Please open an issue if you have questions or problems with the dataset.

## Updates
June 23rd, 2018: 
  * Un-obfuscated names are released. Simply replace the `categories` list in the dataset files with the list found in this [file](http://www.vision.caltech.edu/~gvanhorn/datasets/inaturalist/fgvc5_competition/categories.json.tar.gz).

  * Thanks to everyone who attended and participated in the [FGVC5 workshop](https://sites.google.com/view/fgvc5/home)! Slides from the competition overview and presentations from the top two teams can be found [here](https://www.dropbox.com/s/52nz6qc3zcwqhoa/iNaturalist_Competition_FGVC_2018.pdf?dl=0).

  * A video of the validation images can be viewed [here](https://www.youtube.com/watch?v=LNq1rCUf7v4).

April 10th, 2018: Bounding boxes have been added to the 2017 dataset, see [here](2017/README.md#bounding-boxes).

## Kaggle
We are using Kaggle to host the leaderboard. Checkout the competition page [here](https://www.kaggle.com/c/inaturalist-2018).

## Dates
|||
|------|---------------|
Data Released|February, 2018|
Submission Server Open |February, 2018|
Submission Deadline|June, 2018|
Winners Announced|June, 2018|

## Details
There are a total of 8,142 species in the dataset, with 437,513 training and 24,426 validation images.

| Super Category |	Category Count	| Train Images |	Val Images |
|------|---------------|-------------|---------------|
Plantae|2,917|118,800|8,751|
Insecta|2,031|87,192|6,093|
Aves|1,258|143,950|3,774|
Actinopterygii|369|7,835|1,107|
Fungi|321|6,864|963|
Reptilia|284|22,754|852|
Mollusca|262|8,007|786|
Mammalia|234|20,104|702|
Animalia|178|5,966|534|
Amphibia|144|11,156|432|
Arachnida|114|4,037|342|
Chromista|25|621|75|
Protozoa|4|211|12|
Bacteria|1|16|3|
|||||
Total|8,142|437,513|24,426|

![Train Val Distribution](https://rawgit.com/visipedia/inat_comp/master/assets/train_val_distribution.png)

## Video
Click on the image below to view a video showing images from the validation set.
[![Video](https://rawgit.com/visipedia/inat_comp/master/assets/inat2018_video.png)](https://www.youtube.com/watch?v=LNq1rCUf7v4)

## Evaluation
We follow a similar metric to the classification tasks of the [ILSVRC](http://image-net.org/challenges/LSVRC/2016/index#scene). For each image $i$, an algorithm will produce 3 labels $l_{ij}$, $j=1,\ldots,3$. We allow 3 labels because some categories are disambiguated with additional data provided by the observer, such as latitude, longitude and date. For a small percentage of images, it might also be the case that multiple categories occur in an image (e.g. a photo of a bee on a flower). For this competition each image has one ground truth label $g_i$, and the error for that image is:
$$
e_i = \min_{j}d(l_{ij}, g_i)
$$
Where
$$
d(x, y) =
\begin{cases}
    0       & \quad \text{if } x = y \\
    1  & \quad \text{otherwise}\\
\end{cases}
$$

The overall error score for an algorithm is the average error over all $N$ test images:
$$
\text{score} = \frac{1}{N} \sum_{i} e_{i}
$$

## Differences from iNaturalist 2017 Competition
The 2018 competition differs from the [2017 Competition](2017/README.md) in several ways:

### Species Only
The 2017 dataset categories contained mostly species, but also had a few additional taxonomic ranks (e.g. genus, subspecies, and variety). The 2018 categories are all species.

### Taxonomy Information & Obfuscation
The 2018 dataset contains kingdom, phylum, class, order, family, and genus taxonomic information for all species. However, we have obfuscated all taxonomic names (including the species name) to hinder participants from performing web searchs to collect additional data.

### Data Overlap
The 2018 dataset contains some species and images that are found in the 2017 dataset. However, we will not provide a mapping between the two datasets.

### Scoring Metric
The 2018 competition allows for 3 guesses per test image, whereas the 2017 competition allowed 5.

## Guidelines

Participants are welcome to use the [iNaturalist 2017 Competition dataset](2017/README.md) as an additional data source. There is an overlap between the 2017 species and the 2018 species, however we do not provide a mapping between the two datasets. Besides using the 2017 dataset, participants are restricted from collecting additional natural world data for the 2018 competition. Pretrained models may be used to construct the algorithms (e.g. ImageNet pretrained models, or iNaturalist 2017 pretrained models). Please specify any and all external data used for training when uploading results.

The general rule is that participants should only use the provided training and validation images (with the exception of the allowed pretrained models) to train a model to classify the test images. We do not want participants crawling the web in search of additional data for the target categories. Participants should be in the mindset that this is the only data available for these categories.

Participants are allowed to collect additional annotations (e.g. bounding boxes, keypoints) on the provided training and validation sets. Teams should specify that they collected additional annotations when submitting results.

## Annotation Format
We follow the annotation format of the [COCO dataset](http://mscoco.org/dataset/#download) and add additional fields. The annotations are stored in the [JSON format](http://www.json.org/) and are organized as follows:
```
{
  "info" : info,
  "images" : [image],
  "categories" : [category],
  "annotations" : [annotation],
  "licenses" : [license]
}

info{
  "year" : int,
  "version" : str,
  "description" : str,
  "contributor" : str,
  "url" : str,
  "date_created" : datetime,
}

image{
  "id" : int,
  "width" : int,
  "height" : int,
  "file_name" : str,
  "license" : int,
  "rights_holder" : str
}

category{
  "id" : int,
  "name" : str,
  "supercategory" : str,
  "kingdom" : str,
  "phylum" : str,
  "class" : str,
  "order" : str,
  "family" : str,
  "genus" : str
}

annotation{
  "id" : int,
  "image_id" : int,
  "category_id" : int
}

license{
  "id" : int,
  "name" : str,
  "url" : str
}
```

## Submission Format

The submission format for the Kaggle competition is a csv file with the following format:
```
id,predicted
12345,0 78 23
67890,83 13 42
```
The `id` column corresponds to the test image id. The `predicted` column corresponds to 3 category ids, separated by spaces. You should have one row for each test image. Please sort your predictions from most confident to least, from left to right, this will allow us to study top-1, top-2, and top-3 accuracy.

## Terms of Use

By downloading this dataset you agree to the following terms:

1. You will abide by the [iNaturalist Terms of Service](https://www.inaturalist.org/pages/terms)
2. You will use the data only for non-commercial research and educational purposes.
3. You will NOT distribute the above images.
4. The California Institute of Technology makes no representations or warranties regarding the data, including but not limited to warranties of non-infringement or fitness for a particular purpose.
5. You accept full responsibility for your use of the data and shall defend and indemnify the California Institute of Technology, including its employees, officers and agents, against any and all claims arising from your use of the data, including but not limited to your use of any copies of copyrighted images that you may create from the data.

## Data

Download the dataset files here:
  * All training and validation images [120GB]
      * Links for different parts of the world:
          * [North America](https://storage.googleapis.com/inat_data_2018_us/train_val2018.tar.gz)
          * [Asia](https://storage.googleapis.com/inat_data_2018_asia/train_val2018.tar.gz)
          * [Europe](https://storage.googleapis.com/inat_data_2018_eu/train_val2018.tar.gz)
      * Posterity [Caltech link](http://www.vision.caltech.edu/~gvanhorn/datasets/inaturalist/fgvc5_competition/train_val2018.tar.gz). Warning this will be slow.
      * Running `md5sum train_val2018.tar.gz` should produce `b1c6952ce38f31868cc50ea72d066cc3`
      * Images have a max dimension of 800px and have been converted to JPEG format
      * Untaring the images creates a directory structure like `train_val2018/super category/category/image.jpg`. This may take a while.
  * Training annotations [26MB]
      * Links for different parts of the world:
          * [North America](https://storage.googleapis.com/inat_data_2018_us/train2018.json.tar.gz)
          * [Asia](https://storage.googleapis.com/inat_data_2018_asia/train2018.json.tar.gz)
          * [Europe](https://storage.googleapis.com/inat_data_2018_eu/train2018.json.tar.gz)
      * Posterity [Caltech link](http://www.vision.caltech.edu/~gvanhorn/datasets/inaturalist/fgvc5_competition/train2018.json.tar.gz)
      * Running `md5sum train2018.json.tar.gz` should produce `bfa29d89d629cbf04d826a720c0a68b0`
  * Validation annotations [26MB]
      * Links for different parts of the world:
          * [North America](https://storage.googleapis.com/inat_data_2018_us/val2018.json.tar.gz)
          * [Asia](https://storage.googleapis.com/inat_data_2018_asia/val2018.json.tar.gz)
          * [Europe](https://storage.googleapis.com/inat_data_2018_eu/val2018.json.tar.gz)
      * Posterity [Caltech link](http://www.vision.caltech.edu/~gvanhorn/datasets/inaturalist/fgvc5_competition/val2018.json.tar.gz)
      * Running `md5sum val2018.json.tar.gz` should produce `f2ed8bfe3e9901cdefceb4e53cd3775d`
  * Test images [40GB]
      * Links for different parts of the world:
          * [North America](https://storage.googleapis.com/inat_data_2018_us/test2018.tar.gz)
          * [Asia](https://storage.googleapis.com/inat_data_2018_asia/test2018.tar.gz)
          * [Europe](https://storage.googleapis.com/inat_data_2018_eu/test2018.tar.gz)
      * Posterity [Caltech link](http://www.vision.caltech.edu/~gvanhorn/datasets/inaturalist/fgvc5_competition/test2018.tar.gz). Warning this will be slow.
      * Running `md5sum test2018.tar.gz` should produce `4b71d44d73e27475eefea68886c7d1b1`
      * Images have a max dimension of 800px and have been converted to JPEG format
      * Untaring the images creates a directory structure like `test2018/image.jpg`.
  * Test image info [6.3MB]
      * Links for different parts of the world:
          * [North America](https://storage.googleapis.com/inat_data_2018_us/test2018.json.tar.gz)
          * [Asia](https://storage.googleapis.com/inat_data_2018_asia/test2018.json.tar.gz)
          * [Europe](https://storage.googleapis.com/inat_data_2018_eu/test2018.json.tar.gz)
      * Posterity [Caltech link](http://www.vision.caltech.edu/~gvanhorn/datasets/inaturalist/fgvc5_competition/test2018.json.tar.gz)
      * Running `md5sum test2018.json.tar.gz` should produce `fc717a7f53ac72ed8b250221a08a4502`

## Pretrained Models

A pretrained InceptionV3 model in PyTorch is available [here](https://github.com/macaodha/inat_comp_2018).

## Previous Competitions

* [2017 Competition](2017/README.md)
